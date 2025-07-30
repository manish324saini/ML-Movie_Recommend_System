import requests
import streamlit as st
import pandas as pd
import pickle
import time
import os
import requests
import gdown
from dotenv import load_dotenv

load_dotenv()
# Replace with your actual file ID from Google Drive
file_id = os.getenv("FILE_ID")
api_key = os.getenv("API_KEY")
url = f"https://drive.google.com/uc?id={file_id}"
local_filename = "similarity1.pkl"

# Remove corrupted file
if os.path.exists(local_filename):
    os.remove(local_filename)

# Re-download using gdown
gdown.download(url, local_filename, quiet=False)
print("File size:", os.path.getsize(local_filename), "bytes")
# Safely load the pickle file
try:
    similarity = pd.read_pickle(local_filename)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Failed to load model: {e}")
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch poster for movie_id {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    index = movies_df[movies_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommened_movies = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        #time.sleep(2.0)
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommened_movies.append(movies_df.iloc[i[0]].title)
    return recommened_movies, recommended_movie_posters

st.title('Top 10 Movies Recommender Model')

# Load into pandas
movies_df = pd.read_pickle("movies.pkl")



selected_Movie_option = st.selectbox(
    "How would you like to be contacted?",
    (movies_df['title'].values.tolist()),
)

st.write("You selected:", selected_Movie_option)

st.write("Discover similar movies — click the button below!", selected_Movie_option)

if st.button("Go for Recommendation"):
    recommended_movie_names,recommended_movie_posters = recommend(selected_Movie_option)
    cols = st.columns(len(recommended_movie_names))
    for i in range(len(recommended_movie_names)):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])



