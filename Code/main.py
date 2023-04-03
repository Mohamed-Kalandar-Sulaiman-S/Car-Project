import time
import datetime

from utility import *
from helper import *


#DATABASE - IN MEMORY
CARS = []
CUSTOMERS = []
CATALOGUE = None
#............................................

def display_user_menu()->None:
    clear_screen()
    run = True
    while run:
        print("Customer Menu")
        print("\t1.List out cars available\n\t2.Book test drive \n\t9.Exit Customer Console")
        choice = get_option()
        if choice == 1 :
            print_cars(CATALOGUE)
        elif choice == 2 :
            book_test_drive()
            
        elif choice == 9:
            print("Logging out as Customer....")
            run = False
            break
        else:
            print("Enter choice within range....")
            time.sleep(2)
            clear_screen()



def display_admin_menu()->None:
    run = True
    while run:
        print("Admin Menu")
        print("\t1.Check most test drived cars\n\t2.Print cars available \n\t3.Print Orders \n\t9.Exit Admin Console")
        choice = get_option()
        if choice == 1 :
            most_test_drived_cars()
        elif choice ==2 :
            print_cars(CATALOGUE)
        elif choice ==3:
            print_orders()
        elif choice == 9:
            print("Logging out as Admin....")
            run = False
            break
        else:
            print("Enter choice within range....")
            time.sleep(2)
            clear_screen()


def print_orders():
    for order in CUSTOMERS:
        print(order)



def most_test_drived_cars():
    print("*********************************")
    car_name = input("Enter Car name : ")
    if car_name not in CATALOGUE.keys():
        print("No such car exists ......")
        return
   
    count = dict()
    
    for customer in CUSTOMERS:
        if car_name == customer.car_name[0]:
            if customer.model_name[0] not in count.keys():
                count[customer.model_name[0]] = 1
            else:
                count[customer.model_name[0]] +=1
    print(count)
    most_test_drived_name = None
    most_test_drived_count = 0
    for model in count.keys():
        if count[model] > most_test_drived_count:
            most_test_drived_name = model
            most_test_drived_count = count[model]
    print("Most test drived models : " , most_test_drived_name)
    print("Most test drived model count  : " , most_test_drived_count)
    print("*********************************")



def book_test_drive()->None:
    print("******************* TEST DRIVE BOOKING ************************")
    print("Which car-model you would choose ")
    for car in CATALOGUE:
        print(">> "  , car)
    car_name = input("Enter car name : ")
    if car_name not in CATALOGUE.keys():
        print("Enter valid car name ......")
        clear_screen()
        book_test_drive()
    print("Enter model name : ")
    variants = CATALOGUE[car_name]
    models = []
    for variant in variants:
        print("\t>>>>" , variant.model_name)
        models.append(variant.model_name)
    model_name = input("Enter Model : ")
    if model_name not in models:
        print("Enter valid car model name ......")
        clear_screen()
        book_test_drive()
    name = input("Enter your name : ")
    phone = input("Enter your phone number :")
    dateOfTestDrive = input("Enter date of test drive in this format (DD:MM:YYYY): ")
    def extract_date(date:str)->datetime:
        raw = date.split(":")
        day = int(raw[0])
        month = int(raw[1])
        year = int(raw[2])
        date_obj = datetime.date(year=year , month=month , day=day)
        return date_obj
    dateOfTestDrive = extract_date(date = dateOfTestDrive)
    customer = Customers(name=name , phone_number=phone , car_name=car_name , model_name=model_name,datOfTestDrive=dateOfTestDrive)
    CUSTOMERS.append(customer)
    print("Your Order has been accepted !!!")
    print(customer)
    time.sleep(2)
    clear_screen()


def get_option()->int:
    try:
        option = int(input("Enter Your Choice :  "))
    except :
        print("Please enter a integer ......")
        time.sleep(2)
        clear_screen()
        option = 0 
        
    finally:        
        return option


def main()->None:
    run = True
    def main_menu():
        print("****************************")
        print("Test Driving Booking CLI")
        print("****************************")
        print("\t1.Login as Customer \n\t2.Login as Admin\n\t9.Exit CLI")
        return get_option()
    while run == True:
        choice = main_menu()
        if choice == 1:
            display_user_menu()
        elif choice ==2:
            display_admin_menu()
        elif choice == 9:
            print("Closing Application.......")
            run = False
            exit()
        elif choice == 0:
            clear_screen()
        else:
            print("Enter choice within range....")
            time.sleep(2)
            clear_screen()

    
def setup()->None:
    global CARS , CATALOGUE
    CARS =create_cars()
    CATALOGUE = get_catalogue_of_cars(CARS=CARS)
    

if __name__ == '__main__':
    setup()
    main()


