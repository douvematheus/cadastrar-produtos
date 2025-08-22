# PASSO A PASSO
# passo 1 entrar no sistema
# passo 2 fazer login
# passo 3 importar base de dados 
# passo 4 cadastrar o produto
# passo 5 repetir ate acabar a lista de produtos

#pip install pyautogui
#pip install pandas


import pyautogui
import time

# pyautogui.click - clicar com o mouse 
# pyautogui.write - escrever um texte 
# pyautogui.press - apertar 1 tecla                                      
# pyautogui.hotkey - combinação de telcas (CTRL C)
# pyautogui.scroll - descer o scroll para cima ou para baixo

pyautogui.PAUSE = 0.5

#  PASSO 1 - entrar no sistema
#  abrir o navegador 
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')

# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3) # garantir que o site vai abrir tranquilo 

# passo 2 - FAZER LOGIN NO SISTEMA
pyautogui.click(x=1208, y=395) # local que pegou a posição do mouse na tela
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('e-mail qualquer ')

pyautogui.PAUSE = 0.5

# colocar a senha 
pyautogui.press('tab')
pyautogui.write('123456')

pyautogui.click(x=1300, y=550)

time.sleep(3)

# passo 3 -  IMPORTAR A BASE DE DADOS
# pandas - trabalhar com todo tipo de base de dados + openpyxl numpy
import pandas

tabela = pandas.read_csv('produtos.csv') # ler a base de dados 

print(tabela)

# PASSO 4 CADASTRAR O PRODUTO
# para cada linha da minha tabala:
for linha in tabela.index: # tabela.index 
    # CODIGO
    pyautogui.click(x=1189, y=273) 

    codigo = str(tabela.loc[linha, "codigo"])  # string = texto
    pyautogui.write(codigo)
    
    # MARCA
    pyautogui.press("tab") 
    marca = str(tabela.loc[linha, "marca"])
    #tipo  categoria   unitario    custo   obs 
    pyautogui.write(marca)
    # TIPO
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    # CATEGORIA
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    # PRECO_UNITARIO
    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)   
    # CUSTO
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    # OBS
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": # != e diferente 
        pyautogui.write(obs)

    # clicar no botao de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(100000) # para voltar para cima e voltar a fazer o cadastro
    #pyautogui.scroll(1000) # se o numero for posito vai para cima se for negativo vai para baixo

    # PASSO 5 - REPETIR PARA TODOS OS PRODUTOS  - PARA TODAS AS LINHAS DA TABELA