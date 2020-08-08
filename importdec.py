import onetimepad
import pyperclip
import random

key = ''
string_counter = ''
msg = ''
nmsg = ''
flag = 0

def sim_decryp(var, var_1, var_2, var_3):
    global msg; global nmsg; global flag
    if i == var_1 or i == var_2 or i == var_3:
        nmsg += var
    else:
        flag += 1
        

def sim_encryp(var, var_1, var_2, var_3):
    global msg; global nmsg; global flag
    if i == var:
        nmsg += random.choice([var_1, var_2, var_3])
    else:
        flag += 1
        

def decrypt_counter(cipher_text):
    global key
    k = 0
    counter = int(cipher_text[-5:-1])
    cipher = open('key.txt')
    for i in cipher:
        if k == counter:
            key = i
        k += 1
    ncounter = counter + 1
    ncounter = str(ncounter)
    cout = open('kcounter.txt','a+')
    cout.write("\n")
    cout.write(ncounter)
    f = cout.read()
    cipher.close
    cout.close

for i in range(1000):
    nmsg = ''
    f = int(input("\n1: Encrypt a message \n2: Decrypt a message \n\nEnter your option: "))
    
    if f == 1:
        msg = input("\nEnter a message:  ")
        k = 0
        counter = ""
        
        encryp = open('kcounter.txt')
        for i in encryp:
            counter = i
        encryp.close

        scounter = int(counter) + 1
        ncounter = str(scounter)
    
        if len(counter) == 1:
            string_counter = '000' + counter
        if len(counter) == 2:
            string_counter = '00' + counter
        if len(counter) == 3:
            string_counter = '0' + counter
        if len(counter) == 4:
            string_counter = ncounter

        encryp = open('kcounter.txt','a+')
        encryp.write('\n')
        encryp.write(ncounter)
        f = encryp.read()
        encryp.close
        
        k = 0
        
        cipher = open('key.txt')
        for i in cipher:
            if k == int(counter):        
                key = i
            k+=1
        msg = onetimepad.encrypt(msg, key)
        
        msg = msg + string_counter + random.choice(['1','2','3','4','5','6','7','8','0'])

        for i in msg:
            flag = 0

            sim_encryp('0','$','<','!')
            sim_encryp('1','&','>',';')
            sim_encryp('2','%','=','(')
            sim_encryp('3','@',')',':')
            sim_encryp('4','+',']','-')
            sim_encryp('5','~',',','?')
            sim_encryp('6','^','|','/')
            sim_encryp('7','{','`','_')
            sim_encryp('8','}','.','}')
            sim_encryp('9',' ',' ',' ')
            if flag == 10:
                nmsg += i
        
        pyperclip.copy(nmsg)
        print(nmsg)

    elif f == 2:
        nmsg = ''
        msg = pyperclip.paste()
        
        for i in msg:
            flag = 0
            sim_decryp('0','$','<','!')
            sim_decryp('1','&','>',';')
            sim_decryp('2','%','=','(')
            sim_decryp('3','@',')',':')
            sim_decryp('4','+',']','-')
            sim_decryp('5','~',',','?')
            sim_decryp('6','^','|','/')
            sim_decryp('7','{','`','_')
            sim_decryp('8','}','.','}')
            sim_decryp('9',' ',' ',' ')
            if flag == 10:
                nmsg += i
            
        print(nmsg)
        msg = nmsg
        decrypt_counter(msg)
        minus_length = len(msg)-5
        msg = msg[0:minus_length]
        msg = onetimepad.decrypt(msg, key)
        print("\nDecoded Message:  %s"%msg)
    
