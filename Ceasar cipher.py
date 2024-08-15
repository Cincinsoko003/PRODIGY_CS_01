def caesar_cipher(text, shift, mode):
  """Encrypts or decrypts a text using the Caesar cipher.

  Args:
    text: The text to be encrypted or decrypted.
    shift: The number of positions to shift the letters.
    mode: The mode of operation, either 'encrypt' or 'decrypt'.

  Returns:
    The encrypted or decrypted text.
  """

  result = ""
  # traverse text
  for char in text:
    # Encrypt this character
    if char.isupper():
      result += chr((ord(char) + shift - 65) % 26 + 65)
    elif char.islower():
      result += chr((ord(char) + shift - 97) % 26 + 97)
    else:
      result += char

  if mode == 'decrypt':
    # Decrypt by shifting in the opposite direction
    shift = -shift
    return caesar_cipher(result, shift, 'encrypt')
  else:
    return result

# Get input from the user
text = input("Enter your message: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter mode (encrypt/decrypt): ")

# Call the function and print the result
result = caesar_cipher(text, shift, mode)
print("The", mode, "ed text is:", result)
