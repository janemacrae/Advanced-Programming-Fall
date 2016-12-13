import webbrowser
import fresh_tomatoes
import media

hangover=media.Movie("The Hangover","Some guys just can't handle Vegas", "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg", "https://www.youtube.com/watch?v=tcdUhdOlz9M", "*****")
oceans=media.Movie("Ocean's Eleven", "Place your bets", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY0Mzg4MzgwN15BMl5BanBnXkFtZTgwNDk0MzkxMDE@._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=imm6OR605UI", "****")
love=media.Movie("Love Actually", "The ultimate romantic comedy", "https://upload.wikimedia.org/wikipedia/en/e/eb/Love_Actually_movie.jpg", "https://www.youtube.com/watch?v=KdzH6a-XEGM", "****")

movies=[hangover, oceans, love]

fresh_tomatoes.open_movies_page(movies)
