# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from surprise import Reader, Dataset, SVD
from surprise.model_selection import train_test_split
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load data
books_df = pd.read_csv('Books.csv', low_memory=False)
ratings_df = pd.read_csv('ratings.csv')

# Convert Pandas DataFrame to Surprise Dataset
reader = Reader(rating_scale=(1, 10))
data = Dataset.load_from_df(ratings_df[['User-ID', 'ISBN', 'Book-Rating']], reader)

# Split the data into train and test sets
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Initialize and train the recommendation model
model = SVD()
model.fit(trainset)

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for recommendation
# Update the Flask route for the /recommend endpoint
@app.route('/recommend', methods=['POST'])
def recommend_books():
    # Get user ID from form submission
    user_id = int(request.form['user_id'])

    # Get books the user has not rated
    rated_books = set(ratings_df[ratings_df['User-ID'] == user_id]['ISBN'])
    all_books = set(books_df['ISBN'])
    unrated_books = list(all_books - rated_books)

    # Make predictions for unrated books
    predictions = []
    for isbn in unrated_books:
        prediction = model.predict(user_id, isbn)
        # Get book title and author
        book_title = books_df.loc[books_df['ISBN'] == isbn, 'Book-Title'].values[0]
        book_author = books_df.loc[books_df['ISBN'] == isbn, 'Book-Author'].values[0]
        predictions.append(
            {'ISBN': isbn, 'Book-Title': book_title, 'Book-Author': book_author, 'predicted_rating': prediction.est})

    # Sort predictions by predicted rating
    predictions.sort(key=lambda x: x['predicted_rating'], reverse=True)

    # Return top N recommendations along with user ID
    top_n = 10
    recommended_books = predictions[:top_n]

    return render_template('recommendations.html', recommended_books=recommended_books, user_id=user_id)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
