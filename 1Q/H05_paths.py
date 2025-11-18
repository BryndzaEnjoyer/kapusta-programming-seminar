import random

import os

from datetime import datetime, timedelta

def rad_string(n):
    """
    Creates a string composed of 'n' random lowercase letters.

    Parameters
    ----------
    n : int
        The desired length of the random string.

    Returns
    -------
    str
        The generated random string.
    """
    # Alphabet excludes 'j', 'k', 'q', 'x', 'z' as in your original (slightly modified) code, 
    # but the full alphabet is standard for random string generation.
    abc = "abcdefghijklmnopqrstuvwxyz"
    rad = ""
    for _ in range(n):
        rad += random.choice(abc)
    return rad

def create_list_of_strings(count):
    """
    Creates a list containing a specified number of random strings.
    
    Each string in the list is generated using rad_string(), 
    with a random length between 1 and 10. (Requirement 3 & 4)

    Parameters
    ----------
    count : int
        The desired number of strings (elements) in the list.

    Returns
    -------
    list of str
        The list populated with random strings.
    """
    ran_list = []
    for _ in range(count):
        # Determine a random length for the string (1 to 10 characters)
        string_length = random.randint(1, 10)
        # Use the previous function to generate the string (Requirement 5)
        ran_list.append(rad_string(string_length))
    return ran_list

def multiply_list_elements(input_list):
    """
    Multiplies (repeats) each string in the input list by a random integer (1-3).
    
    This function fulfills Requirement 6.

    Parameters
    ----------
    input_list : list of str
        The list of strings to be multiplied.

    Returns
    -------
    list of str
        A new list with the multiplied (repeated) strings.
    """
    multiplied_list = []
    for s in input_list:
        # Generate a random multiplier (e.g., 1 to 3 times repetition)
        multiplier = random.randint(1, 3) 
        multiplied_list.append(s * multiplier)
    return multiplied_list

def print_string_lengths(input_list):
    """
    Calculates and prints the length (number of characters) of every string in the list.
    
    This fulfills Requirement 7.

    Parameters
    ----------
    input_list : list of str
        The list of strings to analyze.
    """
    print("\n--- Počet znakov (String Lengths) ---")
    for i, s in enumerate(input_list):
        # Display the start of the string for context
        display_str = s[:20] + "..." if len(s) > 20 else s
        print(f"String {i+1} ('{display_str}'): Length: {len(s)}")

def start():
    """
    Main function to execute the assignment steps.
    
    This function coordinates the creation, manipulation, and analysis 
    of the list of random strings.
    """
    print("--- Spustenie programu (Program Start) ---")

    # 1. Determine the number of strings for the list (e.g., 1 to 10)
    N = random.randint(1, 5) 
    print(f"Bude vytvorený zoznam s {N} prvkami (stringami).")
    
    # 2. Create the initial list of random strings
    initial_list = create_list_of_strings(N)
    print("\n--- Vytvorený pôvodný zoznam ---")
    print(initial_list)
    
    # 3. Multiply (repeat) the strings by a random factor (Requirement 6)
    final_list = multiply_list_elements(initial_list)
    print("\n--- Zoznam po prenásobení (String Repetition) ---")
    print(final_list)
    
    # 4. Determine and print the lengths (Requirement 7)
    print_string_lengths(final_list)

# Execute the main function
start()


# --- Konfigurácia priečinkov ---
MAIN_DIR = "data"
SUB_DIR = "dates"
FULL_PATH = os.path.join(MAIN_DIR, SUB_DIR)

def ensure_directories_exist():
    """
    Overí a vytvorí hlavný priečinok 'data' a jeho podpriečinok 'dates'.
    Používa os.makedirs(exist_ok=True) pre bezpečné vytvorenie.
    """
    # 1. Vytvorenie priečinka 'data' a jeho podpriečinka 'dates'
    # os.makedirs s exist_ok=True vytvorí priečinky rekurzívne a nevyvolá chybu, ak už existujú.
    if not os.path.exists(MAIN_DIR):
        print(f"Vytváram hlavný priečinok: {MAIN_DIR}")
    if not os.path.exists(FULL_PATH):
        print(f"Vytváram podpriečinok: {FULL_PATH}")
        
    os.makedirs(FULL_PATH, exist_ok=True)
    
def dice_roll():
    """
    Simuluje hod šesťstennou kockou.
    
    Returns
    -------
    int
        Náhodné celé číslo v rozsahu 1 až 6.
    """
    # 2. Vytvorenie funkcie pre hod kockou
    return random.randint(1, 6)

def generate_dice_rolls(num_rolls):
    """
    Generuje zoznam 'num_rolls' hodov kockou a formátuje ich do reťazca pre zápis.
    
    Parameters
    ----------
    num_rolls : int
        Počet hodov, ktoré sa majú vykonať.
        
    Returns
    -------
    str
        Reťazec s hodmi kockou oddelenými novým riadkom.
    """
    rolls = [str(dice_roll()) for _ in range(num_rolls)]
    return "\n".join(rolls)

def generate_date_files():
    """
    Generuje 10 textových súborov, ktorých názvy začínajú dátumami 
    (desať dní od dnes). Do každého súboru zapíše 10 hodov kockou.
    """
    print("\n--- Generovanie dátumových súborov ---")
    today = datetime.now()
    
    # 3. Vytvorenie 10 súborov pre 10 dní
    for i in range(1, 11): # Generuje 10 dní (1 až 10)
        future_date = today + timedelta(days=i)
        
        # Formát názvu súboru: YYYY-MM-DD_data.txt
        # 4. Vytvorenie Stringov pre názov súboru (s úplnou cestou)
        date_string = future_date.strftime("%Y-%m-%d")
        file_name = f"{date_string}_data.txt"
        file_path = os.path.join(FULL_PATH, file_name)
        
        # 5. Vytvorenie súborov a zápis hodov kockou
        dice_content = generate_dice_rolls(10) # 10 hodov kockou
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(dice_content)
            print(f"Súbor úspešne vytvorený: {file_name}")
        except IOError as e:
            print(f"CHYBA pri zápise súboru {file_name}: {e}")

def create_timestamp_file():
    """
    Vytvorí jeden súbor v hlavnom priečinku 'data', 
    ktorý obsahuje aktuálny čas.
    """
    # 6. Vytvorenie súboru s aktuálnym časom
    now = datetime.now()
    timestamp_string = now.strftime("%Y%m%d_%H%M%S")
    file_name = f"timestamp_{timestamp_string}.txt"
    file_path = os.path.join(MAIN_DIR, file_name)
    
    current_time_content = f"Aktuálny čas vytvorenia: {now.strftime('%d.%m.%Y %H:%M:%S')}"
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(current_time_content)
        print(f"\nSúbor aktuálneho času úspešne vytvorený v '{MAIN_DIR}': {file_name}")
    except IOError as e:
        print(f"CHYBA pri zápise timestamp súboru: {e}")

# --- Hlavná exekúcia ---
if __name__ == "__main__":
    ensure_directories_exist()
    generate_date_files()
    create_timestamp_file()
    print("\nProgram bol dokončený.")