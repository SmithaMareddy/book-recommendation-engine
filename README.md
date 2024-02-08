# Book Recommendation Engine

Welcome to the Book Recommendation Engine project! This project provides book recommendations based on user ratings using collaborative filtering techniques.

## Data Source

The project utilizes three main datasets:
- `books.csv`: Contains information about books such as ISBN, title, author, etc.
- `ratings.csv`: Includes user ratings for books.
- `users.csv`: Contains user information such as location, age, etc.

## Exploratory Data Analysis (EDA)

The project includes an exploratory data analysis phase where the datasets are loaded and analyzed. Missing values are handled, and basic statistics and visualizations are generated to understand the data better.

## Data Preprocessing

Data preprocessing involves handling missing values, feature engineering, and preparing the data for model training. Steps such as imputation, encoding categorical variables, and scaling may be performed as part of this phase.

## Building Recommendation Model

The recommendation model is built using collaborative filtering algorithms, leveraging libraries such as Surprise. The model is trained on the ratings data to generate personalized book recommendations for users.

## Deployment Details

The recommendation engine is deployed using a Flask web application. Users can interact with the recommendation system through a simple web interface, where they can enter their user ID to receive personalized book recommendations.

## Getting Started

To get started with the project:
1. Clone the repository to your local machine.
2. Install the required dependencies listed in `requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Access the web interface at `http://localhost:5000` in your browser.
