# import time
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
#
# def fetch_poster(movie_id):
#     url="https://api.themoviedb.org/3/movie/{}?api_key=133412970f6734a435bc3b45db5f2503".format(movie_id)
#     # response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=133412970f6734a435bc3b45db5f2503'.format(movie_id))
#     data=requests.get(url)
#     data=data.json()
#     poster_path=data['poster_path']
#     full_path="https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
#     # return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#         time.sleep(10)
#
#     return recommended_movie_names, recommended_movie_posters
#     # index = movies[movies['title'] == movie].index[0]
#     #
#     # # distances = similarity[index]
#     # # movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:10]
#     #
#     # recommended_movies=[]
#     # recommended_movies_posters=[]
#     # for i in movies_list:
#     #     movie_id=i[0]
#     #
#     #     recommended_movies.append(movies.iloc[i[0]].title)
#     #     # fetch poster from API
#     #     recommended_movies_posters.append(fetch_poster(movie_id))
#     #     fetch_poster(i[0])
#     # return recommended_movies,recommended_movies_posters
#
# st.header('Movie Recommendations')
# movies=pickle.load(open('movie_list.pkl', 'rb'))
#
# similarity=pickle.load(open('similarity.pkl', 'rb'))
# movie_list=movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )
#
# # st.title('Get Your Recommendations')
# #
# # selected_movie_name=st.selectbox('Select Movie Name',movies['title'].values)
#
# if st.button('Show Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
#
#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])
import pickle
import streamlit as st
import requests
import time

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=133412970f6734a435bc3b45db5f2503&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        time.sleep(1)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies=pickle.load(open('movie_list.pkl', 'rb'))
#
similarity=pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    # with col6:
    #     st.text(recommended_movie_names[5])
    #     st.image(recommended_movie_posters[5])
    # with col7:
    #     st.text(recommended_movie_names[6])
    #     st.image(recommended_movie_posters[6])
    # with col8:
    #     st.text(recommended_movie_names[7])
    #     st.image(recommended_movie_posters[7])
    # with col9:
    #     st.text(recommended_movie_names[8])
    #     st.image(recommended_movie_posters[8])
    #


# import requests
# from requests.exceptions import ConnectionError
# import time

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=YOUR_API_KEY"
#     num_retries = 3
#     retry_delay = 1 # seconds

#     for i in range(num_retries):
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#             data = response.json()
#             poster_path = [item['file_path'] for item in data['posters'] if item['file_path'] is not None][0]
#             poster_url = "https://image.tmdb.org/t/p/w500{poster_path}"
#             return poster_url
#         except ConnectionError as e:
#             print("Error fetching movie poster (attempt {i+1}/{num_retries}): {e}")
#             if i < num_retries - 1:
#                 print("Retrying in {retry_delay} seconds...")
#                 time.sleep(retry_delay)

#     print("Failed to fetch movie poster after multiple attempts.")
#     return None

# # data = requests.get(url, timeout=10)  # Timeout set to 10 seconds