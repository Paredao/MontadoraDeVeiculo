import sys
import msvcrt
import time
import random
import csv  # Módulo que fornece acesso a variáveis e funções específicas do sistema, como leitura e escrita no terminal, manipulação de argumentos de linha de comando, etc.
# PIL é a biblioteca Python Imaging Library. 'Image' é usado para abrir e manipular imagens, enquanto 'ImageTk' é usado para converter uma imagem em um formato que o Tkinter possa exibir em uma interface gráfica.
from PIL import Image, ImageTk
# Tkinter é a biblioteca padrão de interfaces gráficas do Python. 'Tk' é a classe principal para criar a janela da interface, e 'Label' é usado para exibir widgets como imagens e textos dentro da janela.
from tkinter import Tk, Label
import threading  # Importando o módulo threading para criar uma nova thread

typing_speed = 200  # palavras por minuto, serve pra manipular a velocidade do texto
# Slow type made by Vitor


def slow_type(t):
    for i, l in enumerate(t):
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            if key == chr(27):  # 'esc'
                sys.stdout.write(t[i:])
                sys.stdout.flush()
                break
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)
    print("\n")  # Para uma linha extra após a impressão do texto


pecas_finais = {}

pecas = {'Peças customizáveis': [
    'Mochila à Jato', 'Canhão de Chiclete', 'Cafeteira', 'Arador de Terra']}
campos = ['Assento', 'Farol', 'Guidão', 'Rodas',
          'Escapamento', 'Motor', 'Peças Customizáveis']

# Função para abrir a imagem em uma thread separada made by Pedro


def abririmg(imagem):
    def show_image():
        janela = Tk()
        janela.title("Transgender Motorsport")
        try:
            img = Image.open(imagem)
            img_tk = ImageTk.PhotoImage(img)
            label = Label(janela, image=img_tk)
            label.pack()
            label.image = img_tk
            janela.mainloop()
        except FileNotFoundError:
            print(f"Erro: Arquivo {imagem} não encontrado.")

    # Criando um novo thread para mostrar a imagem
    thread = threading.Thread(target=show_image)
    thread.daemon = True  # Torna o thread um daemon, para não encerrar o programa
    thread.start()

# Assento made by PH


def Assento(dicionario):
    slow_type(
        "Você está escolhendo o Assento para sua moto. Escolha uma das opções abaixo:\n")
    while True:
        # Opções para o usuário
        print("Escolha um assento, dentre as seguintes opções: \n\
1 - Assento Circunflexo \n\
2 - Cadeira de plástico da Skol (de bar) \n\
3 - Assento de Orelhão da Oi \n\
4 - Cadeira Gamer \n\
5 - Banqueta de Pastelaria \n\
6 - Puff Quadrado do Homem Aranha ")
        # Condicional com tratamento de exceção para o usuário escolher as opções fornecidas

        try:
            ass = int(input("--> "))
        except ValueError:
            print("Valor inválido, digite um número de 1 a 6")
            continue
        if ass not in [1, 2, 3, 4, 5, 6]:
            print("Opção Inválida! Escolha uma das opções acima.")
            continue
        opcoes = {
            1: 'Assento Circunflexo',
            2: 'Cadeira de plástico da Skol (de bar)',
            3: 'Assento de Orelhão da Oi',
            4: 'Cadeira Gamer',
            5: 'Banqueta de Pastelaria',
            6: 'Puff Quadrado do Homem Aranha'
        }
        dicionario['Assento'] = opcoes[ass]
        break

# Motor made by Diogo


def motor(dicionario):
    slow_type(
        "Agora, vamos escolher o Motor para sua moto. Selecione a opção desejada:\n")
    while True:
        # Oferecendo as opções ao usuário
        print(f"Escolha um motor entre as seguintes opções:\n\
1 - Motor a Combustão Futurista\n\
2 - Motor Elétrico\n\
3 - Motor Híbrido\n\
4 - Motor 2JZ-GTE Movido a Suco de Laranja")
    # Condicional com tratamento de exceção para o usuário escolher as opções fornecidas

        try:
            escolha_motor = int(input('--> '))
        except ValueError:
            print("Valor inválido, digite um número")
            continue

        if escolha_motor not in [1, 2, 3, 4]:
            print("Opção inválida! Escolha uma das opções acima.")
            continue

        opcoes = {
            1: 'Motor a Combustão Futurista',
            2: 'Motor Elétrico',
            3: 'Motor Híbrido',
            4: 'Motor 2JZ-GTE Movido a Suco de Laranja'
        }
        dicionario['Motor'] = opcoes[escolha_motor]
        break

# Peças customizaveis made by Pedro


def customizaveis(dicionario):
    slow_type(
        "Agora, vamos escolher uma peça customizável para sua moto. Escolha abaixo:\n")
    while True:
        # Oferecendo as opções ao usuário
        slow_type(f"Escolha uma peça entre as seguintes: \n")
        for i, peca in enumerate(pecas['Peças customizáveis'], 1):
            slow_type(f"{i} - {peca}")

        # Condicional com tratamento de exceções para o usuário não escolher algo fora as opções fornecidas
        try:
            peca = int(input('--> '))
        except ValueError:
            print("Valor inválido, digite um número")
            continue

        if peca not in [1, 2, 3, 4]:
            print("Opção Inválida! Escolha uma das opções acima.")
            continue

        # Armazenando a escolha no dicionário
        dicionario['Peças Customizáveis'] = pecas['Peças customizáveis'][peca - 1]
        break

