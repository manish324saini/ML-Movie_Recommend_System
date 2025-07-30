
# 🎬 Movie Recommender System using Machine Learning

A simple and effective content-based movie recommender system built with Python, Machine Learning, and Streamlit. This app suggests similar movies based on your selection using metadata like genre, cast, director, and more.

---

## 🔍 Features

- ✅ Recommend movies similar to a selected title
- 🎭 Uses metadata such as genres, cast, crew, and keywords
- 🤖 Built using NLP and cosine similarity
- 🎨 Fetches movie posters using TMDb API
- ⚡ Interactive and fast web UI using Streamlit

---

## 🚀 Demo

👉 [Live App on Streamlit Cloud](https://ml-movierecommendsystem-fzdsjkduhr7agsjzy2sote.streamlit.app/)  


---

## 📂 Dataset

- TMDb 5000 Movies Dataset (from Kaggle)
- Contains metadata like:
  - Title
  - Overview
  - Cast & Crew
  - Genres
  - Keywords

---

## 🧠 How It Works

1. **Data Cleaning & Preprocessing**  
   Merged relevant features into a combined string for each movie.

2. **Text Vectorization**  
   Used `CountVectorizer` to convert text to a bag-of-words matrix.

3. **Similarity Score**  
   Computed cosine similarity between movies based on their metadata.

4. **Poster Fetching**  
   Integrated TMDb API to get high-quality poster images dynamically.

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Requests
- Streamlit
- TMDb API

---

## 🖼️ Screenshots

![App Screenshot](screenshot.png)

