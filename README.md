### Nikhil Arethiya
# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

## Dataset
- The dataset contains a collection of movies with their names and plot summaries. You can find the dataset file [Top_Movies.csv] in the repository. 
- The dataset is obtained from [Kaggle](https://www.kaggle.com/datasets/moazeldsokyx/the-500-best-movies-imdb): It has 500 rows and 10 column features


## Setup
This project is developed in Python 3.10.6 version

1. Clone this repository:
   ```bash
   git clone https://github.com/Nikhil123n/lumaa-spring-2025-ai-ml.git
   ```

2. Create a Python virtual environment:
   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:
   - **For macOS/Linux**:
     ```bash
     source env/bin/activate
     ```
   - **For Windows**:
     ```bash
     env\Scripts\Activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


## Running the Program
1. To start the recommendation system, run:
   ```bash
   python recommender.py
   ```

2. Enter a movie description when prompted to receive movie recommendations based on similarity.
   - Example Input: `A thrilling space adventure with humor`
   - Example Output: A list of top 5 movie recommendations with their similarity scores.

### Example Usage:
```bash
Welcome to the Movie Recommendation System!
Enter a movie description, or type 'exit' to quit.

Enter your movie description: A thrilling space adventure with humor

Top 5 movie recommendations:

          Movie Name                                               Plot  SimilarityScore
501          Gravity  Two astronauts work together to survive after ...         0.202062
50   La vita è bella  When an open-minded Jewish waiter and his son ...         0.178459
440     Mary Poppins  In turn of the century London, a magical nanny...         0.151315
347  Thelma & Louise  Two best friends set out on an adventure, but ...         0.144349
```

## Demo
Video Demonstration of recommender.py can be found in demo.md.


## Final Notes:
Ensure the Top_Movies.csv file exists and is structured with columns like Movie Name and Plot.
The recommendations will be based on cosine similarity, and the program will return the top N closest matches (default is 5).

## Salary Expectations
My salary expectations depend on the funding status and the size of the startup. 
Based on industry standards, I would expect a monthly salary in the range of *$3,200* to *$4,800* per month, which corresponds to an hourly rate of *$20 to $30*. I am open to further discussions depending on the responsibilities of the role.