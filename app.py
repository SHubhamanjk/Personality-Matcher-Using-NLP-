import streamlit as st
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def process_chat(file):
    chat_data = {}
    pattern = r"(\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}\s?[APMapm]{2}) - ([^:]+): (.+)"

    for line in file:
        line = line.decode("utf-8").strip()
        match = re.match(pattern, line)
        if match:
            timestamp, sender, message = match.groups()

            if message == "<Media omitted>":
                continue

            if sender not in chat_data:
                chat_data[sender] = message
            else:
                chat_data[sender] += " " + message

    chat_df = pd.DataFrame(list(chat_data.items()), columns=['Name', 'Spoken Text'])

    return chat_df

def loader(chat):
    global chat_data, similarity
    chat_data = chat
    max_features = max(1, len(chat_data))  
    cv = CountVectorizer(max_features=max_features, stop_words='english')
    vectors = cv.fit_transform(chat_data['Spoken Text']).toarray()
    similarity = cosine_similarity(vectors)

def check(name):
    """Find and display the most similar individuals based on spoken text."""
    index = chat_data[chat_data['Name'] == name].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1]
    )
    results = []
    for i in distances[1:5]:
        matched_name = chat_data.iloc[i[0]].Name
        similarity_score = i[1]
        results.append((matched_name, similarity_score))
    return results

st.title("Personality Matcher")

uploaded_file = st.file_uploader("Upload your chat data (TXT file with WhatsApp chat format):", type="txt")

if uploaded_file is not None:
    chat = process_chat(uploaded_file)
    loader(chat)

    name_list = chat_data['Name'].unique()
    selected_name = st.selectbox("Select a Name:", options=name_list)


    if selected_name:
        st.write(f"Results for: {selected_name}")

        results = check(selected_name)
        for matched_name, score in results:
            st.write(f"{matched_name}: {score*100:.2f}")
    else:
        st.write("Select from the dropdown.")
else:
    st.write("Please upload a chat data file to begin.")
