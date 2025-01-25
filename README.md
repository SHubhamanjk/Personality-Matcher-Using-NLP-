# Personality Matcher Using NLP

## Overview
The **Personality Matcher Using NLP** is a Streamlit-based web application that processes WhatsApp chat data and identifies individuals with similar conversation patterns based on their text messages. It uses Natural Language Processing (NLP) techniques, including text vectorization and cosine similarity, to calculate the similarity between users.

## Features
- **File Upload**: Upload a WhatsApp chat file in `.txt` format.
- **Similarity Calculation**: Calculate text similarity between users based on their spoken text.
- **Name Selection**: Select or type a user's name to find similar individuals.
- **Interactive UI**: Provides a user-friendly interface for selecting names and viewing results.

## Requirements

To run the application, you need to have the following installed:

- Python 3.7 or higher
- Streamlit
- Pandas
- Scikit-learn

## Installation

1. Clone the repository or download the source code.
   ```bash
   git clone https://github.com/SHubhamanjk/Personality-Matcher-Using-NLP-
   cd https://github.com/SHubhamanjk/Personality-Matcher-Using-NLP-
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## How to Use

1. **Prepare Your Chat File**: Export your WhatsApp chat as a `.txt` file. Ensure the file contains timestamped messages in the following format:
   ```
   12/1/2025, 10:30 AM - John Doe: Hello everyone!
   ```
2. **Upload the Chat File**: Use the file uploader in the app to upload your chat file.
3. **Select or Type a Name**: Choose a name from the dropdown menu or type a name in the input field.
4. **View Results**: The app displays the top 4 individuals with the most similar conversation patterns to the selected user.

## Application Logic

### 1. Process Chat Data
The `process_chat` function processes the uploaded chat file and extracts:
- **Name**: The sender of the message.
- **Spoken Text**: Combined text messages from each sender.

### 2. Text Vectorization
The `CountVectorizer` converts the spoken text into numerical vectors. The `max_features` parameter is dynamically set based on the number of unique users.

### 3. Similarity Calculation
Cosine similarity is used to calculate the similarity scores between users based on their text vectors.

### 4. Results Display
The `check` function identifies the top 4 users with the highest similarity scores to the selected user and displays the results.

## Example Output

- **Input**: Selected or typed user name (e.g., `John Doe`).
- **Output**:
  ```
  Jane Smith: 0.87
  Bob Johnson: 0.82
  Alice Brown: 0.79
  Charlie Davis: 0.75
  ```

## File Structure
```
|-- app.py               # Main application script
|-- requirements.txt     # Dependencies list
|-- README.md            # Project documentation
```


