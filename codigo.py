import pyautogui
import time 

pyautogui.PAUSE = 1

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=448, y=374)

pyautogui.write("Teste@gmail.com")

pyautogui.press("tab")

pyautogui.write("minhasenha")

pyautogui.press ("tab")

pyautogui.press("enter")

import pandas

tabelaprodutos = pandas.read_csv("produtos.csv")

print(tabelaprodutos)
#codigo,marca,tipo,categoria,preco_unitario,custo,obs
for linha in tabelaprodutos.index:
    pyautogui.click(x=508, y=264)

    codigo = tabelaprodutos.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabelaprodutos.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabelaprodutos.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabelaprodutos.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabelaprodutos.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabelaprodutos.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = str(tabelaprodutos.loc[linha, "obs"])
    if obs != "nan":        
        pyautogui.write(str(obs))

    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(10000)


