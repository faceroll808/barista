





print("Hello, welcome to js Coffee!!!!")

name = input ("What is your name?\n")
print ("Hello " + name + ",thank you so much for coming in today. \n\n\n")

menu= " Black Coffee, Espresso, Latte, Cappuchino"

print(name + " What would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()
price = 8.25
quantities =input("how many would you like ?\n")
total = int(quantities) * price
print(f'Great your total is: ${total}')
print("Welp sounds good " + name + ", we'll have that " + order + " ready for you in a moment." )
