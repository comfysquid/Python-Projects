inp = input("Enter Fahrenheit Temperature: ")
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print("Please enter a number")


inp = input("Enter Celsius Temperature: ")
try:
    cel = float(inp)
    fah = (cel * 9/5) + 32
    print(fah)
except:
    print("Please enter a number")
