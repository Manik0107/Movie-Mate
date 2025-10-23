import streamlit as st
import pickle
import requests
import os

# Load movie list and similarity matrix
movies = pickle.load(open("/Users/manikmanavenddram/movie mate/Movie-Mate/movie_list.pkl", "rb"))
similarity = pickle.load(open("/Users/manikmanavenddram/movie mate/Movie-Mate/similarity.pkl", "rb"))

movie = movies['title'].values
st.header("Movie Recommendation System")
selection = st.selectbox('Select a movie from the dropdown', movie)

# Recommendation function to get similar movies
def recommendation(mov):
    rec_mov = []
    index = movies[movies['title'] == mov].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    for i in distance[1:6]:  # Get top 5 recommendations
        rec_mov.append(movies.iloc[i[0]].title)
    return rec_mov

# Function to fetch movie details including poster from OMDb API
def fetch_movie_details(movie_title):
    api_key = '8efc867d'  # Replace with your OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['Response'] == 'True':
        return {
            'title': data['Title'],
            'year': data['Year'],
            'genre': data['Genre'],
            'plot': data['Plot'],
            'poster': data['Poster'] if data['Poster'] != 'N/A' else None
        }
    else:
        return None  # In case the movie details are not found

# Add custom CSS to add spacing between columns
st.markdown(
    """
    <style>
    .movie-poster {
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display recommendations and movie details on button click
if st.button("Recommend"):
    movie_names = recommendation(selection)
    cols = st.columns(5)
    
    # Loop through each recommended movie and fetch details
    for idx, col in enumerate(cols):
        movie_name = movie_names[idx]
        movie_details = fetch_movie_details(movie_name)
        
        with col:
            if movie_details:
                if movie_details['poster']:
                    # Add custom CSS class to poster image for spacing
                    st.image(movie_details['poster'], width=150, use_column_width=True, caption=movie_details['title'])
                    st.markdown('<div class="movie-poster"></div>', unsafe_allow_html=True)  # Apply spacing
                st.caption(f"Genre: {movie_details['genre']}")
                st.caption(f"Year: {movie_details['year']}")
                st.write(movie_details['plot'])  # Display movie plot
            else:
                st.text(movie_name)  # Fallback if no details are found