def encrypt(text, key):
    """
    Encrypts the given text using the provided key.

    This function shifts each character in the text by the key value.
    If the character is lowercase, it remains lowercase; if uppercase, it remains uppercase.

    Args:
        text (str): The plaintext to be encrypted.
        key (int): The encryption key.

    Returns:
        str: The encrypted text (ciphertext).
    """
    encrypted = ''.join(chr((ord(char) + key - 97) % 26 + 97) if char.islower() else chr((ord(char) + key - 65) % 26 + 65) for char in text)
    return encrypted

def decrypt(text, key):
    """
    Decrypts the given text using the provided key.

    This function shifts each character in the text back by the key value.
    If the character is lowercase, it remains lowercase; if uppercase, it remains uppercase.

    Args:
        text (str): The ciphertext to be decrypted.
        key (int): The decryption key.

    Returns:
        str: The decrypted text (plaintext).
    """
    decrypted = ''.join(chr((ord(char) - key - 97) % 26 + 97) if char.islower() else chr((ord(char) - key - 65) % 26 + 65) for char in text)
    return decrypted
