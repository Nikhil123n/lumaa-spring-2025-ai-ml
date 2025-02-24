import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load stopwords
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """Cleans and preprocesses movie plot descriptions."""
    if pd.isna(text):
        return ""
    # Lowercasing the text
    text = text.lower()  
    # Removing special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  
    # Tokenizing and filtering stopwords
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_text)

def load_data(csv_path="./Top_Movies.csv"):
    """Loads movie dataset from a CSV file containing 'Movie Name' and 'Plot'."""
    return pd.read_csv(csv_path)

def recommend_movies(user_input, df, vectorizer, tfidf_matrix, top_n=5):
    """Recommends top N movies based on similarity to user input."""
    # Preprocess the user input text
    user_tfidf = vectorizer.transform([preprocess_text(user_input)])
    # Calculate cosine similarity between the user input and all movie plots
    similarity_scores = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    top_indices = similarity_scores.argsort()[-top_n:][::-1]  # Get top N similar movies
    
    # Prepare and return recommendations
    recommendations = df.iloc[top_indices][['Movie Name', 'Plot']].copy()
    recommendations['SimilarityScore'] = similarity_scores[top_indices]
    recommendations = recommendations.drop_duplicates(subset=['Movie Name'])
    return recommendations

def main():
    """Main function to run the recommendation system."""
    # Load dataset and preprocess movie plots
    movie_df = load_data()  
    movie_df['ProcessedPlot'] = movie_df['Plot'].apply(preprocess_text)

    # Initialize TF-IDF Vectorizer and compute the TF-IDF matrix for all movie plots
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(movie_df['ProcessedPlot'])

    print("\nWelcome to the Movie Recommendation System!")
    print("Enter a movie description, or type 'exit' to quit.")

    while True:
        # Get user input for a movie description query
        user_query = input("\nEnter your movie description: ")
        
        # Exit condition
        if user_query.lower() in ['exit', 'quit']:
            print("Exiting the program. Goodbye!")
            break
        
        # Get and display recommendations
        recommendations = recommend_movies(user_query, movie_df, vectorizer, tfidf_matrix)
        if recommendations.empty:
            print("\nNo recommendations found. Try a different description.")
        else:
            print(f"\nTop 5 movie recommendations:\n")
            print(recommendations[['Movie Name', 'Plot', 'SimilarityScore']])

# Start the program
if __name__ == "__main__":
    main()
