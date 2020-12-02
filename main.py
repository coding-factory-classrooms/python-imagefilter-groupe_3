import grayscale as gs
import flou
import sys

args = sys.argv

try:
    first_arg = args[1]
    src = args[2]
    if first_arg == "grayscale" :
        gs.grayscayle(src)
    elif first_arg == "flou":
        flou.blur(src)
    else:
        print("Mauvaise sasie de commande")
except IndexError :
    print("erreur d'index : ")