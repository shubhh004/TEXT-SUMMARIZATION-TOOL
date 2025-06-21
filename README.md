# TEXT-SUMMARIZATION-TOOL

COMPANY: CODTECH IT SOLUTION 

NAME: SHUBH CHAURASIA

INTERN ID: CT04DN889

DOMAIN: ARTIFICIAL INTELLIGENCE

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH 

Project Overview
The Text Summarization Tool is a Python-based application that automatically generates concise summaries from lengthy articles or documents using Natural Language Processing (NLP) techniques. This tool is designed to help users quickly extract key information from large volumes of text, making it useful for students, researchers, and professionals who need to process large documents efficiently.
The summarization process follows an extractive summarization approach, where the most important sentences are identified and extracted based on word frequency and sentence scoring. The tool is built using the NLTK (Natural Language Toolkit) and spaCy libraries, which provide essential NLP functionalities such as tokenization, stop-word removal, and sentence scoring.

Features
Input Flexibility: Accepts multi-line text input directly from the user.
Customizable Summary Length: Allows users to control the number of sentences in the summary.
Stop-Word Removal: Filters out common words (e.g., "the," "is," "and") to focus on meaningful content.
Sentence Scoring: Ranks sentences based on word importance to generate a coherent summary.
User-Friendly Interface: Simple command-line interaction for ease of use.

Technical Details
Algorithm & Working
Sentence Tokenization: The input text is split into individual sentences using NLTK’s sent_tokenize().
Word Tokenization & Cleaning:
Words are extracted and converted to lowercase.
Stop-words (e.g., "the," "is") are removed to focus on meaningful terms.
Frequency Analysis:
Each word's frequency is calculated to determine its importance.
Sentence Scoring:
Sentences are scored based on the sum of their words' frequencies.

Summary Extraction:
The top-scoring sentences are selected and combined to form the summary.
Libraries Used
NLTK: For tokenization and stop-word removal.
spaCy: For advanced NLP processing (optional for improved accuracy).
