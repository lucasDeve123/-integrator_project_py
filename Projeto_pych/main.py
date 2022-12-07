import requests
from bs4 import BeautifulSoup
import pandas as pd

lista = []

r = requests.get("http://127.0.0.1:5500/produtos.html")
soup = BeautifulSoup(r.content, "html.parser")

s = soup.find('div', class_="tenis")
tituloproduto = s.find_all('h1')
for c in tituloproduto:
    lista.append(c.text)
valorp = s.find_all('b')
for c in valorp:
    lista.append(c.text)

descp = s.find_all('p')
for c in descp:
    lista.append(c.text)
listaok = {"Nome Produto": lista[0:4], "Preço Produto": lista[4:8], "Descrição Produto": lista[8:12]}
listalegal = pd.DataFrame(listaok)
listalegal.to_excel("ProjetoIntegrador-Lucas.xls")
