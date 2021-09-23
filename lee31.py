import random
import json

def getRandomValues():

    values = "yxcvbnmasdfghjklqwertzuiopYXCVBNMASDFGHJKLQWERTZUIOP1234567890*?!#$%&/´"

    random_values = []

    while len(random_values) != 32:

        random_value = random.choice(values)

        if random_value not in random_values:

            random_values.append(random_value)

    return random_values

def get_encryption_key():

    values = getRandomValues()

    encryption_key = ""

    for val in values:

        encryption_key += val

    f = open("encryption_key.txt", "w")

    f.write(encryption_key)

    f.close()

    print("Encryption key saved!")

    print(f"\nYour encryption key is: {encryption_key}\n")

    return encryption_key

def encrypt(data, encryption_key):

    string_separator = encryption_key[10]

    num_separator = encryption_key[31]

    new_string = ""

    tables = [

        {

            "0": encryption_key[0],
            "1": encryption_key[1],
            "2": encryption_key[2],
            "3": encryption_key[3],
            "4": encryption_key[4],
            "5": encryption_key[5],
            "6": encryption_key[6],
            "7": encryption_key[7],
            "8": encryption_key[8],
            "9": encryption_key[9]

        },

        {

            "0": encryption_key[11],
            "1": encryption_key[12],
            "2": encryption_key[13],
            "3": encryption_key[14],
            "4": encryption_key[15],
            "5": encryption_key[16],
            "6": encryption_key[17],
            "7": encryption_key[18],
            "8": encryption_key[19],
            "9": encryption_key[20],

        },

        {
            "0": encryption_key[21],
            "1": encryption_key[22],
            "2": encryption_key[23],
            "3": encryption_key[24],
            "4": encryption_key[25],
            "5": encryption_key[26],
            "6": encryption_key[27],
            "7": encryption_key[28],
            "8": encryption_key[29],
            "9": encryption_key[30],
        }

    ]

    separated_strings = data.split()

    for string in separated_strings:

        for character in string:

            char_code = str(ord(character))

            new_char_string = ""

            for i in char_code:

                random_table = random.choice(tables)

                for key in random_table.keys():

                    if i == key:

                        new_char_string += random_table[key]

            new_string += new_char_string + num_separator

        new_string += string_separator

    return new_string

def decrypt(encrypted_string, encryption_key):

    string_separator = encryption_key[10]

    num_separator = encryption_key[31]

    tables = [

        {

            "0": encryption_key[0],
            "1": encryption_key[1],
            "2": encryption_key[2],
            "3": encryption_key[3],
            "4": encryption_key[4],
            "5": encryption_key[5],
            "6": encryption_key[6],
            "7": encryption_key[7],
            "8": encryption_key[8],
            "9": encryption_key[9]

        },

        {

            "0": encryption_key[11],
            "1": encryption_key[12],
            "2": encryption_key[13],
            "3": encryption_key[14],
            "4": encryption_key[15],
            "5": encryption_key[16],
            "6": encryption_key[17],
            "7": encryption_key[18],
            "8": encryption_key[19],
            "9": encryption_key[20],

        },

        {
            "0": encryption_key[21],
            "1": encryption_key[22],
            "2": encryption_key[23],
            "3": encryption_key[24],
            "4": encryption_key[25],
            "5": encryption_key[26],
            "6": encryption_key[27],
            "7": encryption_key[28],
            "8": encryption_key[29],
            "9": encryption_key[30],
        }

    ]

    separated_strings = encrypted_string.split(string_separator)

    separated_strings.pop()

    new_string = ""

    for string in separated_strings:

        numbers = string.split(num_separator)

        numbers.pop()

        new_character_string = ""

        for num in numbers:

            num_string = ""

            for single_number in num:
            
                for table in tables: 

                    for key in table.keys():

                        if table[key] == single_number:

                            num_string += key

            new_char = chr(int(num_string))

            new_character_string += new_char

        new_string += new_character_string + " "
            
    return new_string

encryption_key = get_encryption_key()

while True:

    option = input("1) Encrypt\n2) Generate new encryption key\n3) Decrypt\n4) Change encryption key\n5) Exit\n\nChoose an option: ")

    if option == "1":

        input_string = input("String you want to encrypt: ")

        encrypted_string = encrypt(input_string, encryption_key)

        print(f"\nEncrypted: {encrypted_string}\n")

    elif option == "2":

        encryption_key = get_encryption_key()

    elif option == "3":

        encrypted_string = input("Encrypted string: ")

        decrypted_string = decrypt(encrypted_string, encryption_key)

        print(f"Decrypted string: {decrypted_string}\n")

    elif option == "4":

        encryption_key = input("New encryption key: ")

    elif option == "5":
    
        break

    else: 

        print("Please choose a valid option\n")