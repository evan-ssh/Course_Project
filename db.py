#players blackjack bank
FILENAME = "playermoney.txt"
def load_bank(FILENAME):    
    try:
        with open(FILENAME, "r") as file:
            return float(file.read().strip())
    except FileNotFoundError:
        print("no money in bank. starting with 100")
        return 100.0        

def save_bank(FILENAME, amount):
    try:
        with open(FILENAME, "w") as file:
            file.write(str(amount))
    except FileNotFoundError:
        print("File cant be found to be saved.")
   
