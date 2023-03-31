class Car():
    def __init__(self , name:str , model_name:str , year:int , type:str , price:int) -> None:
        """
        Create car object
        """
        self.name = name
        self.model_name = model_name
        self.year = year
        self.type = type
        self.price = price

    def __repr__(self) -> str:
        """
        Print car
        """
        response = "Car Details : \nName:{0}\nModel:{1}\nYear:{2}\nType:{3}\nPrice:{4}\n".format(self.name, 
                                                                                                self.model_name,
                                                                                                self.year,
                                                                                                self.type,
                                                                                                self.price)
        return response


