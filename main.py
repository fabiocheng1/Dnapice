from random import *
import time
import os
from colors import *

def sequencia(tamanho):
    a = 0
    t = 0
    c = 0
    g = 0

    # Inicialize total_bases antes do loop
    total_bases = 0

    for ciclo in range(tamanho):
        base = choice(list(bases.keys()))
        
        # Contagem de bases
        if base == "A":
            a += 1
        elif base == "T":
            t += 1
        elif base == "C":
            c += 1
        elif base == "G":
            g += 1
        
        # Incrementa o total de bases
        total_bases += 1
        
        # Exibe a base e a ligação com a cor
        ligacao = bases[base]
        print(f"|{cores['vermelho']}{base}{cores['branco']}--{cores['verde']}{ligacao}|")

    # Calcula as porcentagens de cada base
    if total_bases > 0:
        perc_a = (a / total_bases) * 100
        perc_t = (t / total_bases) * 100
        perc_c = (c / total_bases) * 100
        perc_g = (g / total_bases) * 100
    else:
        perc_a = perc_t = perc_c = perc_g = 0

    # Exibe as porcentagens
    print(f"|{cores['vermelho']}Porcentagem A: {perc_a:.2f}% | Porcentagem T: {perc_t:.2f}% | Porcentagem C: {perc_c:.2f}% | Porcentagem G: {perc_g:.2f}%{cores['restaura']}")

bases = {"A":"T" , "T": "A" , "C":"G" , "G":"C"} #Contitui as bases e as ligações correspondentes



while True:
    try:
        tamanho = int(input(f"{cores['azul']} Digite o tamanho da bactéria: {cores['restaura']}"))  # Solicita o tamanho da bactéria
        # Se a entrada for um número válido, o loop é interrompido
        break
    except ValueError:
        print("Erro!Valor inválido")
        time.sleep(2)
        os.system('cls')




while True:
    try:
        resp = int(input(f"""{cores["vermelho"]}1- Imprimir toda a sequência de DNA{cores["verde"]} / 2- Número de fitas determinado {cores["magenta"]}/ 3- Encerrar {cores["restaura"]}"""))
        break
    except ValueError:
        os.system('cls')
        
while True:

    try:
        if resp == 1:
            sequencia(tamanho)
        elif resp == 2:
            continuar = 0
            while continuar != 3:
        
        
                fita = int(input(f"{cores["amarelo"]}Quantas fitas? {cores["verde"]}"))
                if fita > tamanho:
                    print("Erro! Número de fitas maior que o informado")
                    time.sleep(2)
                    os.system('cls')
                elif fita <= tamanho:

                    sequencia(fita)
                    
                    while True:
                        try:
                            continuar = int(input(f"{cores["amarelo"]}Deseja continar? (3 Para acabar e 1 Para continuar)"))
                            break
                        except ValueError:
                            print("Erro!")
                            time.sleep(2)
                            os.system('cls')
                    time.sleep(2)
                    os.system('cls')
        break
    except ValueError:
        print("Valor inválido!")
        time.sleep(2)
        os.system('cls')



limpar = int(input(f"{cores["amarelo"]}Deseja limpar? 1-Sim 2-Não"))



if limpar == 1: 
    time.sleep(1.0)
    os.system('cls')

