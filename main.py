import filter_selection
import os
import sys
import writing
import imread
import cv2

dico_img = {}
args = sys.argv
new_directory = "output"
list_filtre = []

# étape 1: initialiser ma config à partir de la CLI
try:
    print(args)
    if args[1] == "--filters":
        if type(args[2]) == str:
            filter_ls = args[2]
            filter_ls = filter_ls.split("|")
            for n in filter_ls:
                effect_ls = n.split(":")
                if len(effect_ls) > 1:
                    filter = {"filter_type": effect_ls[0], "filter_value": effect_ls[1]}
                    list_filtre.append(filter)
                    if filter["filter_type"] == "dilate":
                        print("filtre dilate")

                    elif filter["filter_type"] == "blur":
                        print("filtre blur")
                else:
                    filter = {"filter_type": effect_ls[0], "filter_value": 0}
                    list_filtre.append(filter)
                    if filter["filter_type"] == "grayscale":
                        print("filtre grayscale")


    elif args[1] == "-h":
        print("Voici les différentes commandes :")
except IndexError:
    print("erreur d'index : arguments manquant. Tappez \"-h\" pour de l'aide")

# étape 2: exécuter mon programme à partir de la config
path = "imgs"
i = 0
dirs = os.listdir(path)

for file in dirs:
    if file.find(".png") >= 0 or file.find(".jpg") >= 0 or file.find(".jpeg"):

        print(file)
        try:
            # Ouvrir image :
            dico_img[i] = imread.imread(f"{path}/{file}", file)
            print(dico_img[i])
            print(f"{path}/{file}")
            for filter_dict in list_filtre:
                # Appliquer les filtres :

                try:
                    dico_img[i] = filter_selection.filter_application(filter_dict["filter_type"],
                                                                      int(filter_dict["filter_value"]), file,
                                                                      dico_img[i])
                    print("filtre appliquer")
                except cv2.error:
                    print("erreur filtre")

        # Ecrire l'image :
        except AttributeError:
            print("oui")
        try:
            writing.write_file(new_directory, file, dico_img[i])
            i = i + 1
        except cv2.error:
            print("erreur 1")