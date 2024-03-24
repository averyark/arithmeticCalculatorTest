def getNextNumber(value: str, index):
    numStr = ""

    for char in value[index+1:]:
        if char == ",":
            pass
        elif char.isnumeric():
            numStr = numStr + char
        else:
            break

    if numStr == "": 
        return 0 
    else: 
        return int(numStr)

def getPrevNumber(value: str, index):
    numStr = ""

    for char in value[index-1::-1]:
        if char == ",":
            pass
        elif char.isnumeric():
            numStr = numStr + char
        else:
            break

    if numStr == "": 
        return 0 
    else: 
        return int(numStr[::-1])

# Solving simple arithmetic without using eval
def solveArithmetic(value: str):
    if value == "":
        return
    
    value = value.replace(" ", "")

    tokens = []
    tokens.append(["+", getNextNumber(value, -1), False])

    for i in range(len(value)):
        char = value[i]

        if char in ["/", "*", "+", "-"]:
            if char == "/":
                prevIndex = len(tokens)-1
                lastOccupy = tokens[prevIndex]
                if lastOccupy[2] == True:
                    tokens[prevIndex] = ["+", lastOccupy[1] / getNextNumber(value, i), True]
                else:
                    tokens[prevIndex] = ["+", getPrevNumber(value, i) / getNextNumber(value, i), True]
            elif char == "*":
                prevIndex = len(tokens)-1
                lastOccupy = tokens[prevIndex]
                if lastOccupy[2] == True:
                    tokens[prevIndex] = ["+", lastOccupy[1] * getNextNumber(value, i), True]
                else:
                    tokens[prevIndex] = ["+", getPrevNumber(value, i) * getNextNumber(value, i), True]
            else:
                tokens.append([
                    char,
                    getNextNumber(value, i),
                    False
                ])

    print(tokens)
    sum = 0

    for task in tokens:
        if task[0] == "+":
            sum = sum + task[1]
        elif task[0] == "-":
            sum = sum - task[1]

    print(f"Answer: {sum}")

print("Arithmetic calculator:")

while True:
    solveArithmetic(input("Solve for: "))
    
#solveArithmeticNew("1 + 2 * 3 + 4 * 3")
