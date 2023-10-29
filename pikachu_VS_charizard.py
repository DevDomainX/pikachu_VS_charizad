#!/usr/bin/env python3
import os
from time import sleep
from colorama import init, Fore, Style, Back
init()


pikachu = Fore.YELLOW+Style.BRIGHT+"""           PICKACHU

 [1] Impak Trueno                       
  
 [2] Cola de hierro     
                                       
 [3] Impack Trueno X

"""

charizard = Fore.RED+Style.BRIGHT+"""        CHARIZARD

[1] Bola de fuego

[2] Cola de hierro

[3] Bola de poder 

"""


jugadas = 0
jugador1 = Fore.YELLOW+Style.BRIGHT+"pikachu"
vida1 = 100
jugador2 = Fore.RED+Style.BRIGHT+"charizard"
vida2 = 100

while True:
    print(Fore.BLUE+Style.BRIGHT+"Cargando ... ")
    sleep(5)
    os.system("clear")
    print(Fore.GREEN+Style.BRIGHT+"""
    
    Created by: Hans Saldias
    
    by: 1LugarParaProgramar
    
    Script : PIKACHU VS CHARIZARD
    
                BATALLA POKEMŐN""")
    print("                 BATALLA    POKEMON \n\n[1] PIKACHU\n\n[2] CHARIZARD\n\n")
    jugadas += 1
    if jugadas == 1:
        print(Fore.YELLOW+Style.BRIGHT+"Quien va  a tirar ? \n")
    if jugadas == 2:
        print(Fore.RED+Style.BRIGHT+"Quien va  a tirar ? \n")
    if jugadas == 3:
        print(Fore.YELLOW+Style.BRIGHT+"Quien va  a tirar ? \n")
    if jugadas == 4:
        print(Fore.RED+Style.BRIGHT+'Quien va  a tirar ? \n')
    if jugadas == 5:
        print(Fore.YELLOW+Style.BRIGHT+"Quien va  a tirar ? \n")
    if jugadas == 6:
        print(Fore.RED+Style.BRIGHT+"Quien va  a tirar ? \n")
    
    op= int(input("ingrese op: "))
    if op  == 1:
        print("Ataca {}".format(jugador1))
        print(pikachu)
        atake1 = int(input("Ingrese op de atake: "))
        if atake1 == 1:
            print("\nCharizard: aaaaahhh!!!\n")
            vida2 -= 15
            print(Fore.YELLOW+Style.BRIGHT+f"\n\n### {jugador1} ataka a {jugador2} quedando con {vida2}% de vida   ###")      
        if atake1 == 2:
            vida2 -= 15
            print(Fore.YELLOW+Style.BRIGHT+f"{jugador1} ataka a {jugador2} quedando con {vida2}% de vida")      
        if atake1 == 3:
            vida2 -= 15
            print(Fore.YELLOW+Style.BRIGHT+f"{jugador1} ataka a {jugador2} quedando con {vida2}% de vida")      
        if vida2 <= 0:
            print(Fore.YELLOW+Style.BRIGHT+f"\n{jugador1} Ha Ganado!!!\n")
            print("\nFin del juego.....")
            break
    if op == 2:
        print(Fore.RED+Style.BRIGHT+f"ataca {jugador2}...")
        print(charizard)
        atake2 = int(input("ingrese op de atake: "))
        if atake2 == 1:
            vida1 -= 15
            print(Fore.RED+Style.BRIGHT+f"{jugador2} ataka a {jugador1} quedando con {vida1}% de vida")
        if atake2 == 2:
            vida1 -= 15
            print(Fore.RED+Style.BRIGHT+f"{jugador2} ataka a {jugador1} quedando con {vida1}% de vida")
        if atake2 == 3:
            vida1 -= 15
            print(Fore.RED+Style.BRIGHT+f"{jugador2} ataka a {jugador1} quedando con {vida1}% de vida")
        if vida1 <= 0:
            print(Fore.RED+Style.BRIGHT+f"\n{jugador2} Ha Ganado!!!\n{jugador2} con {vida2}% de vida {jugador1} con {vida1}")
            print("\nFin del juego.....")
            break
        
        
       
            
        
