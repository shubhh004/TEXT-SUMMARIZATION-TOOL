import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import spacy
from collections import defaultdict

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    """
    Summarize the input text by extracting the most important sentences.
    
    Args:
        text (str): The input text to summarize
        num_sentences (int): Number of sentences in the summary
        
    Returns:
        str: The summarized text
    """
    # Load the English language model for spaCy
    nlp = spacy.load('en_core_web_sm')
    
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Remove stopwords and punctuation, then tokenize words
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Calculate word frequencies
    freq_table = defaultdict(int)
    for word in words:
        freq_table[word] += 1
    
    # Calculate sentence scores based on word frequencies
    sentence_scores = defaultdict(int)
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                sentence_scores[i] += freq_table[word]
    
    # Get the top N sentences
    top_sentences_indices = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    # Sort the top sentences by their original order
    summarized_sentences = [sentences[i] for i in sorted(top_sentences_indices)]
    
    # Join the sentences to form the summary
    summary = ' '.join(summarized_sentences)
    
    return summary

def main():
    print("TEXT SUMMARIZATION TOOL")
    print("=======================")
    
    # Get input text
    input_text = input("Paste your text here (press Enter twice to finish):\n")
    
    # For multi-line input, keep reading until two consecutive newlines
    while True:
        line = input()
        if not line:
            break
        input_text += "\n" + line
    
    if not input_text.strip():
        print("No input text provided.")
        return
    
    # Generate and display the summary
    print("\nSUMMARY:")
    print("========")
    summary = summarize_text(input_text)
    print(summary)

if __name__ == "__main__":
    main()

