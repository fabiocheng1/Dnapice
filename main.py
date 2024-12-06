
from random import *
import time
import os
from colors import *
from Bio import SeqIO


# nome_arquivo = input("Digite o nome do arquivo:")

#                            nome do arquivo   tipo de arquivo





codigos_geneticos = {
    "1": "sequence.fasta" ,
    "2": "sequence2.fasta" ,
    "3": "sequence3.fasta" 

}

nomes = {

    "1": "arenarius ratus" ,
    "2": "mycoplasm pneumonia" ,
    "3": "mycoplasma genitalium" 

}




def sequencia_real():
    print(nomes)
    
    while True:
        try:
            x = input("Escolha o número do especime: ")
            break
        except ValueError:
            print("Valor inválido!")
    
    for sequencia in SeqIO.parse(codigos_geneticos[x],"fasta"):
        a = 0
        t = 0
        c = 0
        g = 0
        
        total_bases = 0

        fita1 = sequencia.seq
        fita2 = fita1.complement()

        print(nomes[x])
        
        for i in range(len(fita1)):
            
            print(f"{cores['vermelho']}|{fita1[i]}{cores['branco']} ---{cores['verde']} {fita2[i]}|")
            if fita1[i] == "A":
                a += 1
                t += 1
            elif fita1[i] == "T":
                t += 1
                a += 1
            elif fita1[i] == "C":
                c += 1
                g += 1
            elif fita1[i] == "G":
                g += 1
                c += 1
                
            total_bases += 2
            
            if total_bases > 0:
                perc_a = (a / total_bases) * 100
                perc_t = (t / total_bases) * 100
                perc_c = (c / total_bases) * 100
                perc_g = (g / total_bases) * 100
            else:
                perc_a = perc_t = perc_c = perc_g = 0

    # Exibe as porcentagen
        print(f"|{cores['vermelho']}Porcentagem A: {perc_a:.2f}% | Porcentagem T: {perc_t:.2f}% | Porcentagem C: {perc_c:.2f}% | Porcentagem G: {perc_g:.2f}%{cores['restaura']}")

def sequencia_aleatoria(tamanho):
    a = 0
    t = 0
    c = 0
    g = 0
      
    total_bases = 0
      
    for ciclo in range(tamanho):
        base = choice(list(bases.keys()))
        if base == "A":
            a += 1
            t += 1
        elif base == "T":
            t += 1
            a += 1
        elif base == "C":
            c += 1
            g += 1
        elif base == "G":
            g += 1
            c += 1
        
        # Incrementa o total de bases
        total_bases += 2
        
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
            

bases = {"A":"T" , "T": "A" , "C":"G" , "G":"C"}



print('''
      BEM VINDO
      
      ''')
                
    
while True:
    try:
        pergunta = input("1- Gerar fita aleatória\n2- Gerar fita existente")
        break
    except ValueError:
        print("Valor inválido!")


if pergunta == "1":
    while True:
        try:
            tamanho = int(input(f"{cores['azul']} Digite o tamanho da bactéria: {cores['restaura']}"))  # Solicita o tamanho da bactéria
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
                sequencia_aleatoria(tamanho)
            elif resp == 2:
                continuar = 0
                while continuar != 3:
                    fita = int(input(f"{cores["amarelo"]}Quantas fitas? {cores["verde"]}"))
                    if fita > tamanho:
                        print("Erro! Número de fitas maior que o informado")
                        time.sleep(2)
                        os.system('cls')
                    elif fita <= tamanho:
                        sequencia_aleatoria(fita)
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



    


elif pergunta == "2":
    sequencia_real()
    



