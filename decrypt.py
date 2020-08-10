# "CFRLTFBbV0EAVBgDEx9VQBYSTB4fGBVRHB9UXFJfR1dUUwIZFF1BRhYWVVxXHx4SVBZeX1xKRkFU UwIZFFFcUQEWXFBRVFcVX1MfWFBQW1cFFlVcXUwVEklTH0xdVF1RGBZcHh8YFUASEVpQR0sVEklT H0pSXlcVX1MfX1xXFRJJUx9OWlYTFQ4"

import base64

# remove spaces
encrypted = "CFRLTFBbV0EAVBgDEx9VQBYSTB4fGBVRHB9UXFJfR1dUUwIZFF1BRhYWVVxXHx4SVBZeX1xKRkFUUwIZFFFcUQEWXFBRVFcVX1MfWFBQW1cFFlVcXUwVEklTH0xdVF1RGBZcHh8YFUASEVpQR0sVEklTH0pSXlcVX1MfX1xXFRJJUx9OWlYTFQ4="
decoded = base64.b64decode(encrypted)
key = 'ss893822'
encoded = str.encode(key)

decrypted = ""
for i in range(len(decoded)):
    decrypted += chr((encoded[i%len(encoded)]^decoded[i]))

print(decrypted)
# {'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}
