def print_characters(word):
    """
    Prints every character in the given word, one per line.

    How it works:
        - Iterates through the string using a for-loop.
        - Prints each character individually.

    Parameters:
        word (str): The word whose characters will be printed.
    """
    for char in word:
        print(char)


def print_message_n_times(message, n):
    """
    Prints a given message a specified number of times.

    How it works:
        - Uses range(n) to repeat printing exactly n times.

    Parameters:
        message (str): The message to be printed.
        n (int): Number of repetitions.
    """
    for _ in range(n):
        print(message)


def print_words_in_sentence(sentence):
    """
    Splits a sentence into words and prints each word.

    How it works:
        - Uses .split(" ") to divide the sentence into a list of words.
        - Prints each word by iterating through the list.

    Parameters:
        sentence (str): The input sentence to split and print.
    """
    words = sentence.split(" ")
    for word in words:
        print(word)


def reverse_string(word):
    """
    Returns the reverse of the given word.

    How it works:
        - Iterates through the string.
        - Builds the reversed version by prepending each character.

    Parameters:
        word (str): The word to reverse.

    Returns:
        str: The reversed word.
    """
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word


def print_with_indices(word):
    """
    Prints each character in the word along with its index.

    How it works:
        - Uses enumerate() to get both index and character.
        - Prints index and character on each line.

    Parameters:
        word (str): The word to enumerate.
    """
    for index, char in enumerate(word):
        print(index, char)


def count_e_letters(text):
    """
    Counts how many times 'e' or 'E' appears in a text.

    How it works:
        - Iterates through each character.
        - Increments counter if character is 'e' or 'E'.

    Parameters:
        text (str): Text to search through.

    Returns:
        int: Number of 'e' or 'E' characters.
    """
    count = 0
    for char in text:
        if char == "e" or char == "E":
            count += 1
    return count


def print_vowels(text):
    """
    Prints all vowels found in the text.

    How it works:
        - Defines a list of vowels.
        - Prints any character in the text that is a vowel.

    Parameters:
        text (str): The string to check for vowels.
    """
    vowels = ["a", "e", "i", "o", "u"]
    for char in text.lower():
        if char in vowels:
            print(char)


def extract_odd_index_characters(text):
    """
    Returns a string of characters at odd indices.

    How it works:
        - Uses enumerate to track positions.
        - Adds characters where index % 2 != 0.

    Parameters:
        text (str): The input string.

    Returns:
        str: Characters at odd indices.
    """
    result = ""
    for index, char in enumerate(text):
        if index % 2 != 0:
            result += char
    return result


def incremental_join(word):
    """
    Builds and prints the word progressively, joining characters with spaces.

    How it works:
        - Creates an empty list.
        - Appends characters one by one.
        - Uses " ".join() to print the current progress at each step.

    Parameters:
        word (str): The word to process.
    """
    letters = []
    for char in word:
        letters.append(char)
        print(" ".join(letters))


def shift_letters_by_one(text):
    """
    Shifts each character in the text by 1 in ASCII, prints the last shifted character.

    How it works:
        - Converts char with ord(), adds 1, then converts back using chr().
        - Only the final shifted character is printed (same behavior as original code).

    Parameters:
        text (str): The string to shift.
    """
    for char in text:
        shifted = chr(ord(char) + 1)
    print(shifted)


def print_all_substrings(text):
    """
    Prints all possible substrings of the given text.

    How it works:
        - Uses two nested loops:
            Outer loop: start index
            Inner loop: end index
        - Prints text[start:end] for all valid ranges.

    Parameters:
        text (str): The string from which to generate substrings.
    """
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            print(text[i:j])
