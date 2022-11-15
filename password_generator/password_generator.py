"""inicio"""
import random
def save_information(page,pagepassword):
    """save information on a register.txt"""
    with open('register.txt','a',encoding="utf-8") as txt:
    #data=f"nombre:{self.page} password {self.password} \n"
        txt.write(f"{page} {pagepassword} \n")
def read_information():
    """read information from registe.txt"""
    with open('register.txt','r',encoding="utf-8") as txt:
        register= txt.readlines()
    return register
def recovery_password(page,register):
    """""filter the data """
    password = [s for s in register if page in s]
    if len(password) != 0:
        pagepassword = password[0].split()
        print ("====================================")
        print (f"la contraseña de {page} es: {pagepassword[1]}")
    else:
        print ("pagina no encontrada")
def generate_password():
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
