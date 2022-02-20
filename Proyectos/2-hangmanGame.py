import random
import os

def word ():
    with open ("./archivos/data.txt","r", encoding="utf-8") as f:
        words = [line.replace("\n","") for line in f]
        
    random_word = random.choice(words)    
    return random_word.upper()
    

def run():
    
    ahorcado = ["""
      _ _    _ ______ _____  ____     _____  ______ _                  _    _  ____  _____   _____          _____   ____  
     | | |  | |  ____/ ____|/ __ \   |  __ \|  ____| |           /\   | |  | |/ __ \|  __ \ / ____|   /\   |  __ \ / __ \ 
     | | |  | | |__ | |  __| |  | |  | |  | | |__  | |          /  \  | |__| | |  | | |__) | |       /  \  | |  | | |  | |
 _   | | |  | |  __|| | |_ | |  | |  | |  | |  __| | |         / /\ \ |  __  | |  | |  _  /| |      / /\ \ | |  | | |  | |
| |__| | |__| | |___| |__| | |__| |  | |__| | |____| |____    / ____ \| |  | | |__| | | \ \| |____ / ____ \| |__| | |__| |
 \____/ \____/|______\_____|\____/   |_____/|______|______|  /_/    \_\_|  |_|\____/|_|  \_\\_____/_/    \_\_____/ \____/         
        
        ""","""
        +----------+
        ||         |
        ||         |
        ||         | 
        ||        
        || 
        || 
        || 
        ||
---------------------------
---------------------------""",
"""
        +----------+
        ||         |
        ||         |
        ||         | 
        ||         O
        ||         
        ||         
        ||        
        ||
---------------------------
---------------------------""",
"""
        +----------+
        ||         |
        ||         |
        ||         | 
        ||         O
        ||         |
        ||         
        ||        
        ||
---------------------------
---------------------------""",
"""
        +----------+
        ||         |
        ||         |
        ||         | 
        ||         O
        ||        /|
        ||         
        ||        
        ||
---------------------------
---------------------------""",
"""
        +----------+
        ||         |
        ||         |
        ||         | 
        ||         O
        ||        /|\\
        ||         
        ||        
        ||
---------------------------
---------------------------""",
"""
        +----------+
        ||         |
        ||         |
        ||         | 
        ||         O
        ||        /|\\
        ||         |
        ||         
        ||
---------------------------
---------------------------""",
"""
        +----------+
        ||         |
        ||         |
        ||         | 
        ||         O
        ||        /|\\
        ||         |
        ||        / 
        ||
---------------------------
---------------------------""",
"""
        +----------+
        ||         |
        ||         |
        ||         | 
        ||         O
        ||        /|\\
        ||         |
        ||        / \\
        ||       
---------------------------
---------------------------""",
"""
_____  ______ _____  _____ _____  _____ _______ ______ 
|  __ \|  ____|  __ \|  __ \_   _|/ ____|__   __|  ____|
| |__) | |__  | |__) | |  | || | | (___    | |  | |__   
|  ___/|  __| |  _  /| |  | || |  \___ \   | |  |  __|  
| |    | |____| | \ \| |__| || |_ ____) |  | |  | |____ 
|_|    |______|_|  \_\_____/_____|_____/   |_|  |______|
""",
"""
          _____ _______      _______ _   _           _____ _______ ______   _ 
    /\   |  __ \_   _\ \    / /_   _| \ | |   /\    / ____|__   __|  ____| | |
   /  \  | |  | || |  \ \  / /  | | |  \| |  /  \  | (___    | |  | |__    | |
  / /\ \ | |  | || |   \ \/ /   | | | . ` | / /\ \  \___ \   | |  |  __|   | |
 / ____ \| |__| || |_   \  /   _| |_| |\  |/ ____ \ ____) |  | |  | |____  |_|
/_/    \_\_____/_____|   \/   |_____|_| \_/_/    \_\_____/   |_|  |______| (_)
"""]
    word_pc = word()
    
    word_user = []
    for i in range(len(word_pc)):
        word_user.append(" _ ")
    
    
    letra = ""
    letras_usadas = []
    final_word = ""
    errors = ""
    failed_attempt = 1
    
    while final_word != word_pc:
        if failed_attempt > 7:
            os.system("clear")
            print(ahorcado[9])
            print("La palabra era " + word_pc)
            break
        else:
            fail = True 
            print(ahorcado[0])
            print(ahorcado[failed_attempt])
            #print(failed_attempt)
            #print(word_pc)
            print("\nAdivina la palabra!\n" + "".join(word_user) + 
                "\n\nLas letras que has usado son: " + ",".join(letras_usadas) + "\n" + errors)
            
            letra = input("\nIngresa una letra: ").upper()        
            
            if len(letra) > 1 or letra.isnumeric():
                errors = "No se pueden ingresar números y solo puedes ingresar una letra"
                fail = False
            elif letra in letras_usadas:
                errors = "La letra " + letra + " ya fue usada"
                fail = False
            else:
                errors = ""
                letras_usadas.append(letra)
                       
            for i in range(len(word_pc)):
                if letra == word_pc[i]:
                    word_user[i] = letra + " "
                    fail = False
                    
            if fail:
                failed_attempt += 1
                
            final_word = "".join(word_user)
            final_word = final_word.replace(' ','')
            if final_word == "".join(word_pc):
                os.system("clear")
                print(ahorcado[10])                
                print("la palabra era " + word_pc)
            else:
                os.system("clear")
            
            
if __name__ == '__main__':
    run()