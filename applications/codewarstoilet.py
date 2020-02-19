def get_free_urinals(urinals):
    len(urinals)
    space = 0
    if int(urinals) < 1:
        return -1
        
    for i in range(len(urinals)):
            print(urinals[i],urinals[i+1])   
            if i == len(urinals) - 2:
                break    
            elif urinals[i] == "0" and urinals[i+1] == "0":
                print("test")
                space += 1
                                     
    return space     

print(get_free_urinals("10001"))