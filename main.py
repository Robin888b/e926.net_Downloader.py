query = "chunie"
pages = 99
file_name = "chunie "
folder_name = "chunie art"
user = "ravenspart"
use_multiple_folder = True
#  Code, nothing to change
import requests; import shutil;import os
if os.path.exists(str(os.getcwd() + "/"+ folder_name)) == False: os.mkdir(str(os.getcwd() + "/"+ folder_name))
folder = os.getcwd() + "/"+ folder_name
if use_multiple_folder == True:
    if os.path.exists(str(str(folder +"/rating_s"))) == False: os.mkdir(str(folder +"/rating_s"))
    if os.path.exists(str(str(folder +"/rating_q"))) == False: os.mkdir(str(folder +"/rating_q"))
    if os.path.exists(str(str(folder +"/rating_e"))) == False: os.mkdir(str(folder +"/rating_e"))
url = "https://e621.net/posts.json?tags=" + query; headers = {'User-Agent': 'e621_downloader.py','From': user }; e = 1
while not e > pages:
    finalUrl = url + "&page=" + str(e)
    print("\n\nPage N°"+str(e)+"\n")
    result = requests.get( finalUrl, headers=headers )
    if result.ok:
        result = result.json()["posts"]
        for i in result:
            if i["file"]["url"]:
                a= ""
                if use_multiple_folder == True : file = folder + "/rating_" + str(i["rating"]) + "/" + file_name + str(i["id"]) +"."+str(i["file"]["ext"])
                else : file = folder + "/" + file_name + str(i["id"]) +"."+str(i["file"]["ext"])
                res = requests.get(i["file"]["url"], stream = True)
                if res.status_code == 200:
                    with open(file,'wb') as f:
                        shutil.copyfileobj(res.raw, f)
                    print('Image sucessfully Downloaded: ',file)
                else: {print('Image Couldn\'t be retrieved')}
    else :print(result)
    e+=1
