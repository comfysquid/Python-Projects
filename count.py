largest = None
count = 0
total = 0

while True:
    line = input("Enter a number: \n")
    for i in line:
        if largest is None or i > largest:
            largest == i
        print("Loop: ", i, largest)
        print("Largest: ", largest)
    try:
        line = float(line)
        count = count + 1
        total = total + line
    except:
        if line == "done":
            break
        else:
            print("Invalid input)")
            continue
print({"Count": count, "Total": total, "Minimum": min(line), "Maximum": max(line)})
