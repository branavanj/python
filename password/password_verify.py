import re 

password = input("Entrez votre mot de passe : ")

if len(password) < 8:
    print("Le mot de passe est trop court")
elif not re.search("[a-z]", password):
    print("Le mot de passe doit contenir au moins une lettre minuscule")
elif not re.search("[A-Z]", password):
    print("Le mot de passe doit contenir au moins une lettre majuscule")
elif not re.search("[0-9]", password):
    print("Le mot de passe doit contenir au moins un chiffre")
elif not re.search("[_@$]", password):
    print("Le mot de passe doit contenir au moins un caractère spécial")
else:
    print("Le mot de passe est suffisamment fort")