from Car import Car
from Customers import Customers

def create_car(name , model , year , type , price  ) -> Car:
    car = Car(name=name , 
              model_name=model,
              year=year,
              type=type,
              price=price)
    return car

def create_cars() ->list:
    CARS = []
    data = [
        {
        "name":"i10",
        "model":"lite",
        "year":2010,
        "type":"HatchBack",
        "price": 520000
        },
        {
        "name":"i10",
        "model":"era",
        "year":2010,
        "type":"HatchBack",
        "price": 570000
        },
        {
        "name":"i10",
        "model":"magna",
        "year":2010,
        "type":"HatchBack",
        "price": 600000
        },
        {
        "name":"i20",
        "model":"asta",
        "year":2010,
        "type":"HatchBack",
        "price": 578000
        },
        {
        "name":"i20",
        "model":"sports",
        "year":2010,
        "type":"HatchBack",
        "price": 690000
        },
        {
        "name":"i20",
        "model":"magna",
        "year":2010,
        "type":"HatchBack",
        "price": 708000
        },
        {
        "name":"verna",
        "model":"S",
        "year":2010,
        "type":"Sedan",
        "price": 790000
        },
        {
        "name":"verna",
        "model":"SX",
        "year":2010,
        "type":"Sedan",
        "price": 856000
        },
        {
        "name":"verna",
        "model":"S+",
        "year":2010,
        "type":"Sedan",
        "price": 890000
        },
        {
        "name":"creta",
        "model":"E",
        "year":2010,
        "type":"SUV",
        "price": 108000
        },
        {
        "name":"creta",
        "model":"S",
        "year":2010,
        "type":"SUV",
        "price": 120000
        }

    ]
    for d in data:
        CARS.append(create_car(d["name"] , d['model'] , d['year'] , d['type'] , d['price']))
    return CARS
    

def print_cars(catalogue:dict)->None:
    print("Cars Available .......")
    for name in catalogue.keys():
        print("Car Name : " , name)
        car_objects = catalogue[name]
        print("Year     : ", car_objects[0].year)
        print("Type     : ", car_objects[0].type)
        print("Variants available are ......")
        for variant in car_objects:
            print("\tModel Name : " , variant.model_name)
            print("\tPrice      : " , variant.price)
        print("********************************************")
    

def get_catalogue_of_cars(CARS:list) ->dict:
    catalogue = {}
    #{"i10":[Car_obj] 
    for car in CARS:
        if car.name not in catalogue.keys():
            catalogue[car.name] = []
            catalogue[car.name].append(car)
        if car.name in catalogue.keys() and car not in catalogue[car.name]:
            catalogue[car.name].append(car)
    return catalogue



l = create_cars()
c = get_catalogue_of_cars(l)
print(c.values())





