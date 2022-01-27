from movie import Movie

MyMovie = Movie(False,60,"action","Anna Kendrick","PG",1,"Flowers")
Movie2 = Movie(True,40,"mystery","Tom Hanks","Pg-13",2,"Little Rocks")
Movie3 = Movie (False,80,"action","Tom Holland","PG",2,"Tom's Fall")


MovieList =[MyMovie,Movie2,Movie3]
print(len(MovieList))
for movie in MovieList:
  print(movie.title)

 #def __init__(self,_animated,_length,_genre,_cast,_rating,_part,_title):