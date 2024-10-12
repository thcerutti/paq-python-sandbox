from Models.db import get_client, get_collection

DB_NAME = "sample_mflix"
COLLECTION_NAME = "movies"

def get_movies(year, limit):
  client = get_client()
  movie_collection = get_collection(client, DB_NAME, COLLECTION_NAME)
  all_movies = []
  for movie in movie_collection.find({
    "year": year,
  }).limit(limit):
    all_movies.append({
      "title": movie.get("title", ""),
      "year": movie.get("year", ""),
      "plot": movie.get("plot", ""),
      "cast": movie.get("cast", ""),
      "directors": movie.get("directors", ""),
      "genres": movie.get("genres", ""),
      "runtime": movie.get("runtime", ""),
      "imdb": movie.get("imdb", ""),
      "awards": movie.get("awards", ""),
      "type": movie.get("type", "")
    })
  return all_movies
