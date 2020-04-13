import random
import os
print("####   Benvenuto a LUPUS in TABULA  ####\n\n")
print("In questa versione del gioco rivisitata sono disponibili 4 ruoli: Coniglio Mannaro, Ubriacone, Polizia Municipale e Drone.\n"
      "Sono, ovviamente, i corrispettivi Lupo, Contadino, Guardia e Veggente del gioco originale!\n\n"
      "-- Questa schermata è riservata SOLO al master del gioco! --\n"
      "-- Ci saranno un solo Drone ed una sola Polizia Municipale! Ti basta inserire il numero di Conigli Mannari e di Ubriaconi ed il gioco può cominciare! --\n\n")
ruoli = ['Polizia Municipale', 'Drone']
for i in range(int(input("Quanti Conigli Mannari?\n"))):
  ruoli.append('Coniglio Mannaro')
for i in range(int(input("Quanti Ubriaconi?\n"))):
  ruoli.append('Ubriacone')
abbinamenti = {}
random.shuffle(ruoli)
random.shuffle(ruoli)
for i in range(len(ruoli)):
  abbinamenti[input(f"Inserisci il {i+1}° giocatore\n")] = ruoli.pop()

input("Pronti a cominciare?? ( Premi invio ;) )")
os.system('cls')
for el in abbinamenti:
  if abbinamenti[el] == 'Polizia Municipale':
    print(f"{el} è la {abbinamenti[el]}")
  elif abbinamenti[el] == 'Drone':
    print(f"{el} è il {abbinamenti[el]}")
  else:
    print(f"{el} è un {abbinamenti[el]}")
input("\nPremi invio per chiudere... e BUON DIVERTIMENTO!!!")