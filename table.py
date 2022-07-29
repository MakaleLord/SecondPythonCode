
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
print("Content-type: text/html \n")
import magicwand

num = 13 

print(num, "x 1 =", num*1, "<br>")
print(num, "x 2 =", num*2, "<br>")
print(num, "x 3 =", num*3, "<br>")
print(num, "x 4 =", num*4, "<br>")
print(num, "x 5 =", num*5, "<br>")
print(num, "x 6 =", num*6, "<br>")
print(num, "x 7 =", num*7, "<br>")
print(num, "x 8 =", num*8, "<br>")
print(num, "x 9 =", num*9, "<br>")
print(num, "x 10 =", num*10, "<br>")
