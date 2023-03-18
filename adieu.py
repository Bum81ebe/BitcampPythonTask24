import inflect

text = inflect.engine()

words = []


while True:
    try:
        
        
        c = input("Name: ")
        if x != "":
            words.append(x)
            
            
        else:
            continue
    except EOFError:
        
        print("Adieu, adieu, to " + text.join(words))
        break 
