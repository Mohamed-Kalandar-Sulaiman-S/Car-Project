import datetime
class Customers():
    def __init__(self, name:str , phone_number:int , car_name :str , model_name:str , datOfTestDrive:datetime) -> None:
        self.name = name
        self.phone_number = phone_number
        self.car_name = str(car_name),
        self.model_name = str(model_name) ,
        self.datOfTestDrive=datOfTestDrive
    
        
    def __repr__(self) -> str:
        seq = "\n*************************************\n"
        response = "Customer Name : {0}\nCustomer Phone Number : {1}\nRequested Car name : {2}\nRequested model name:{3}\nRequested Date:{4}".format(self.name, 
                                                                             self.phone_number,
                                                                             self.car_name,
                                                                             self.model_name,
                                                                             self.datOfTestDrive)
        #types = "car name : {0} \n car model :{1}\n".format( type(self.car_name) ,type( self.model_name))

        return seq + response + seq 
    

    


