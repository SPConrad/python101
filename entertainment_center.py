import media
import fresh_tomatoes

# This file contains prepared sample movies for the movie array,
# populates the array, and opens the movie page.

toy_story = media.Movie("Toy Story", "Toys do stuff", "https://upload.wikime" +
                        "dia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px" +
                        "-Toy_Story.jpg", "https://www.youtube.com/watch?v=" +
                        "KYz2wyBy3kc")

avatar = media.Movie("Avatar", "Aliens and stuff", "https://upload.wikimedia" +
                     ".org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/" +
                     "220px-Avatar-Teaser-Poster.jpg", "https://www.youtube." +
                     "com/watch?v=cRdxXPV9GNQ")

serenity = media.Movie("Serenity", "They aim to misbehave", "https://upload." +
                       "wikimedia.org/wikipedia/en/thumb/9/9e/Serenity_One_S" +
                       "heet.jpg/215px-Serenity_One_Sheet.jpg", "https://ww" +
                       "w.youtube.com/watch?v=6nEAlpTb4tk")

avengers = media.Movie("Avengers", "They assemble", "https://upload.wikimedi" +
                       "a.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster." +
                       "jpg/220px-TheAvengers2012Poster.jpg", "https://www." +
                       "youtube.com/watch?v=eOrNdBpGMv8")

skyfall = media.Movie("Skyfall", "Bond wins, but also loses", "https://uploa" +
                      "d.wikimedia.org/wikipedia/en/thumb/a/a7/Skyfall_poste" +
                      "r.jpg/220px-Skyfall_poster.jpg", "https://www.youtub" +
                      "e.com/watch?v=6kw1UVovByw")

the_martian = media.Movie("The Martian", "Matt Damon gets stranded AGAIN", +
                          "https://upload.wikimedia.org/wikipedia/en/thumb/c" +
                          "/cd/The_Martian_film_poster.jpg/220px-The_Martia" +
                          "n_film_poster.jpg", "https://www.youtube.com/wat" +
                          "ch?v=ej3ioOneTy8")

movies = [toy_story, avatar, serenity, avengers, skyfall, the_martian]

fresh_tomatoes.open_movies_page(movies)
