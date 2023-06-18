'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter != " ":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index_letter = alphabet.index(letter)
        index_shifted = (index_letter + shift) % 26
        shifted_letter = alphabet[index_shifted]
        return shifted_letter
    else:
        print("no letter breh")

print(shift_letter("A",19))
print(shift_letter("Z",5))
print(shift_letter("Z",1))
print("-----")

def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message_shifted = ""

    for letter in message:
        if letter == " ":
            message_shifted += " "
        else:
            index_letter = alphabet.index(letter)
            index_shifted = (index_letter + shift) % 26
            shifted_letters = alphabet[index_shifted]
            message_shifted += shifted_letters

    return message_shifted.lower()

print(caesar_cipher("tea is the coolest ever", 5))
print("-----")

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter != " ":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter_to_number = alphabet.index(letter_shift)
        index_letter = alphabet.index(letter)
        index_shifted = (index_letter + letter_to_number) % 26
        shifted_letter = alphabet[index_shifted]
        return shifted_letter
    elif letter_shift == " ":
        print("no letter breh")
    else:
        print("no letter breh")

print(shift_by_letter("A","C"))
print("-----")

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #sample: message = betita 6
    #sample: replace = tea 3
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    repeated_key = key * (len(message) // len(key) + 1) + key[:len(message) % len(key)]
    final_message = ""
    key_index = 0

    for x in range(len(message)):
        if message[x] != " ":
            index_message = alphabet.index(message[x])
            index_key = alphabet.index(repeated_key[x])
            index_shift = (index_message + index_key) % 26
            message_to_key = alphabet[index_shift]
            final_message += message_to_key
        else:
            final_message += " "
    
    return final_message

print(vigenere_cipher("kendall roman and shiv roy", "hi"))
print("-----")
    
def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if len(message) % shift != 0:
        message += "_" * (shift - (len(message) % shift))

    gibberish = ""
    for x in range(len(message)):
        index = (x // shift) + (len(message) // shift) * (x % shift)
        gibberish += message[index]
    
    return gibberish

print(scytale_cipher("i love jbizzle and boniver", 10))
print("-----")

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    rows = len(message) // shift
    columns = shift

    grid = [[""] * columns for _ in range(rows)]
    index = 0

    for x in range(rows):
        for y in range(columns):
            grid[x][y] = message[index]
            index += 1

    non_gibberish = ""
    for y in range(columns):
        for x in range(rows):
            non_gibberish += grid[x][y]

    non_gibberish = non_gibberish.replace("_"," ")

    return non_gibberish

print(scytale_decipher("ivjzenbir_lebz_dov__o_ila_ne__", 10))