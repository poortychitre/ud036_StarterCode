import media            # import package media to use class movie
import fresh_tomatoes   # import package fresh_tomatoes

print(media.Movie.__doc__)

# Create instances of class movie
hunger_games = media.Movie("Hunger Games", \
                           "http://www.thehungergames.movie/assets/images/fi" \
                           "lms/hg/posters/thg_teaser_poster.jpg", \
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

star_wars = media.Movie("Star Wars: The Last Jedi", \
                        "https://upload.wikimedia.org/wikipedia/en/thumb/7/7" \
                        "f/Star_Wars_The_Last_Jedi.jpg/220px-Star_Wars_The_" \
                        "Last_Jedi.jpg", \
                        "https://www.youtube.com/watch?v=zB4I68XVPzQ")

lord_of_the_rings = media.Movie("The Lord of the Rings: The" \
                                "Fellowship of the Ring", "https://upload." \
                                "wikimedia.org/wi"
                                "kipedia/en/9/9d/The_Lord_of_the_Rings_The_" \
                                "Fellowship_of_the_Ring_%282001%29_" \
                                "theatrical_poster" \
                                ".jpg", \
                                "https://www.youtube.com/watch?v=V75dMMIW2B4")

notebook = media.Movie("The Notebook", \
                       "https://upload.wikimedia.org/wikipedia" \
                       "/en/8/86/Posternotebook.jpg", \
                       "https://www.youtube.com/watch?v=4M7LIcH8C9U")

sherlock_homes = media.Movie("Sherlock Homes", \
                             "https://upload.wikimedia.org/wikipedia" \
                             "/en/e/e0/Sherlock_holmes_ver5.jpg", \
                             "https://www.youtube.com/watch?v=J7nJksXDBWc")

martian = media.Movie("The Martian", \
                      "https://upload.wikimedia.org/wikipedia" \
                      "/en/c/cd/The_Martian_film_poster.jpg", \
                      "https://www.youtube.com/watch?v=ej3ioOneTy8")

jungle_book = media.Movie("The Jungle Book", \
                          "https://upload.wikimedia.org/wikipedia" \
                          "/en/a/a4/The_Jungle_Book_%282016%29.jpg", \
                          "https://www.youtube.com/watch?v=5mkm22yO-bs")

finding_nemo = media.Movie("Finding Nemo", \
                           "https://upload.wikimedia.org/wikipedia" \
                           "/en/2/29/Finding_Nemo.jpg", \
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

toy_story = media.Movie("Toy Story", \
                        "https://upload.wikimedia.org/wikipedia" \
                        "/en/1/13/Toy_Story.jpg", \
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Grouping the above movie class instances into a list called movies
movies = [hunger_games, star_wars, lord_of_the_rings, \
          notebook, sherlock_homes, martian, jungle_book, \
          finding_nemo, toy_story]

# call the open_movies_page function to generate an HTML page
fresh_tomatoes.open_movies_page(movies)

