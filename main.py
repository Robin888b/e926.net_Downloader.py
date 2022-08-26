# info à compléter
query = "wolf gay rating:e score:>800"    # Recherche dont les résultats seront télécharcés
pages = 99                             # Nombre de pages de téléchargés
file_name = "gay wolf yiff"        # Nom de l'image
folder = "./download"          # Chemin d'accès du dossier ou tout vas être mis
user = "username"         # vottre pseudo e621, un lien vers vottre profil ou vottre email


import requests; import shutil
url = "https://e621.net/posts.json?tags=" + query; headers = {'User-Agent': 'e621_downloader.py','From': user }; file_name = folder + "/" + file_name + " - post "; e = 1
while not e > pages:
    finalUrl = url + "&page=" + str(e)
    print("\n\nPage N°"+str(e)+"\n")
    result = requests.get( finalUrl, headers=headers )
    if result.ok:
        result = result.json()["posts"]
        for i in result:
            if i["file"]["url"]:
                a= ""
                file = file_name + str(i["id"]) +"."+str(i["file"]["ext"])
                res = requests.get(i["file"]["url"], stream = True)
                if res.status_code == 200:            
                    with open(file,'wb') as f:
                        shutil.copyfileobj(res.raw, f)
                    print('Image sucessfully Downloaded: ',file)
                else: {print('Image Couldn\'t be retrieved')}
    else :print(result)
    e+=1
