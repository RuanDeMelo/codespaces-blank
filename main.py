import sys
import requests
from antlr4 import *
from TrelloLangLexer import TrelloLangLexer
from TrelloLangParser import TrelloLangParser

keys = []

def inicializar(prog): 
        keys.append(prog.children[1].getText())
        keys.append(prog.children[3].getText())
        for c in prog.comando():
            execute(c)

def execute(com):
     if com.REPITA():
        for x in range(int(com.children[1].getText())):
             execute(com.children[3])
            
     if com.CRIAR():
        
        criar(com)
     #elif com.MOVER():
          
    #elif com.MOSTRAR():
          
def criar(com):
    if com.BOARD():
        url = "https://api.trello.com/1/boards/"
        query = {
        "key": keys[0],  # Sua API Key
        "token": keys[1],  # Seu Token de Acesso
        "name": com.children[2].getText().replace('"', ''),  
        "defaultLabels": "true",  
        "defaultLists": "true",  
    }

    # Faz a requisição POST para criar o board
    response = requests.post(url, params=query)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        board = response.json()  # Converte a resposta em JSON
        print(f"Board criado com sucesso!")
        print(f"Nome do Board: {board['name']}")
        print(f"ID do Board: {board['id']}")
    else:
        print(f"Erro ao criar o board: {response.status_code}")
        print(response.text)  # Exibe a mensagem de erro da API

         
    

input_stream = InputStream(
    """KEY 957738ac823bdaf7bff6dc6bfc1b6fe0 TOKEN ATTA5340f4382b9b4bc2850d9b859906b4a7664a92f7683e5def4556d155550c080b954A89BD REPITA 1 { CRIAR BOARD "teste1" }
    """)
lexer = TrelloLangLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = TrelloLangParser(stream)
tree = parser.prog()
if parser.getNumberOfSyntaxErrors()==0:
    print("ok")
    inicializar(tree)
    print(keys)
    print(tree.toStringTree(recog=parser))
else:
    print("erro sintático")
