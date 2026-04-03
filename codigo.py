import pyautogui
import time
import pandas

pyautogui.PAUSE = 2.0
pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press("enter")
pyautogui.press("enter")

time.sleep(5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

pyautogui.click(x=683, y=385)
pyautogui.write("Mahcarvalho3009@gmail.com")
pyautogui.press("tab")
pyautogui.write("32558732")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.click(x=673, y=255)



tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):    
        pyautogui.write(str(obs))
        pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(1000)
    pyautogui.click(x=673, y=255)