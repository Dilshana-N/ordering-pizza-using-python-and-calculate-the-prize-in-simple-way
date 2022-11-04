pizza= {"Smallpizza" : 150,"Mediumpizza": 200,"Largepizza" : 250}
print("How many pizzas do you want ?")
a = int(input("Enter the number of small pizza :"))
b = int(input("Enter the number of medium pizza :"))
c = int(input("Enter the number of large pizza :"))

cost =(a*pizza["Smallpizza"]+b*pizza["Mediumpizza"]+c*pizza["Largepizza"])
print(cost)
