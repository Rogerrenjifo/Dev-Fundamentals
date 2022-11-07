"""inicio"""
import random
class PasswordGenerator:
    """clase passwordGenerador"""
    def generate_password(self):
        """generate an aleatory password"""
        password = []
        passw_leng = random.randint(9,16)
        num_of_capital_letters= random.randint(1,(passw_leng-2))
        num_of_lower_case_letters= random.randint(1,(passw_leng-num_of_capital_letters-1))
        num_of_numbers= passw_leng - num_of_lower_case_letters - num_of_capital_letters
        for _ in range(num_of_capital_letters):
            password.append(chr(random.randint(65,90)))
        for _ in range(num_of_lower_case_letters):
            password.append(chr(random.randint(97,122)))
        for _ in range(num_of_numbers):
            password.append(str(random.randint(0,9)))
        random.shuffle(password)
        password_str= ''.join(password)
        return password_str

diccionario ={"facebook":"12345678aA","Amazon": "12345678bB"}

salir = False
while salir is False:
    print ("este programa crea y almacena contraseñas para paginas web")
    print ("1. Crear contraseña")
    print ("2. buscar una contraseña")
    print ("3. mostrar todas las contraseñas")
    print ("4. Salir")
    option= input ("seleccione una opcion:")
    if option == "1":
        print ("increse el nombre de la pagina web para generar y guardar la contraseña")
        page = input()
        pagepassword= PasswordGenerator()
        diccionario[page]= pagepassword.generate_password()
    if option == "2":
        print ("ingrese el nombre de la pagina web para ver su contraseña")
        page=input()
        print("pagina: ",page,"contraseña: ", diccionario[page])
    if option == "3":
        print (diccionario)
    if option == "4":
        salir = True
