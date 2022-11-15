"""the principal page"""
import menu
import password_generator
if __name__ == "__main__":
    while True:
        option=menu.principal_menu()
        if option == "1":
            page = menu.create_and_generate_password_menu()
            pagepassword = password_generator.generate_password()
            password_generator.save_information(page,pagepassword)
        if option == "2":
            page = menu.create_and_generate_password_menu()
            register= password_generator.read_information()
            password_generator.recovery_password(page,register)
        if option == "3":
            break
