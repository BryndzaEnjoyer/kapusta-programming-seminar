import tkinter as tk
import random

memory = []
root = tk.Tk()
root.title("U01_Kapusta")
root.geometry("400x500")


def enter():
    """
    Add the text entered by the user into the memory list.

    How it works:
        - Reads text from the INPUT text widget.
        - Removes the trailing newline using "end-1c".
        - Appends the text to the global 'memory' list.
        - Prints the updated memory list to the console.

    Parameters:
        None

    Returns:
        None
    """
    memory.append(INPUT.get("1.0", "end-1c"))
    print(memory)


def mix():
    """
    Shuffle the stored words in 'memory' and choose a random position
    for the user to guess.

    How it works:
        - Swaps elements in 'memory' using a custom swapping pattern.
        - Selects a random index in the list.
        - Updates label2 to ask the user which word is at the chosen position.

    Global Variables Used:
        memory (list): Word storage.
        pos (int): Randomly chosen index for guessing.

    Parameters:
        None

    Returns:
        None
    """
    global pos
    for i in range(1, len(memory) - 1):
        memory[i + 1], memory[i] = memory[i], memory[i + 1]
        memory[0], memory[i - 1] = memory[i - 1], memory[0]

    print(memory)

    pos = random.randint(0, len(memory) - 1)
    label2.config(text=f"What word is on the position: {pos}")


def guess():
    """
    Check whether the user's guessed word matches the word stored
    at the generated random position.

    How it works:
        - Reads user input from GUESS text widget.
        - Compares it with memory[pos].
        - Updates label2 with "Correct" or "Incorrect".

    Global Variables Used:
        memory (list)
        pos (int): the index the user must guess

    Parameters:
        None

    Returns:
        None
    """
    if memory[pos] == GUESS.get("1.0", "end-1c"):
        label2.config(text="Correct")
    else:
        label2.config(text="Incorect")


# --- GUI elements ---

label = tk.Label(root, text="Enter data", font=("Arial", 16))
label.pack(pady=20)

INPUT = tk.Text(root, height=2, width=30)
INPUT.pack()

button = tk.Button(root, text="Enter", command=enter)
button.pack(pady=10)

button2 = tk.Button(root, text="shuffle", command=mix)
button2.pack(pady=10)

GUESS = tk.Text(root, height=2, width=30)
GUESS.pack()

button3 = tk.Button(root, text="guess", command=guess)
button3.pack(pady=10)

label2 = tk.Label(root, text="", font=("Arial", 16))
label2.pack(pady=20)

root.mainloop()
