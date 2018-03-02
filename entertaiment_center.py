import media
import fresh_tomatoes

toy_story=media.Movie("Toy story 3",
                      "A toy come to life",
                      "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-wt2it4_fbf729c8.jpeg?region=0,0,300,450",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar=media.Movie("Avatar",
                      "A marine on an alien planet",
                      "http://cima4up.tv/wp-content/uploads/2017/03/Avatar-2009.jpeg",
                      "https://www.youtube.com/watch?v=uZNHIU3uHT4")

lucifer=media.Movie("Lucifer",
                      "the original fallen angel",
                      "https://www.hypable.com/wp-content/uploads/2016/08/lucifer-poster-season-2.jpg",
                      "https://www.youtube.com/watch?v=X4bF_quwNtw")

shape_of_voice=media.Movie("The Shape of Voice",
                      " A young man is ostracized by his classmates after he bullies a deaf girl to the point where she moves away",
                      "http://www.cinema.com.my/images/movies/2017/7silentvoice00_450.jpg",
                      "https://www.youtube.com/watch?v=Ivrq1ZwsRps")

dil_mushkil=media.Movie("Channa Mereya",
                      "Indian romantic drama film",
                      "http://www.bollywoodlife.com/wp-content/uploads/2016/09/ADHM-1.jpg",
                      "https://www.youtube.com/watch?v=Z_PODraXg4E")

rissala=media.Movie("Ar-Rissala",
                      "The history of prophet",
                      "http://islammedia.free.fr/image/affiche_film.jpg",
                      "https://www.youtube.com/watch?v=4n9ssMte-hc")
hunger_games=media.Movie("Hunger games",
                      "After being symbolized as the Mockingjay, Katniss Everdeen and District 13 engage in an all-out revolution against the autocratic Capitol",
                      "http://is3.mzstatic.com/image/thumb/Video69/v4/ce/a3/f6/cea3f6e8-8bcf-01e8-928e-fe6a39eecfe8/source/1200x630bb.jpg",
                      "https://www.youtube.com/watch?v=KmYNkasYthg")
#avatar.show_trailer()
movies=[rissala,hunger_games,dil_mushkil,shape_of_voice,lucifer,avatar,toy_story]
fresh_tomatoes.open_movies_page(movies)


