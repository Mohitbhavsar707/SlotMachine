import random

# Constants for the slot machine
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Slot machine dimensions
ROWS = 3
COLS = 3

# Symbols and their corresponding counts and values
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6, 
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3, 
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    # Calculate the winnings from the slot machine spin
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines
            
def get_slot_machine_spin(rows, cols, symbols):
    # Generate a spin for the slot machine
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Making a copy of the list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    # Print the slot machine columns in a readable format
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    # Prompt the user to deposit money and ensure it's a valid positive number
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

def get_number_of_lines():
    # Prompt the user to enter the number of lines to bet on
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
            
    return lines

def get_bet():
    # Prompt the user to enter their bet amount per line
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return amount

def spin(balance):
    # Perform a spin of the slot machine and update the balance based on the outcome
    lines = get_number_of_lines()
    while True:
        bet = get_bet()   
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    # Main function to run the slot machine game
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

# Start the game
main()