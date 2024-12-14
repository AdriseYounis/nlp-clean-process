import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
import re

nltk.data.path.append('~/nltk_data') 

nltk.download('punkt', download_dir='~/nltk_data')
nltk.download('stopwords', download_dir='~/nltk_data')
nltk.download('wordnet', download_dir='~/nltk_data')
nltk.download('averaged_perceptron_tagger', download_dir='~/nltk_data')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    
    lemmatizer = WordNetLemmatizer()
    lemmatizer_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    
    return {
        "cleaned_text": ' '.join(filtered_tokens),
        "stemmed_tokens": stemmed_tokens,
        "lemmatizer_tokens": lemmatizer_tokens
    }

def preprocess_text_with_pos(text):
    tokens = word_tokenize(text.lower())
    
    pos_tags = pos_tag(tokens)
    
    lemmatizer = WordNetLemmatizer()
    lemmatizer_tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]
    return lemmatizer_tokens
    
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

sample_text = "John has 5 years of experience in software development. He is proficient in Python, Java, and SQL. His previous role involved building scalable applications."

result = preprocess_text(sample_text)

print("Cleaned Text:", result["cleaned_text"])
print("stemmed Tokens:", result["stemmed_tokens"])
print("Lemmatizer Tokens:", result["lemmatizer_tokens"])

text = "Building multiple software engineering teams."
lemmatized_output = preprocess_text_with_pos(text)

print("Lemmatized Input with POS:", text)
print("Lemmatized Output with POS:", lemmatized_output)