choice = input("Encode or Decode: ").lower()
word_encode = input("Input the word you want to Encrypt: ")
shift_encode = int(input("Please enter a number to be use for shift: ")) 


def cipher_encode(text,s):
  encrypted_text_result = " "

  #this for loop will travel through the text
  for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            encrypted_text_result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            encrypted_text_result += chr((ord(char) + s - 97) % 26 + 97)
 
  return encrypted_text_result


def cipher_decode(text,s):
  s1 = 26 - s
  decrypted_text_result = " "

  #this for loop will travel through the text
  for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            decrypted_text_result += chr((ord(char) + s1 -65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            decrypted_text_result += chr((ord(char) + s1 - 97) % 26 + 97)
 
  return decrypted_text_result

if choice == "encode":
   print("ENCODED MESSAGE: "+ cipher_encode(text = word_encode, s = shift_encode))
else:
   print("DECODED MESSAGE:" + cipher_decode(text = word_encode, s = shift_encode))
