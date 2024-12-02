import requests
from string import ascii_letters,digits
from random import choice

caracteres = ascii_letters[:26] + digits
with open("links_encontrados.txt","w") as links:
    pass

formato = input("escolha os formatos a serem procurados separados por virgula.\nescolha: ").split(",")

def procura(string,formato):
     link_testado = requests.get(f"https://files.catbox.moe/{string}.{formato}")
     print(f"testando {string}.{formato}")
     if link_testado.status_code == 200:
        print(f"LINK ENCONTRADO!!!{string}.{formato}")
        with open("links_encontrados.txt","a") as links:
            links.write(link_testado.url + "\n")

while True:
    a = choice(caracteres)
    b = choice(caracteres)
    c = choice(caracteres)
    d = choice(caracteres)
    e = choice(caracteres)
    f = choice(caracteres)
    string = a+b+c+d+e+f

    for x in formato:
         procura(string,x)