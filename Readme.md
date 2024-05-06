Agricultural Query Clarifier System using BERT:
This repository contains the code and data for an agricultural query clarifier system developed as a Master of Computer Applications project. The system uses a BERT model to analyze and understand farmer queries, providing them with relevant and accurate information.

Project Motivation:
In India, access to reliable agricultural information is crucial for farmers to improve their crop yields and make informed decisions. However, traditional methods like field officers and government portals often fall short due to accessibility, language barriers, and lack of 24/7 availability. This project aims to bridge this gap by utilizing NLP and AI to offer a user-friendly and efficient solution for farmers to access critical agricultural knowledge.

System Overview
The system comprises several modules:
Dataset Generation: Downloads and preprocesses data from the Kisan Call Center (KCC) in JSON format, converting it to CSV for further processing.
Data Cleaning: Cleans the dataset by removing punctuation, translating languages, applying tokenization and lowercasing, removing stop words, and stemming.
Data Frame Creation: Structures the data into a data frame with relevant features like query, query type, state, district, time of query, and list of corresponding answers.
Model Training: Trains a Sentence-BERT model on the data frame to generate sentence embeddings for accurate similarity comparisons.
Answer Mapping: Analyzes user queries, finds the most similar queries in the training data using cosine similarity, and ranks the answers using a modified Lesk algorithm for localized relevance.

Technologies Used
Python: Primary programming language for the project.
TensorFlow: Framework for building and training the BERT model.
NumPy: Library for numerical computations.
NLTK: Natural Language Toolkit for text processing tasks.
Flask: Framework for creating the user interface.
Google Colab: Cloud-based platform for development and training.

Results and Performance
The system achieved an accuracy of 86% in identifying the most relevant answers to user queries. The use of entity extraction and dimensional optimization further enhanced the model's performance.

Future Work
Potential future enhancements include:
Multilingual Support: Expanding language capabilities to cater to a wider range of users.
Voice-Over Support: Integrating voice recognition and synthesis for improved accessibility.
Knowledge Graph Generation: Extracting entities and relationships from answers to build a knowledge graph for deeper understanding and reasoning.

Getting Started
Clone the repository.
Install the required libraries.
Download the KCC dataset and place it in the appropriate directory.
Run the scripts to train the model and start the application.

Please refer to the project report (Vijai_Kumar_S_FYP_Thesis.pdf) for detailed information about the system design, implementation, and results.