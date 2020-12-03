import filter_selection
import os
import sys
import writing

args = sys.argv
new_directory="output"
list_filtre=[]

#étape 1: initialiser ma config à partir de la CLI
try:
    print(args)
    if args[1] == "--filters":
        if type(args[2]) == str:
            filter_ls = args[2]
            filter_ls = filter_ls.split("|")
            for n in filter_ls:
                effect_ls = n.split(":")
                if len(effect_ls)>1 :
                    filter = {"filter_type": effect_ls[0], "filter_value": effect_ls[1]}
                    list_filtre.append(filter)
                    if filter["filter_type"] == "dilate":
                        print("filtre dilate")

                    elif filter["filter_type"] == "blur":
                        print("filtre blur")
                else:
                    filter = {"filter_type": effect_ls[0]}
                    list_filtre.append(filter)
                    if filter["filter_type"] == "grayscale":
                        print("filtre grayscale")


    elif args[1]=="-h":
        print("Voici les différentes commandes :")
except IndexError :
    print("erreur d'index : arguments manquant. Tappez \"-h\" pour de l'aide")

#étape 2: exécuter mon programme à partir de la config
path = "imgs"
dirs = os.listdir(path)
for file in dirs:
    print(file)
    for filter_dict in list_filtre:
        print(len(filter_dict))
        if len(filter_dict)>1:
            filter_selection.filter_application(filter_dict["filter_type"], int(filter_dict["filter_value"]), f"{path}/{file}", file)
        else :
            filter_selection.filter_application(filter_dict["filter_type"], 0,
                                                f"{path}/{file}", file)
        writing.write_file(new_directory, file, )

print(list_filtre)