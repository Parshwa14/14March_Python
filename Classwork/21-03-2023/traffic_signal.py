ts = input("Enter Traffic Signal : ")


if ts == "Red" or ts == "red":
    print("Please Stop")
elif ts == "Green" or ts == "green":
    print("You can Go")
elif ts == "Yellow" or ts== "yellow":
    print("Stop and then Go")
else:
    print("Invalid Input!")