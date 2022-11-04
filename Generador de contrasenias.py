##########          Generador de contraseñas            ##########
import random
def password_generator():
    password = []
    passw_leng = random.randint(9,16)
    num_of_capital_letters= random.randint(1,(passw_leng-2))
    num_of_lower_case_letters= random.randint(1,(passw_leng-num_of_capital_letters-1))
    num_of_numbers= passw_leng - num_of_lower_case_letters - num_of_capital_letters
    for i in range(num_of_capital_letters):
        password.append(chr(random.randint(65,90)))
    for i in range(num_of_lower_case_letters):
        password.append(chr(random.randint(97,122)))
    for i in range(num_of_numbers):
        password.append(str(random.randint(0,9)))
    random.shuffle(password)    
    print (passw_leng)
    print (num_of_capital_letters)
    print (num_of_lower_case_letters)
    print (num_of_numbers)
    print (num_of_capital_letters + num_of_lower_case_letters + num_of_numbers)    
    password_str= ''.join(password)
    print ("la contraseña es:", password_str)
    
password_generator()

