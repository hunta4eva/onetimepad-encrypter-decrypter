"""The keys and the counter for which keys to use are in text files, named 'keys.txt' and 'kcounter.txt' respectively
The last number in the 'kcounter.txt' file is the counter that is used find the corresponding key for encryption
The ciphertext from the onetimepad has 5 digits added to it, the first 4 are the counter for the key and the last is a random digit
The counter is incremented by 1 with every encryption and decryption.  """
"Testing git push"
"third/second test of git push"
"fourth commit"

from random import choice
import onetimepad
import pyperclip

def main():
    while True:
        try:
            menu_choice = input('\n1: Encrypt a message \n2: Decrypt a message \n\nEnter your option: ')
            if int(menu_choice) == 1:
                encrypt(input('\nEnter a message:   \033[92m'))
            if int(menu_choice) == 2:
                decrypt()
        except ValueError:
            print(f"\n\033[91mError:'{menu_choice}' is an invalid option\033[00m")

def half_encrypt(i, number, char_1, char_2, char_3):
    if i == number:
        return choice([char_1, char_2, char_3])
    else:
        return ''

def half_decrypt(i, number, char_1, char_2, char_3):
    if i == char_1 or i == char_2 or i == char_3:
        return number
    else:
        return ''

def half_encrypt_loop(plaintext):
    ciphertext = ''
    for i in plaintext:
        ciphertext += half_encrypt(i,'0','$','<','!')
        ciphertext += half_encrypt(i,'1','&','>',';')
        ciphertext += half_encrypt(i,'2','%','=','(')
        ciphertext += half_encrypt(i,'3','@',')',':')
        ciphertext += half_encrypt(i,'4','+',']','-')
        ciphertext += half_encrypt(i,'5','~',',','?')
        ciphertext += half_encrypt(i,'6','^','|','/')
        ciphertext += half_encrypt(i,'7','{','`','_')
        ciphertext += half_encrypt(i,'8','}','.','}')
        ciphertext += half_encrypt(i,'9',' ',' ',' ')
        if i in 'abcdef':
            ciphertext += i
    return ciphertext

def half_decrypt_loop(ciphertext):
    plaintext = ''
    for i in ciphertext:
        plaintext += half_decrypt(i,'0','$','<','!')
        plaintext += half_decrypt(i,'1','&','>',';')
        plaintext += half_decrypt(i,'2','%','=','(')
        plaintext += half_decrypt(i,'3','@',')',':')
        plaintext += half_decrypt(i,'4','+',']','-')
        plaintext += half_decrypt(i,'5','~',',','?')
        plaintext += half_decrypt(i,'6','^','|','/')
        plaintext += half_decrypt(i,'7','{','`','_')
        plaintext += half_decrypt(i,'8','}','.','}')
        plaintext += half_decrypt(i,'9',' ',' ',' ')
        if i in 'abcdef':
            plaintext += i
    return plaintext

def encrypt(plaintext):
    print('\033[00m')
    k, counter = 0, ''

    with open('kcounter.txt') as get_counter:
        for i in get_counter:
            counter = i
    new_counter = str(int(counter)+1)
    string_counter = counter.rjust(4, '0')

    with open('kcounter.txt','a+') as append_counter:
        append_counter.write(f'\n{new_counter}')
        placeholder = append_counter.read()

    with open('key.txt') as get_key:
        for i in get_key:
            if k == int(counter):
                key = i
            k+=1

    plaintext = onetimepad.encrypt(plaintext, key)
    plaintext += string_counter + str(choice(range(9)))
    ciphertext = half_encrypt_loop(plaintext)
    print(f'Encoded Message:   \033[93m{ciphertext}\033[00m'); pyperclip.copy(ciphertext)

def decrypt():
    k = 0
    ciphertext = pyperclip.paste()
    plaintext = half_decrypt_loop(ciphertext)
    print(f'\nEncoded Message:   \033[93m{plaintext}\033[00m')
    counter = int(plaintext[-5:-1])

    with open('key.txt') as get_key:
        for i in get_key:
            if k == counter:
                key = i
            k += 1
    new_counter = str(counter+1)

    with open('kcounter.txt','a+') as append_counter:
        append_counter.write(f'\n{new_counter}')
        placeholder = append_counter.read()

    plaintext = plaintext[0:len(plaintext)-5]
    plaintext = onetimepad.decrypt(plaintext,key)
    print(f'\nDecoded Message:   \033[92m{plaintext}\033[00m')

if __name__ == '__main__':
    main()
