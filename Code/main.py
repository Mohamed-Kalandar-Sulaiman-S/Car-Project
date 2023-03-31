import time
from utility import decorater , clear_screen



def display_user_menu():
    print("User")

def display_admin_menu():
    print("admin")




def get_option():
    try:
        option = int(input("Enter Your Choice :  "))
    except :
        print("Please enter a integer ......")
        time.sleep(2)
        clear_screen()
        option = 0 
        
    finally:        
        return option


def main():
    run = True
    def main_menu():
        print("****************************")
        print("Test Driving Booking CLI")
        print("****************************")
        print("\t1.Login as Customer \n\t2.Login as Admin\n\t3.Exit")
        return get_option()
    while run == True:
        choice = main_menu()
        if choice == 1:
            display_user_menu()
        elif choice ==2:
            display_admin_menu()
        elif choice == 3:
            print("Closing Application.......")
            run = False
            exit()
        elif choice == 0:
            clear_screen()
        else:
            print("Enter choice within range....")
            time.sleep(2)
            clear_screen()

    


if __name__ == '__main__':
    main()