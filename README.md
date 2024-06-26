# Cryptography Project

This project implements basic encryption and decryption functions using a custom algorithm. The functions are designed to transform plaintext into ciphertext and vice versa, ensuring the original message can be retrieved when decrypted with the correct key.

## Project Structure

# Encrypt and Decrypt Functions

## Overview

The `encrypt` and `decrypt` functions are designed to transform a plaintext message into ciphertext and vice versa. The encryption process involves shifting each character in the plaintext by a specified key value, while the decryption process reverses this shift.

## Functions

### `encrypt(text, key)`

The `encrypt` function takes a plaintext string and a key as input and returns the encrypted ciphertext. Each character in the text is shifted by the key value. If the character is lowercase, it remains lowercase; if uppercase, it remains uppercase.

#### Parameters

- `text` (str): The plaintext to be encrypted.
- `key` (int): The encryption key, which determines the number of positions each character is shifted.

#### Returns

- `str`: The encrypted text (ciphertext).

#### Example

```python
plaintext = "abc"
key = 1
ciphertext = encrypt(plaintext, key)
print(ciphertext)  # Output: "bcd"
```

### `decrypt(text, key)`

The `decrypt` function takes a ciphertext string and a key as input and returns the decrypted plaintext. Each character in the text is shifted back by the key value. If the character is lowercase, it remains lowercase; if uppercase, it remains uppercase.

#### Parameters

- `text` (str): The ciphertext to be decrypted.
- `key` (int): The decryption key, which determines the number of positions each character is shifted back.

#### Returns

- `str`: The decrypted text (plaintext).

#### Example

```python
ciphertext = "bcd"
key = 1
plaintext = decrypt(ciphertext, key)
print(plaintext)  # Output: "abc"
```