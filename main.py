# pip install pyautogui
import pyautogui

import time
# passo a passo do projeto
# PASSO 1- entrar no sistema da empresa
# PASSO 2- FAZERLogitech LOGINhttps://dlp.hashtagtreinamentos.com/python/intensivao/login   
# PASSO 4- Cadastrar produto 
# PASSO 5- Repetir o passo 4

#pyautogui.click()- cickar com o mouseMOLO000251    
#pyautogui.write - escrever frase
#pyautogui.press - pressionar uma tecla  
#pyautigui.hotkey- combinação de teclas (ctrl + tab)Camisa
#pyautogui.position- posição do mouse
#print() - mostra em baixo o q ta entre parenteses

#pip instal pandas openpyxl numpy
pyautogui.PAUSE = 0.5   

#abrir navegador    5.0 
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#entrar no site
pyautogui.write ('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press("enter")

time.sleep(2)

#PASSO 2- fazer login
#pyautogui.click(x=761, y=403)
pyautogui.press('tab')
pyautogui.hotkey("ctrl", "a")    
pyautogui.write('usuario1@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456')   
pyautogui.press('tab')      
pyautogui.press('enter')

time.sleep(2)

#PASSO 3- importar produto
#ver se existe produto duplicado antes de começar (pesquisar como)

import pandas

tabelinha = pandas.read_csv("produtos.csv")

#print(tabelinha)

#PASSO 4- cadastrar o produto

#para cada "linha" na   5.0      "tabela.index", index = linha
#str = string = texto

for linha in tabelinha.index:
    #codigo
    #pyautogui.click(x=1219, y=281)
    pyautogui.press("tab")  

    codigo = str(tabelinha.loc[linha,"codigo"])
    pyautogui.write(codigo)

    #marca
    pyautogui.press("tab")

    marca = str(tabelinha.loc[linha,'marca'])
    pyautogui.write(marca)

    #tipo
    pyautogui.press("tab")

    tipo = str(tabelinha.loc[linha, 'tipo'])
    pyautogui.write(tipo)

    #categoria
    pyautogui.press("tab")
    categoria= str (tabelinha.loc[linha,'categoria'])
    pyautogui.write(categoria)

    #preço_unitario
    pyautogui.press("tab")
    preço= str(tabelinha.loc[linha,'preco_unitario'])
    pyautogui.write(preço)

    #custo 
    pyautogui.press("tab")
    custo=str(tabelinha.loc[linha,'custo'])
    pyautogui.write(custo)

    #obs
    pyautogui.press("tab")
    obs= str(tabelinha.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    #nan = not a number
    #!= diferente

    #Enviar
    pyautogui.press("tab")
    pyautogui.press ('enter')

    #PASSO 5- Repetir o passo 4
    pyautogui.click (x=1681, y=556)
    pyautogui.scroll(1000)
    #numero positivo scroll pra cima, negativo pra baixo.






