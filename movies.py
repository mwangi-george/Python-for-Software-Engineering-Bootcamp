from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Movie(BaseModel):
    title: str = Field(
        title="Movie title",
        description="This is the title of the movie"
    )
    release_year: int
    genre: str = Field(max_length=20)
    director: Optional[str]
    duration_min: int
    rating: float
    created_at: str = Field(
        description="This is the date when the movie was created"
    )

    class Config:
        str_max_length = 50
        str_min_length = 4


class MultipleMoviesResponse(BaseModel):
    movies: list[Movie]


all_movies = {
    0: {
        "title": "My journey in Software Engineering",
        "release_year": 2024,
        "genre": "Sci-Fi",
        "director": "George Mwangi",
        "duration_min": 120,
        "rating": 4.6,
        "created_at": "2024-06-30"
    }
}


def new_movie(movie_details: Movie) -> None:

    new_movie_id = len(all_movies)

    all_movies[new_movie_id] = {
        "title": movie_details.title,
        "release_year": movie_details.release_year,
        "genre": movie_details.genre,
        "director": movie_details.director,
        "duration_min": movie_details.duration_min,
        "rating": movie_details.rating,
        "created_at": movie_details.created_at
    }
    return None


def get_movie(movie_id: int = 0) -> Movie:
    movie = all_movies[movie_id]
    return Movie(**movie)


def get_multiple_movies_paginated(start: int = 0, limit: int = 20):

    list_of_movies = []
    movie_dict_keys = list(all_movies.keys())

    for index in range(0, len(movie_dict_keys), 1):
        if index < start:
            continue
        current_key = movie_dict_keys[index]
        movie = get_movie(current_key)
        list_of_movies.append(movie)
        if len(list_of_movies) >= limit:
            break
    return list_of_movies


@app.post("/movies")
def create_movie(movie_details: Movie) -> None:
    """Endpoing to create a new movie"""
    new_movie(movie_details)
    return None


@app.get("/movie/{movie_id}", response_model=Movie)
def get_movie_by_id(movie_id: int) -> Movie:
    """Endpoint to get movie details by id"""
    return get_movie(movie_id=movie_id)


# Get multiple movies details (query parameters)
@app.get("/movies", response_model=MultipleMoviesResponse)
def get_multiple_movies(start: int = 0, limit: int = 10) -> MultipleMoviesResponse:
    movies = get_multiple_movies_paginated(start, limit)
    formatted_movies = MultipleMoviesResponse(movies=movies)
    return formatted_movies
