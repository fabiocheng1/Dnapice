from random import *
import time
import os
from colors import *

def sequencia(tamanho):
    for ciclo in range(tamanho):
        base = choice(list(bases.keys()))
        ligacao = bases[base]
        print(f"|{cores["vermelho"]}{base}--{cores["verde"]}{ligacao}|")






bases = {"A":"T" , "T": "A" , "C":"G" , "G":"C"} #Contitui as bases e as ligações correspondentes

tamanho = int(input(f"{cores["azul"]} Digite o tamanho da bactéria:")) #Informa o tamanho da bactéria em questão

resp = int(input(f"""
{cores["vermelho"]}1- Imprimir toda a sequência de DNA
{cores["verde"]}2- Número de fitas determinado
{cores["magenta"]}3- Encerrar
{cores["restaura"]}

                                                           
                                    :::             .:.                                   
                                     :::.          .::                                    
                                      .:-..       :::                                     
                                        .:-:.   :::.                                      
                                          .:-.::::                                        
                                           .:---:                                         
                                         .:::. ::::                                       
                                       .:::.     :::.                                     
                                     .:::.        .:-.                                    
                                    .::.           .::                                    
                                    ::               --                                   
                                   --.               .:                                   
                                   :.                ...                                  
                                   ::                ::.                                  
                                   ::                ::                                   
                                   ::               .:-                                   
                                   :::             :::                                    
                                    .--           -:.                                     
                                      -:.     ..-::.                                      
                                       .--    -:..                                        
                                        ..---- .                                          
                                         .=-=-                                            
                                       .--   .=-..                                        
                                      --.       -:.                                       
                                    .--           --                                      
                                   .::             :-:                                    
                                   .:               .::                                   
                                   --                ::                                   
                                   ..                ::.                                  
                                   :.                .:.                                  
                                   --.               ...                                  
                                    -:               -=                                   
                                    .::.            ::                                    
                                     .:::.         .-.                                    
                                       .:::.     .::.                                     
                                         .:::. .:::                                       
                                           .:-:-:                                         
                                          .:::.::.                                        
                                        .:::.   :::.                                      
                                      .:-:.       .::                                     
                                     :::.          .::                                    
                                    .::             ::.                                   
                                    :.               --.                                  
                                   -=                 :                                   


"""))


if resp == 1:
    sequencia(tamanho)
elif resp == 2:
    continuar = 0
    while continuar != 3:
        
        
        fita = int(input(f"{cores["amarelo"]}Quantas fitas?"))
        sequencia(fita)
        continuar = int(input(f"{cores["amarelo"]}Deseja continar? (3 Para acabar)"))



limpar = int(input(f"{cores["amarelo"]}Deseja limpar? 1-Sim 2-Não"))


if limpar == 1: 
    time.sleep(1.0)
    os.system('cls')




      



            



    