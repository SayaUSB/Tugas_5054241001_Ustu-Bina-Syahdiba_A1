#user input
cmd, K = map(int, input("Masukkan command : ").split())

char = [] 
line = input("Masukkan kalimat : ") 

shifted_text = []

if cmd == 1 : # Enkripsi
    for char in line : 
        if 'A' <= char <= 'Z' :
            another_char = chr(((ord(char)- ord ('A')+ K)%26) + ord ('A'))  
        elif 'a' <=char <= 'z' : 
            another_char = chr(((ord(char)- ord ('a')+ K)%26) + ord ('a'))  
        else : 
            another_char = char  
        shifted_text.append(another_char)
elif cmd==2 : # Dekripsi
    for char in line : 
        if 'A' <= char <= 'Z' : 
            another_char = chr(((ord(char)- ord ('A')- K)%26) + ord ('A'))  
        elif 'a' <=char <= 'z' :  
            another_char = chr(((ord(char)- ord ('a')- K)%26) + ord ('a')) 
        else : 
            another_char = char
        shifted_text.append(another_char)
shifted_text.append('\n')

print("".join(shifted_text))