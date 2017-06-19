alphabet = "abcdefghijklmnopqrstuvwxyz"

# Encryption code.
def encrypt():
    cipher = ''
    input_key = input("Enter your desired key value: ")
    key = int(input_key)    
    encrypt = input("Enter the phrase you wish to encrypt: ").lower()
    for c in encrypt:
        if c in alphabet:
            cipher += alphabet[(alphabet.index(c)+key)%(len(alphabet))]
        else:
            cipher += c 
    print("Your message: " + cipher)

# Decryption code.
def decrypt():
    cipher = ''
    input_key = input("Enter your desired key value: ")
    key = int(input_key)    
    decrypt = input("Enter the phrase you wish to decrypt: ").lower()
    for c in decrypt:
        if c in alphabet:
            cipher += alphabet[(alphabet.index(c)-key)%(len(alphabet))]
        else:
            cipher += c
    print("Your message: " + cipher)

# Quit code.
def quit():
    print("Goodbye!")
    
# Main program loop.
print("Welcome to the Encrypt and Decrypt Machine 2000!")
done = False
while not done:
    user_input = input("Enter 'e' for encryption, \nEnter 'd' for decryption, \nEnter 'q' to quit. \n").lower()
    if user_input == "e":
        encrypt()
    elif user_input == "d":
        decrypt()
    elif user_input == "q":
        quit()
        done = True


