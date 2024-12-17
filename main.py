from random import *
import time
import os
from colors import *
from Bio import SeqIO


os.system("cls")

codigos_geneticos = {
    1: "sequence.fasta" ,
    2: "sequence2.fasta" ,
    3: "sequence3.fasta" 

}

nomes = {

    1: "arenarius ratus" ,
    2: "mycoplasm pneumonia" ,
    3: "mycoplasma genitalium" 

}




def sequencia_real():
    teste = 0
    
    os.system("cls")
    print(f"""{cores["ciano"]}1- Arenarius Ratus (formiga)
2- Mycoplasm Pneumonia (bactéria da pneumonia)
3- Mycoplasm Genitalium (bactéria parasita que vive na região genital dos primatas)""")
    
    while True:
        try:
            
            x = int(input("\nEscolha o número do espécime: "))
            if x > 3 or x < 1:
                print("Erro! Valor não encontrado")
                time.sleep(2)
                os.system("cls")
            else:
                break

        except ValueError:
            print("Valor inválido!")
            time.sleep(2)
            os.system("cls")
            print(f"""{cores["ciano"]}1- Arenarius Ratus (formiga)
2- Mycoplasm Pneumonia (bactéria da pneumonia)
3- Mycoplasm Genitalium (bactéria parasita que vive na região genital dos primatas)""")
    
    
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
            
            

            if teste == 0:
                print(f"|{cores['vermelho']}{fita1[i]}{cores['branco']}-----{cores['verde']}{fita2[i]}|")
                teste += 1
            elif teste == 1:
                print(f" \{cores['vermelho']}{fita1[i]}{cores['branco']}---{cores['verde']}{fita2[i]}/")
                teste += 1
            elif teste == 2:
                print(f"  |{cores['vermelho']}{fita1[i]}{cores['branco']}-{cores['verde']}{fita2[i]}|")
                teste += 1
            elif teste == 3:
                print(f" /{cores['vermelho']}{fita1[i]}{cores['branco']}---{cores['verde']}{fita2[i]}\ ")
                teste = 0

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

    # Exibe as porcentagens
        print(f"|{cores['vermelho']}Porcentagem A: {perc_a:.2f}% | Porcentagem T: {perc_t:.2f}% | Porcentagem C: {perc_c:.2f}% | Porcentagem G: {perc_g:.2f}%{cores['restaura']}")
        clear = int(input("Deseja limpar? (1-Sim)(2-Não)"))
        if clear == 1:
            os.system('cls')

def sequencia_aleatoria(tamanho):
    a = 0
    t = 0
    c = 0
    g = 0
    
    teste = 0
      
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
        if teste == 0:
            print(f"|{cores['vermelho']}{base}{cores['branco']}-----{cores['verde']}{ligacao}|")
            teste += 1
        elif teste == 1:
            print(f" \{cores['vermelho']}{base}{cores['branco']}---{cores['verde']}{ligacao}/")
            teste += 1
        elif teste == 2:
            print(f"  |{cores['vermelho']}{base}{cores['branco']}-{cores['verde']}{ligacao}|")
            teste += 1
        elif teste == 3:
            print(f" /{cores['vermelho']}{base}{cores['branco']}---{cores['verde']}{ligacao}\ ")
            teste = 0

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



while True:
    
    os.system("cls")

    
                
    
    while True:
        try:
            print(f'''  
    {cores["verde"]}
    ____  ______ __  __     __      _______ _   _ _____   ____  
    |  _ \|  ____|  \/  |    \ \    / /_   _| \ | |  __ \ / __ \ 
    | |_) | |__  | \  / |______ \  / /  | | |  \| | |  | | |  | |
    |  _  |  __| | |\/| |______\ \/ /   | | | . ` | |  | | |  | |
    | |_) | |____| |  | |       \  /   _| |_| |\  | |__| | |__| |
    |____/|______|_|  |_|        \/   |_____|_| \_|_____/ \____/ 
                                                              
                                                              





        ''')
            pergunta = int(input(f"{cores["verde"]}1- Gerar fita aleatória\n2- Mostrar fita existente \n"))
            if pergunta >= 3 or pergunta <= 0:
                print("Valor inválido!")
                time.sleep(2)
                os.system("cls")
                continue
            else:
                break
        except ValueError:
            print("Valor inválido!")
            time.sleep(2)
            os.system("cls")


    if pergunta == 1:
        os.system("cls")
        while True:
            try:
                tamanho = int(input(f"{cores['azul']}Digite o tamanho da bactéria: {cores['restaura']}"))  # Solicita o tamanho da bactéria
                break
        
            except ValueError:
                print("Erro!Valor inválido")
                time.sleep(2)
                os.system('cls')
    
        while True:
            try:
                resp = int(input(f"""{cores["vermelho"]}
    1- Imprimir toda a sequência de DNA{cores["verde"]}
    2- Número de fitas determinado {cores["magenta"]}
    3- Encerrar {cores["restaura"]}"""))
                break
            except ValueError:
                os.system('cls')
        
        while True:
            
            try:
                
                if resp == 1:
                    sequencia_aleatoria(tamanho)
                elif resp == 2:
                    continuar = 2
                    while continuar == 2:
                        fita = int(input(f"{cores["amarelo"]}Quantas fitas de DNA? {cores["verde"]}"))
                        if fita > tamanho or fita <= 0:
                            print("Erro! Número de fitas não condiz com o informado")
                            time.sleep(2)
                            os.system('cls')
                        elif fita <= tamanho:
                            sequencia_aleatoria(fita)
                            while True:
                                try:
                                    continuar = int(input(f"{cores["amarelo"]}Deseja continuar?(1-Acabar)(2-Continuar)"))
                                    if continuar == 1:
                                        controle1 = True

                                        break
                                    elif continuar == 2:
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



    


    elif pergunta == 2:
        sequencia_real()
    
    while True:
        try:
            repetir = int(input("Deseja repetir o programa? (1-Sim)(2-Não) "))
            break
        except ValueError:
            print("Valor inválido")

    if repetir == 2:
        break

    time.sleep(2)
    os.system('cls')

    repetir = 0
    resp = 0 
    continuar = 0
