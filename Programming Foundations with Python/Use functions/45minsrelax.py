import time
import webbrowser

tiempo=(60*45)
repeticiones=3
contador=0

while contador<repeticiones:
    time.sleep(tiempo)
    webbrowser.open("https://www.youtube.com/watch?v=3YxaaGgTQYM")
    contador=contador+1