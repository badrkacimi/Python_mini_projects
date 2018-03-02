import time
import webbrowser

number_of_breaks=3
break_counter=0
print(" Program start at "+time.ctime())
while(break_counter<number_of_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=YYf3zrwe3CA")
    break_counter+=1

