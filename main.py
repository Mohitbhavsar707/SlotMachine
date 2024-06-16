import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6, 
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = [[], [], []]
    for col in range(cols):
        coloumn = []
        for row in range(rows):
            value = random.choice(all_symbols)
            
    



def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        #check if the amount is a number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

def get_numebr_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+ str(MAX_LINES)+ ")? ")
        #check if the amount is a number
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
            
    return lines
    
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        #check if the amount is a number
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return amount
    

def main():
    balance = deposit()
    lines = get_numebr_of_lines()
    while True:
        bet = get_bet()   
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to be tthat amount, your current balance is: ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on ${lines} lines. Total bet is equal to: ${total_bet}")
    
    
main()