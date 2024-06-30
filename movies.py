from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Movie(BaseModel):
    title: str = Field(
        title="Movie title",
        description="This is the title of the movie",
        max_length=50,
        min_length=1
    )
    release_year: int
    genre: str = Field(max_length=20)
    director: Optional[str]
    duration_min: int
    rating: float
    created_at: str = Field(
        description="This is the date when the movie was created",
        max_length=20,
        min_length=4
    )


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


def get_movie(movie_id: int = 0) -> Movie:
    movie = all_movies[movie_id]
    return Movie(**movie)

# Get Movie details by id


@app.get("/movie/{movie_id}", response_model=Movie)
def get_movie_by_id(movie_id: int) -> dict:
    """Endpoint to get movie details by id"""
    return get_movie(movie_id=movie_id)


# Get multiple movies details (query parameters)
