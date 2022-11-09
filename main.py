"""the principal page"""
from menu import Menus
#from password_generator import PasswordGenerator,SaveInformation,AplicationInformation
from password_generator import *
menu= Menus()
pagepassword= PasswordGenerator()


while True:
    menu.principal_menu()
    option= input ("seleccione una opcion:")
    if option == "1":
        menu.create_password_menu()
        page = input()
        x=pagepassword.generate_password()
        aplication_information = AplicationInformation(page,x)
        SaveInformation.save_information(aplication_information)
      
    if option == "2":
        print ("ingrese el nombre de la pagina web para ver su contraseña")
        page=input()
        print("roger")
    if option == "3":
        print ("diccionario")
    if option == "4":
        break
