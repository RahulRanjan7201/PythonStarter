class MyRouter(object) :
    "This is a class that describes the functionality of a router"
    def __init__(self, routername, model, serialNumber, ios) :
         self.routername = routername
         self.model = model
         self.serialNumber = serialNumber
         self.ios =ios
         
    def print_router(self, manuf_date) :
        print("The route name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialNumber)
        print("The IOS version is: ", self.ios)
        print("The model and date combines : ", self.model +  manuf_date)
        
myRouter1 =  MyRouter("R1", "2600", "123456", "12.4")
print(myRouter1.print_router("20181010"))   
print(getattr(myRouter1,"ios")) 
setattr(myRouter1, "ios",15)
print(getattr(myRouter1,"ios"))
print(hasattr(myRouter1,"ios1"))
delattr(myRouter1,"ios")
print(hasattr(myRouter1,"ios"))