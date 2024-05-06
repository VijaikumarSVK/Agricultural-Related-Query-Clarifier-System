<h1>Agricultural Query Clarifier System using BERT:</h1><br>
This repository contains the code and data for an agricultural query clarifier system developed as a Master of Computer Applications project. The system uses a BERT model to analyze and understand farmer queries, providing them with relevant and accurate information.<br><br>

<h3>Project Motivation:</h3>
In India, access to reliable agricultural information is crucial for farmers to improve their crop yields and make informed decisions. However, traditional methods like field officers and government portals often fall short due to accessibility, language barriers, and lack of 24/7 availability. This project aims to bridge this gap by utilizing NLP and AI to offer a user-friendly and efficient solution for farmers to access critical agricultural knowledge.<br><br>

<h3>System Overview:</h3>
The system comprises several modules:<br>
<b></b>Dataset Generation:</b> Downloads and preprocesses data from the Kisan Call Center (KCC) in JSON format, converting it to CSV for further processing.<br>
<b>Data Cleaning:</b> Cleans the dataset by removing punctuation, translating languages, applying tokenization and lowercasing, removing stop words, and stemming.<br>
<b>Data Frame Creation:</b> Structures the data into a data frame with relevant features like query, query type, state, district, time of query, and list of corresponding answers.<br>
<b>Model Training:</b> Trains a Sentence-BERT model on the data frame to generate sentence embeddings for accurate similarity comparisons.<br>
<b>Answer Mapping:</b> Analyzes user queries, finds the most similar queries in the training data using cosine similarity, and ranks the answers using a modified Lesk algorithm for localized relevance.<br><br>

<h3>Technologies Used</h3>
<b>Python:</b> Primary programming language for the project.<br>
<b>TensorFlow:</b> Framework for building and training the BERT model.<br>
<b>NumPy:</b> Library for numerical computations.<br>
<b>NLTK:</b> Natural Language Toolkit for text processing tasks.<br>
<b>Flask:</b> Framework for creating the user interface.<br>
<b>Google Colab:</b> Cloud-based platform for development and training.<br><br>

<h3>Results and Performance</h3>
The system achieved an accuracy of 92% in identifying the most relevant answers to user queries. The use of entity extraction and dimensional optimization further enhanced the model's performance.<br><br>

<h3>Future Work</h3>
Potential future enhancements include:<br>
<b>Multilingual Support:</b> Expanding language capabilities to cater to a wider range of users.<br>
<b>Voice-Over Support:</b> Integrating voice recognition and synthesis for improved accessibility.<br>
<b>Knowledge Graph Generation:</b> Extracting entities and relationships from answers to build a knowledge graph for deeper understanding and reasoning.<br><br>

<h3>Getting Started</h3>
Clone the repository.<br>
Install the required libraries.<br>
Download the KCC dataset and place it in the appropriate directory.<br>
Run the scripts to train the model and start the application.<br><br>

<b>Please refer to the project report (Vijai_Kumar_S_FYP_Thesis.pdf) for detailed information about the system design, implementation, and results.</b>
