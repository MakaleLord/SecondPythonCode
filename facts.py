<style>
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono');
html{
   display:flex;
   justify-content:center;
   align-items: center;
   width: 100%;
   height: 100%;
   background-image: url('https://source.unsplash.com/collection/327760/1600x900');
   background-size:cover;
}

body{
   min-width:55%;
   max-width:100%;
   height:60vh;
   border:1px solid lightgray;
   background-color:white;
   border-radius:8px;
   font-family: 'Roboto Mono', monospace;
   box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
   border-top:32px solid #eee;
   overflow-y:scroll;
}

body > div{
  height: calc(100% - 40px);
  overflow-y:auto;
  padding: 20px;
  white-space: pre;
}
</style>

#!/usr/bin/python3

print("Content-type:text/html \n")
import magicwand

celebrity_name = "Chris Hemsworth"
birth_year = 1983
total_movies = 34
first_movie = "Star Trek"
rating = 6.9
print(F"""
Celebrity facts about {celebrity_name}
- {celebrity_name} was born in {birth_year}
- {celebrity_name} has done a total of {total_movies} movies.                
- {celebrity_name} first movie was {first_movie}.
- {celebrity_name} has a rating of {rating}
""")
