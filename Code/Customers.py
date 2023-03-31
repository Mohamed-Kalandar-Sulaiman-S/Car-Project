class Customers():
    def __init__(self, name:str , phone_number:int , car_name :str , model_name:str , datOfTestDrive:str) -> None:
        self.name = name
        self.phone_number = phone_number
        self.car_name = car_name,
        self.model_name = model_name ,
        self.datOfTestDrive=datOfTestDrive
    
        
    def __repr__(self) -> str:
        response = "Customer Name : {0}\nCustomer Phone Number : {1}\nRequested Car name : {2}\nRequested model name:{3}\nRequested Date:{4}".format(self.name, 
                                                                             self.phone_number,
                                                                             self.car_name,
                                                                             self.model_name,
                                                                             self.datOfTestDrive)
        return response
    

    


