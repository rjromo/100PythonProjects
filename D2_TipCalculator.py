#Project for day 2

print ("Welcome to the tip calculator")
bill = float(input ("What was the total bill? $"))
people = int(input ("How many people to split the bill? "))
percentage = float(input ("What percentage tip would you like to give? "))
total = float(round((bill + bill*(percentage/100) )/people,2))
print ("Each person should pay ${}".format(total))