# Farois made by Teteu


def farois(dicionario):
    while True:
        # Oferecendo as opções ao usuário
        slow_type(
            "\nAgora, vamos escolher o Farol para sua moto. Selecione a opção desejada:\n")
        print("Escolha um farol dentre as opções: \n\
1 - Farol de foguete \n\
2 - Farol de caminhão \n\
3 - Farol de carro \n\
4 - Farol de Alexandria")
        # Condicional com tratamento de exceção para o usuário escolher as opções fornecidas
        try:
            farou = int(input('--> '))
        except ValueError:
            print("Valor inválido, digite um número")
            continue

        if farou not in [1, 2, 3, 4]:
            print("Opção Inválida! Escolha uma das opções acima.")
            continue

        if farou == 1:
            dicionario['Farol'] = 'Farol de foguete'
        elif farou == 2:
            dicionario['Farol'] = 'Farol de caminhão'
        elif farou == 3:
            dicionario['Farol'] = 'Farol de carro'
        elif farou == 4:
            dicionario['Farol'] = 'Farol de Alexandria'
        break

# Guidão made by Teteu


def guidao(dicionario):
    while True:
        # Oferecendo as opções ao usuário
        slow_type(
            "\nAgora, vamos escolher o Guidão para sua moto. Selecione a opção desejada:\n")
        print("Escolha um Guidão entre os seguintes: \n\
1 - Guidão de bmx \n\
2 - Guidão levanta suvaco \n\
3 - Guidão padrão de bike \n\
4 - Guidão com fitilhozinho cuti cuti")
        # Condicional com tratamento de exceção para o usuário escolher as opções fornecidas
        try:
            guidau = int(input('--> '))
        except ValueError:
            print("Valor Inválido, digite um número")
            continue

        if guidau not in [1, 2, 3, 4]:
            print("Opção Inválida! Escolha uma das opções acima.")
            continue

        if guidau == 1:
            dicionario['Guidão'] = 'Guidão de bmx'
        elif guidau == 2:
            dicionario['Guidão'] = 'Guidão levanta suvaco'
        elif guidau == 3:
            dicionario['Guidão'] = 'Guidão padrão de bike'
        elif guidau == 4:
            dicionario['Guidão'] = 'Guidão com fitilhozinho cuti cuti'
        break

# Rodas made by Pedro


def rodas(dicionario):
    while True:
        # Oferecendo as opções ao usuário
        slow_type(
            "\nAgora, vamos escolher as Rodas para sua moto. Selecione a opção desejada:\n")
        print(f"Escolha uma peça entre as seguintes: \n\
1 - Roda de Caminhão\n\
2 - Roda de Avião\n\
3 - Roda de Carro\n\
4 - Roda de Moto com Neon")
        # Condicional com tratamento de exceção para o usuário escolher as opções fornecidas
        try:
            peca = int(input('--> '))
        except ValueError:
            print("Valor Inválido, digite número")
            continue

        if peca not in [1, 2, 3, 4]:
            print("Opção Inválida! Escolha uma das opções acima.")
            continue

        if peca == 1:
            dicionario['Rodas'] = 'Roda de Caminhão'
        elif peca == 2:
            dicionario['Rodas'] = 'Roda de Avião'
        elif peca == 3:
            dicionario['Rodas'] = 'Roda de Carro'
        elif peca == 4:
            dicionario['Rodas'] = 'Roda de Moto com Neon'
        break


def escapamento(dicionario):
    while True:
        print(f"Escolha um escapamento entre as seguintes opções:\n\
1 - Escapamento de Alta Performance (Som potente e rápido)\n\
2 - Escapamento Silencioso (Menos barulho, mais eficiência)\n\
3 - Escapamento Turbo (Aumenta a aceleração e potência com som único de turbo)\n\
4 - Ecapamento Esportivo Cromado (Muito usado em motos esportivas, o brilho prata dá um charme)")

        try:
            escolha_escapamento = int(input())
        except ValueError:
            print("Valor inválido, digite um número")
            continue

        if escolha_escapamento not in [1, 2, 3, 4]:
            print("Opção inválida! Escolha uma das opções acima.")
            continue

        if escolha_escapamento == 1:
            dicionario['Escapamento'] = 'Escapamento de Alta Performance'
        elif escolha_escapamento == 2:
            dicionario['Escapamento'] = 'Escapamento Silencioso'
        elif escolha_escapamento == 3:
            dicionario['Escapamento'] = 'Escapamento Turbo'
        elif escolha_escapamento == 4:
            dicionario['Escapamento'] = 'Escapamento Esportivo Cromado'

# Função do CSV que armazena tudo made by Pedro


def escrevercsv(arquivo, pecas, campos):
    with open(arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.DictWriter(csvfile, fieldnames=campos)
        escritor.writeheader()
        escritor.writerow(pecas)
    print(f"Arquivo '{arquivo}' foi salvo com sucesso!")


# Funções que chamam tudo logo
# Beta Tester Vitor
abririmg('transgender.png')  # Abre a imagem
Assento(pecas_finais)
farois(pecas_finais)
guidao(pecas_finais)
rodas(pecas_finais)
escapamento(pecas_finais)
motor(pecas_finais)
customizaveis(pecas_finais)
