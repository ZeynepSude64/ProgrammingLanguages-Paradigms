import random

# -------------------------------
# MOVIE CLASS (OOP)
# -------------------------------
class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.genre}) - Rating: {self.rating}"


# -------------------------------
# USER CLASS (OOP)
# -------------------------------
class User:
    def __init__(self):
        self.watched_movies = []

    def add_movie(self, movie):
        self.watched_movies.append(movie)

    # Weighted genre (puan bazlı analiz)
    def get_weighted_favorite_genre(self):
        if not self.watched_movies:
            return None

        genre_scores = {}
        for movie in self.watched_movies:
            genre_scores[movie.genre] = genre_scores.get(movie.genre, 0) + movie.rating

        return max(genre_scores, key=lambda g: genre_scores[g])

    # Kullanıcı istatistikleri
    def get_statistics(self):
        if not self.watched_movies:
            return None

        genre_count = {}
        for movie in self.watched_movies:
            genre_count[movie.genre] = genre_count.get(movie.genre, 0) + 1

        avg_rating = sum(map(lambda m: m.rating, self.watched_movies)) / len(self.watched_movies)

        return genre_count, avg_rating


# -------------------------------
# RECOMMENDATION ENGINE (OOP)
# -------------------------------
class RecommendationEngine:
    def __init__(self, movie_list):
        self.movie_list = movie_list

    def recommend(self, user, min_rating=0):
        favorite_genre = user.get_weighted_favorite_genre()

        if not favorite_genre:
            return []

        # İzlenen filmleri alma
        watched_titles = set(m.title.lower() for m in user.watched_movies)

        # Functional: filtreleme
        filtered = list(filter(
            lambda m: m.genre == favorite_genre
            and m.rating >= min_rating
            and m.title not in watched_titles,
            self.movie_list
        ))

        # Functional: sıralama
        sorted_movies = sorted(filtered, key=lambda m: m.rating, reverse=True)

        return sorted_movies[:3]

    # Random öneri
    def random_recommend(self, user):
        watched_titles = list(map(lambda m: m.title, user.watched_movies))

        available = list(filter(
            lambda m: m.title not in watched_titles,
            self.movie_list
        ))

        if not available:
            return None

        return random.choice(available)

    # Arama
    def search(self, keyword):
        return list(filter(
            lambda m: keyword.lower() in m.title.lower(),
            self.movie_list
        ))


# -------------------------------
# MAIN MENU (PROCEDURAL)
# -------------------------------
def main():
    movies = [
        Movie("Inception", "Sci-Fi", 9),
        Movie("Interstellar", "Sci-Fi", 10),
        Movie("The Matrix", "Sci-Fi", 9.5),
        Movie("Arrival", "Sci-Fi", 8.5),
        Movie("Titanic", "Romance", 8),
        Movie("The Notebook", "Romance", 7.5),
        Movie("John Wick", "Action", 8.7),
        Movie("Mad Max", "Action", 8.9),
    ]

    user = User()
    engine = RecommendationEngine(movies)

    while True:
        print("\n🎬 MENU")
        print("1. Add watched movie")
        print("2. Get recommendations")
        print("3. Random recommendation")
        print("4. Show statistics")
        print("5. Search movie")
        print("6. Exit")

        choice = input("Select an option: ")

        # 1. Film ekleme
        if choice == "1":
            title = input("Movie title: ")
            genre = input("Genre: ")
            rating = float(input("Your rating (0-10): "))
            user.add_movie(Movie(title, genre, rating))
            print("Movie added!")

        # 2. Öneri
        elif choice == "2":
            min_rating = float(input("Minimum rating: "))
            recs = engine.recommend(user, min_rating)

            print("\n📌 Recommendations:")
            if not recs:
                print("No recommendations found.")
            else:
                for m in recs:
                    print(m)

        # 3. Random öneri
        elif choice == "3":
            movie = engine.random_recommend(user)
            if movie:
                print("\n🎲 Random Pick:")
                print(movie)
            else:
                print("No available movies.")

        # 4. İstatistik
        elif choice == "4":
            stats = user.get_statistics()
            if not stats:
                print("No data yet.")
            else:
                genre_count, avg = stats
                print("\n📊 Statistics:")
                for g, c in genre_count.items():
                    print(f"{g}: {c} movies")
                print(f"Average rating: {round(avg, 2)}")

        # 5. Arama
        elif choice == "5":
            keyword = input("Search keyword: ")
            results = engine.search(keyword)

            print("\n🔍 Results:")
            if not results:
                print("No movies found.")
            else:
                for m in results:
                    print(m)

        # 6. Çıkış
        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


# Programı başlat
if __name__ == "__main__":
    main()
