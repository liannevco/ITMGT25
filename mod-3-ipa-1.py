'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
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
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",'O','P',"Q",'R','S','T',"U",'V','W','X','Y','Z']

    if letter in alphabet:
        index = alphabet.index(letter)

        new_letter_number = index + shift

        if new_letter_number >= 26:
            num_wrap = int(new_letter_number / 25)
            return alphabet[new_letter_number - 26*num_wrap]
        elif new_letter_number < 26:
            return alphabet[new_letter_number]
    else:
        return ' '

    

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
    ciphered_message = []
    changes = []
    
    caps_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    low_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for character in message:
        if character in caps_alphabet:
            index = caps_alphabet.index(character)
            cipher = (index+shift)%26
            changes.append(cipher)
            new_character = caps_alphabet[cipher]
            ciphered_message.append(new_character)
        elif character in low_alphabet:
            index = low_alphabet.index(character)
            cipher = (index+shift)%26
            changes.append(cipher)
            new_character = low_alphabet[cipher]
            ciphered_message.append(new_character)
        else:
            ciphered_message.append(character)
            
    return ''.join(ciphered_message)

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
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",'O','P',"Q",'R','S','T',"U",'V','W','X','Y','Z']

    if letter in alphabet:
        index = alphabet.index(letter)

        shift_num = alphabet.index(letter_shift)

        new_letter_number = index + shift_num

        if new_letter_number >= 26:
            num_wrap = int(new_letter_number / 25)
            return alphabet[new_letter_number - 26*num_wrap]
        elif new_letter_number < 26:
            return alphabet[new_letter_number]
    else:
        return ' '

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
    ciphered_message = []
    message_length = len(message)
    key_length = len(key)
    missing_key = []
    key_indices = []
    key_list = list(key)
    
    caps_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for element in message:
        
        if element in caps_alphabet:
            
            if message_length > key_length:
                difference = message_length - key_length
                
                for missing in range(0,difference+1):
                    key_list.append(key_list[missing])
                    missing_key.append(key_list[missing])
                    new_key = ''.join(missing_key)
                        
                for letter in new_key:
                    index = caps_alphabet.index(letter)
                    key_indices.append(index)

                element_alphabet_index = caps_alphabet.index(element)
                element_message_index = message.index(element)
                element_key_index = key_indices[element_message_index]
                cipher = (element_alphabet_index + element_key_index) % 26
                new_character = caps_alphabet[cipher]
                ciphered_message.append(new_character)
            
            else:
                for letter in key_list:
                    index = caps_alphabet.index(letter)
                    key_indices.append(index)

                element_alphabet_index = caps_alphabet.index(element)
                element_message_index = message.index(element)
                element_key_index = key_indices[element_message_index]
                cipher = (element_alphabet_index + element_key_index) % 26
                new_character = caps_alphabet[cipher]
                ciphered_message.append(new_character)
                
        else:
            ciphered_message.append(element)
                    
        
    return ''.join(ciphered_message)

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
    original_length = len(message)
    cipher_process = message
    cipher_length = len(cipher_process)
    
    if cipher_length%shift != 0:
        while cipher_length%shift !=0:
            cipher_process += '_'
    
    scytale=''
    
    for character in range(cipher_length):
        scytale += cipher_process[(character//shift) + (original_length // shift) * (character%shift)]
        
    return scytale

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
    cipher_process = message[1:]
    cipher_length = len(cipher_process)
    decipher = ''
    decipher_length = len(decipher)
    increment=1
    
    while decipher_length < cipher_length:
        if increment > cipher_length:
            increment = 1
        if shift == 1:
            decipher += cipher_process[increment-1]
            increment += 1
        else:
            increment += 1
            shift -= 1
            
    return message[0] + decipher