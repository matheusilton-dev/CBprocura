import requests
from string import ascii_letters,digits
from random import choice

caracteres = ascii_letters[:26] + digits
with open("links_encontrados.txt","w") as links:
    pass

formato = input("escolha os formatos a serem procurados separados por virgula.\nescolha: ").split(",")
if formato == [""]:
    formato = ["pdf","doc","docx","jpg","png","gif","webp","mp3","wav","mp4","avi","txt","zip","rar"]

def procura(string,formato):
     link_testado = requests.get(f"https://files.catbox.moe/{string}.{formato}")
     print(f"testando {string}.{formato}")
     if link_testado.status_code == 200:
        print(f"LINK ENCONTRADO!!!{string}.{formato}")
        with open("links_encontrados.txt","a") as links:
            links.write(link_testado.url + "\n")

while True:
    string = ""
    for x in range(6):
        string += choice(caracteres)

    for x in formato:
         procura(string,x)