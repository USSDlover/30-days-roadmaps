from movies import movies


def recommend_movie():
    genre = input("Please enter favorite genre: ")
    rating = float(input("Please enter favorite rating: "))

    filtered_movies = [movie for movie in movies if movie["genre"] == genre]
    recommended_movies = [movie for movie in filtered_movies if movie["rating"] >= rating]

    if recommended_movies:
        for i, movie in enumerate(recommended_movies, 1):
            print(f"{i}. Title: {movie['title']} \t| Genre: {movie['genre']} \t| Rating: {movie['rating']}")


recommend_movie()
