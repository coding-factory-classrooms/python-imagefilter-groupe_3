import grayscale as gs
import sys

args = sys.argv

try:
    first_arg = args[1]
    src = args[2]
    if first_arg == "grayscale" :
        gs.grayscayle(src)
    else:
        print("Mauvaise sasie de commande")
except IndexError :
    print("erreur d'index : ")