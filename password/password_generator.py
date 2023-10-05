#! /usr/bin/env python3
# coding:utf8
import random

caractere = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"

longueur = 15

password_generator = ""

for i in range(longueur):
    password_generator += random.choice(caractere)

print("Le mot de passe généré est  : " + str(password_generator) )
