import MyRouter
class MyNewRouter(MyRouter) : 
    def __init__(self, routername, model,serialno, ios, portno):
        MyRouter.__init__(self, routername, model, serialno, ios)
        self.portno = portno
    def print_new_router(self, string) : 
        print(string + self.model)
  
new_router1 = MyNewRouter("newr1","1800","11111","12.2","10")
print(new_router1.portno)        