### AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

## Dataset
- The dataset contains a collection of movies with their names and plot summaries. You can find the dataset file [Top_Movies.csv] in the repository. 
- The dataset is obtained from [Kaggle](https://www.kaggle.com/datasets/moazeldsokyx/the-500-best-movies-imdb): It has 500 rows and 10 column features


## Setup
This project is developed in Python 3.10.6 version
1. Clone this repository.
2. Create a Python virtual environment:
python -m venv env source env/bin/activate 

# For macOS/Linux env\Scripts\activate 
# For Windows

3. Install dependencies:
pip install -r requirements.txt

## Running the Program
1. Run the recommendation system:
python recommender.py

2. Enter a movie description to receive movie recommendations.
## Example Usage:
- Input: `A thrilling space adventure with humor`
- Output: A list of top 5 movie recommendations with their similarity scores.

## Demo
- 

## License
This project is licensed under the MIT License.

Final Notes:
Ensure the Top_Movies.csv file exists and is structured with columns like Movie Name and Plot.
The recommendations will be based on cosine similarity, and the program will return the top N closest matches (default is 5).