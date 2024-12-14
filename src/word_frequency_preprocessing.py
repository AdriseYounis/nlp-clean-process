from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

data = ['I love programming', 'I love coding', 'I enjoy coding programming']

#Bag of words(BOW) apporach 
count_vectorizer = CountVectorizer()
x_bow = count_vectorizer.fit_transform(data)
print("Bow vectors:\n", x_bow.toarray())
print("Feature names (Vocabulary)", count_vectorizer.get_feature_names_out())

#TF-IDF

tfidf_vectorizer = TfidfVectorizer()
x_tfidf = tfidf_vectorizer.fit_transform(data)

print("\nTF-IDF Vectors:\n", x_tfidf.toarray())
print("Feature Names (Vocabulary):", tfidf_vectorizer.get_feature_names_out())