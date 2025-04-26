# authorship_detector


## Overview
The code files  is a Python program designed to perform comprehensive text analysis on a given text file. It utilizes Natural Language Processing (NLP) libraries such as NLTK and spaCy to process, analyze, and extract meaningful insights from the text. The script includes functionalities like tokenization, stemming, lemmatization, stopword removal, n-gram analysis, and named entity recognition (NER). 

## Purpose 
The purpose of these code files is to determine the likely author of the fourth text file by applying various Natural Language Processing (NLP) techniques. The analysis involves examining linguistic patterns in the three other text files and comparing them to the fourth. This includes processes such as trigram frequency analysis, lemmatization, stemming, tokenization, and named entity recognition. By running these techniques on each file, the code aims to identify stylistic and lexical similarities that could suggest whether any of the authors of the first three texts also wrote the fourth.

## Files 
- Copilot Chat log.docx - copilot help
- Findings.docx - concludes all findings over the four txt files 
- Martin.txt - also known as four file/txt
- RJ_Lovecraft (1).txt - also know as first file/txt
- RJ_Martin.txt - also know as third file/txt
- RJ_Tolkein.txt - also know as second file/txt 
- fourN.py - script using the Martin.txt
- oneN.py - script using the RJ_Lovecraft (1).txt
- threeN.py - script using the RJ_Martin.txt
- twoN.py - script using the RJ_Tolkein.txt



# Libraries
-  os
- re
- nltk
- nltk.tokenize import word_tokenize
- nltk.corpus import stopwords
- nltk.stem import PorterStemmer, WordNetLemmatizer
- nltk.probability import FreqDist
- nltk.util import ngrams  
- collections import Counter
- spacy

---

## Features
1. **Tokenization**:
   - Splits the text into individual words (tokens) while converting them to lowercase.
   - Filters out non-alphabetic tokens (e.g., punctuation, numbers).

2. **Stopword Removal**:
   - Removes common English stopwords (e.g., "the", "and", "is") using NLTK's stopword list.

3. **Stemming and Lemmatization**:
   - Stemming: Reduces words to their root forms using the Porter Stemmer.
   - Lemmatization: Converts words to their base forms using WordNet Lemmatizer.

4. **Frequency Analysis**:
   - Calculates the frequency of tokens, stems, and lemmas.
   - Displays the 20 most common tokens, stems, and lemmas.

5. **N-Gram Analysis**:
   - Generates trigrams (sequences of three consecutive words) from the filtered tokens.
   - Displays the 20 most common trigrams.

6. **Named Entity Recognition (NER)**:
   - Identifies named entities (e.g., people, locations, organizations) in the text using spaCy's `en_core_web_sm` model.
   - Counts and categorizes entities by type (e.g., PERSON, GPE, ORG).
   - Displays the total number of unique entities and mentions.

---

## Prerequisites
Before running the script, ensure the following dependencies are installed:
- Python 3.x
- Libraries:
  - `nltk`
  - `spacy`

To install the required libraries, run:
```bash
pip install nltk spacy
```

Additionally, download the necessary NLTK resources and spaCy model:
```bash
python -m nltk.downloader punkt stopwords wordnet
python -m spacy download en_core_web_sm
```

---


## Output
The script outputs the following results to the console:
1. Tokenization results:
   - Total tokens
   - Unique tokens
   - 20 most common tokens
2. Stemming and lemmatization results:
   - 20 most common stems
   - 20 most common lemmas
3. N-Gram analysis:
   - 20 most common trigrams
4. Named Entity Recognition (NER):
   - Total unique entities
   - Total entity mentions
   - Entities categorized by type with their mention counts

---

## Error Handling
- If the input file does not exist, the script raises a `FileNotFoundError` with a descriptive message.

---

## Customization
To analyze a different text file:
1. Update the `file_path` variable with the path to your desired file.
2. Ensure the file is accessible and encoded in UTF-8.


## limitations 
1. File Dependency: The file is dependent on (RJ_Lovecraft (1).txt) which may limite the flexability to analyzing other txt files 
2. Stopword Removal: The stopword removal process uses NLTK's default English stopword list, which may not be comprehensive or suitable for all text types or domains.
3. txt files : All txt files were generated and prompted using AI so results are inconclusive
