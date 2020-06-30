from cProfile import label

import pyautogui

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
key = 5
new_msg =""
new_m = ""

message = input("Enter your input : ").upper()
for char in message:
    if char in alphabet:
        position = alphabet.find(char)
        new_position = (position + key) % 26
        new_char = alphabet[new_position]
        print("New encrypted character is {}".format(new_char).lower())
        new_msg += new_char
    elif char == " ":
        new_char = "#"
        new_msg +=new_char

print("Encrypted data for processing is {}".format(new_msg).lower())
pyautogui.confirm("you cant decrypt if you are not authentic user")
password = pyautogui.password("Enter your password")
var = "roopam"
if password == var:
    pyautogui.alert("successfully logged")
    for char in new_msg:
        if char in alphabet:
            position = alphabet.find(char)
            new_position = (position - key) % 26
            new_char = alphabet[new_position]
            print("New decrypted character is {}".format(new_char).lower())
            new_m += new_char
        else:
            if  char == "#":
                char = " "
                new_m +=char

print("Decrypted data after processing is '{}'".format(new_m).lower())

