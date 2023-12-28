
print("Welcome to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    message = input("Enter your message:")
    key = int(input("Enter key(1-94):"))

    encrypted_text = ""
    for i in range(len(message)):
        temp = (ord(message[i]) + key) 
        
        if(temp > 126):
            temp = temp - 127 + 32
        
        encrypted_text += chr(temp)
    print("Encrypted " + encrypted_text)
    main()

def decryption():
    emessage = input("Enter encrypted text:")
    dkey = int(input("Enter key(1-94):"))

    decrypted_text= ""
    for i in range(len(emessage)):
        dtemp = (ord(emessage[i]) - dkey)

        if (dtemp < 32):
            dtemp = dtemp + 127 - 32
        
        decrypted_text += chr(dtemp)
    print("Decrypted " + decrypted_text)

if __name__ == "__main__":
    main()
