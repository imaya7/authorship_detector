import os
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.util import ngrams  
from collections import Counter
import spacy

# Download necessary NLTK resources
nltk.download('punkt') # model for tokenization
nltk.download('stopwords') # stopwords am, the 
nltk.download('wordnet') # lemmatization

# Define the file path
file_path = r"C:\Users\trash\Downloads\RJ_Lovecraft (1).txt"

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file at {file_path} does not exist.")

# Load text from the file

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

def analyze_text(text):
    # Tokenization 
    tokens = word_tokenize(text.lower())
    
    # Remove punctuation and non-alphabetic tokens
    tokens = [token for token in tokens if token.isalpha()]
    
    # Initialize stemmer and lemmatizer
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    
    # Stemming and lemmatization
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    filtered_stems = [token for token in stemmed_tokens if token not in stop_words]
    filtered_lemmas = [token for token in lemmatized_tokens if token not in stop_words]
    
    # Count frequencies
    token_freq = FreqDist(filtered_tokens)
    stem_freq = FreqDist(filtered_stems)
    lemma_freq = FreqDist(filtered_lemmas)
    
    print("=== TOKENIZATION RESULTS ===")
    print(f"Total tokens: {len(tokens)}")
    print(f"Unique tokens: {len(set(tokens))}")
    print("\n20 Most common tokens:")
    for token, count in token_freq.most_common(20):
        print(f"{token}: {count}")
    
    print("\n=== STEMMING RESULTS ===")
    print("\n20 Most common stems:")
    for stem, count in stem_freq.most_common(20):
        print(f"{stem}: {count}")
    
    print("\n=== LEMMATIZATION RESULTS ===")
    print("\n20 Most common lemmas:")
    for lemma, count in lemma_freq.most_common(20):
        print(f"{lemma}: {count}")
              
    # Perform N-Gram Analysis (Trigrams)
    trigrams = list(ngrams(filtered_tokens, 3))  # Generate trigrams
    trigram_freq = FreqDist(trigrams)  # Count trigram frequencies
    
    print("\n=== TRIGRAM ANALYSIS ===")
    print("\n20 Most common trigrams:")
    for trigram, count in trigram_freq.most_common(20):
        print(f"{' '.join(trigram)}: {count}")
    
    # Named Entity Recognition using spaCy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    # Extract entities
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        if ent.text not in entities[ent.label_]:
            entities[ent.label_].append(ent.text)
    
    # Count entity mentions
    entity_mentions = Counter([ent.text for ent in doc.ents])
    
    print("\n=== NAMED ENTITY RECOGNITION ===")
    total_entities = sum(len(entities[label]) for label in entities)
    total_mentions = sum(entity_mentions.values())
    
    print(f"Total unique entities: {total_entities}")
    print(f"Total entity mentions: {total_mentions}")
    
    for label in entities:
        print(f"\n{label}:")
        for entity in entities[label]:
            print(f"  - {entity} ({entity_mentions[entity]} mentions)")

# Run the analysis
analyze_text(text)
