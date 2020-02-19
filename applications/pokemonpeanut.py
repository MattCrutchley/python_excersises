from pokemon import pokemon
import random
choice = input("choose your wepon \n big bad bob  \n wheres my whey jay \n ")
if choice == "big bad bob":
    your_pokemon = pokemon(choice,100, 60, 80, "water")   
else:
    your_pokemon = pokemon(choice,100, 80, 60,"fire")

battle = input("choose a pokemon to battle \n C \n D \n ")

if choice == "C":
    opponent_pokemon = pokemon(choice,100, 60, 80, "grass")   
else:
    opponent_pokemon = pokemon(choice,100, 80, 60,"water")

while getattr(your_pokemon, "hp") > 0:
    cmd = input("x to attack")
    if cmd == "x":
        damage = your_pokemon.calculate_damage(getattr(your_pokemon,"type_"),getattr(opponent_pokemon,"type_"),random.randint(1,50),random.randint(1,50))
        print("damage ", damage)
        setattr(opponent_pokemon,"hp",getattr(opponent_pokemon,"hp") - damage)
        print("opponents hp: ",getattr(opponent_pokemon,"hp"))
