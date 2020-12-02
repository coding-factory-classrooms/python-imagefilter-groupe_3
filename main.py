import grayscale as gs
import philtre
import os
import flou
import sys

args = sys.argv

try:
    print(args)
    if args[1] == "--filters":
        if type(args[2]) == str:
            filter_ls = args[2]
            filter_ls = filter_ls.split("|")
            print(filter_ls)
            for n in filter_ls:
                effect_ls = n.split(":")
                print(effect_ls)
                filter = {"filter_type": effect_ls[0], "filter_value": effect_ls[1]}
                
                print(filter)

    elif args[1]=="-h":
        print("Voici les différentes commandes :")
except IndexError :
    print("erreur d'index : arguments manquant. Tappez \"-h\" pour de l'aide")