from random import randrange

from django.contrib.auth import get_user_model


def generateLogin(first_name, last_name):
    # verification si il un compte existant deja avec le meme nom et prenom
    User = get_user_model()
    numberOfCompte = User.objects.filter(first_name=first_name).filter(first_name=first_name).count()
    prenoms = last_name.lower().split(" ")
    # le prenom doit etre decoupé au cas ou l'agent en plus d'un. on prendra le dernier
    login = str(prenoms[len(prenoms) - 1]) +'.'+ first_name.lower()
    if numberOfCompte > 0:
        number = numberOfCompte + 1
        login = login +str(number)
    print(login)
    return login


def generatePwd():
    caracteres = "KTNYDAIEU0123456789#@"
    pwd =""
    for i in range(0,7) :
        pwd += caracteres[randrange(0, len(caracteres)-1)]
        #print(pwd)
    return pwd