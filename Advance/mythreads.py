import threading 

import time 

# Defining the main function
def myfunction() :
    "Function to be executed"
    print("Start a thread")
    time.sleep(3)
    print("End a thread")
 
#Define an empty list of threads 
threads = []

#Run 5 concurrrent sessions of myfunction()
for i in range(5) :
    th = threading.Thread(target = myfunction)
    th.start() #starting the thread
    threads.append(th)
    
#Waiting fo all threads to terminate    
for th in threads :
    th.join()