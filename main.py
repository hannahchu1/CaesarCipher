name=input("What's your name? ")
print("Hello, " +name+ "!")
print("\n")

# Encrytion is process of encoding data (plain text to ciphertext). Done with a key called Encryption Key.
# Decryption is process of decoding encoded data (ciphertext to plain text). Needs Encrytion Key used for encoding.

def encryption():
# function for choosing E or D
  print("Would you like to:")
  print("1. Encrypt")
  print("2. Decrypt")
  while True:
    userInput=int(input("Enter your choice: "))
    if userInput==1 or userInput==2:
      break
    else:
      print("Invalid choice! Please choose either 1 or 2!")
  if userInput==1:
    encrypt()
  else:
    decrypt()

# Encrypting
def encrypt():
  print("\n")
  print("Let's start Encrypting!")
  while True:
    plain = input("Enter a text: ")
    if plain != "":
      break
  while True:
    key = int(input("Enter an integer between 3-25: "))
    if (key > 2) and (key < 26):
      break
    else:
      print("Key must be an integer between 3 and 25!")

# establish key and the encrypted text
  key=int(key)
  encrypt_text = ""

  for c in range(len(plain)):
    crypt = (chr(ord(plain[c]) + key))
    # ord(changing to unicode number)+key
    # chr(new unicode)-- new character=crypt
    encrypt_text += crypt
  print("Encrypted text: " +encrypt_text)
  encryption_back()
# ord()-- character to numeric rep in Unicode
# chr()-- numeric to character

# decrypting cipher
def decrypt():
  print("\n")
  print("Let's start Decrypting!")
  while True:
    cipher = input("Enter a ciphertext: ")
    if cipher != "":
      break
  while True:
    key = int(input("Enter the key now: "))
    if (key > 2) and (key < 26):
      break
    else:
      print("Key must be an integer between 3-25!")
  
  key=int(key)
  decrypt_text = ""

  for x in range(len(cipher)):
    plain_text = (chr(ord(cipher[x]) - key))
    decrypt_text += plain_text
  if " " in decrypt_text:
    print("Decrypted text: " +decrypt_text)
    encryption_back()
  else:
    print("Key does not match! Please try again!")
  encryption_back()


def encryption_back():
  while True:
    print("\n")
    back = input("Enter 'B' to go back! ")
    if back == "B":
      encryption()
      break
# function to circle back to beginning of encryption function

encryption()


# plain=input("Enter a text: ")
# userKey=int(input("Please enter an integer between 3-25 as the Key: "))

# print("Plain Text: " +plain)
# print("Key: ", userKey)

# def caesar(plain, userKey):
#   cipherText=""
#   for c in plain:
#     if c.isalpha():
#       c_index= chr((ord(c)+ userKey))
#     cipherText+= c_index
# caesar(plain, userKey)

# def caesar(plain, userKey): 
#   cipherText = ""
#   for c in plain:
#     if c.isalpha():
#       c_index = ord(c) + userKey 
#       if c_index > ord('z'):
#         c_index -= 26
#       finalLetter = chr(c_index)
#       cipherText += finalLetter
#   print ("Your ciphertext is: ", cipherText)
#   return cipherText
# caesar(plain,userKey)