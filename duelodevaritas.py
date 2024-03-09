import random

options = ["Petrificus totalus", "Impedimenta", "Tragacaracoles"]

print("Bienvenidos al duelo de varitas.")
print("Elegirán un hechizo con su varita y lo lanzarán a su oponente a la cuenta de tres.")
print("Varitas listas!")
print("Malfoy: Asustado Potter?")
print("Harry Potter: Ya quisieras!")
print("A la cuenta de tres, lanza tus hechizos sólo para desarmar a tu oponente. Sólo para desarmar.")
print("Uno, dos..")
print("")


player_choice = input (
    "Qué hechizo elegirás? Petrificus totalus, Impedimenta, Tragacaracoles: ").capitalize()
print("")

computer_choice = random.choice (options)

print (f"Harry Potter '{player_choice}'")
print (f"Malfoy '{computer_choice}'")
print("")

if player_choice == "Impedimenta" and computer_choice == "Petrificus totalus":
    print("Harry Potter gana! 10 puntos para Gryffindor!")
elif player_choice ==  "Tragacaracoles" and computer_choice == "Petrificus totalus":
    print("Malfoy gana! 10 puntos para Slytherin!")
elif player_choice == "Petrificus totalus" and computer_choice == "Tragacaracoles":
    print("Harry Potter Gana! 10 puntos para Gryffindor!")
elif player_choice == "Impedimenta" and computer_choice == "Tragacaracoles":
    print("Malfoy gana! 10 puntos para Slytherin!")
elif player_choice == "Tragacaracoles" and computer_choice == "Impedimenta":
    print("Harry Potter gana! 10 puntos para Gryffindor!")
elif player_choice == "Petrificus totalus" and computer_choice == "Impedimenta":
    print("Malfoy gana! 10 puntos para Slytherin!")
else:
    print("Ninguno se hizo daño")
    
