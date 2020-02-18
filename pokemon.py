def calculate_damage(your_type, opponent_type, attack, defense):
    effectivness = 0
    
    dicts = [{"fire":{"grass":2,"water":0.5,"electric":1}},
    {"water":{"fire":2,"grass":0.5,"electric":0.5}},
    {"grass":{"fire":0.5,"water":2,"electric":1}},
    {"electric":{"fire":1,"water":2,"grass":1}}]
    
    if your_type ==  opponent_type:
       effectivness = 0.5
       

    else:       
        for item in dicts:
                for j in item:
                    if j == your_type:
                        print(item[your_type][opponent_type])
                        effectivness = item[your_type][opponent_type]
            
    
       

    return 50 * (attack / defense) * effectivness     



print(calculate_damage("fire", "water", 10, 5))