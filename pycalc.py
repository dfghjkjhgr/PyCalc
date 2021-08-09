print("Welcome to PyCalc!")
while True:
    mathExpression = input(
    "Put in the math problem you want to answer. Type q to quit ")
    parsedMathExpression = mathExpression.split()
    startOfExpression = True
    placeInExpression = 0
    if mathExpression == "q":
        break
    try:
        answer = float(parsedMathExpression[placeInExpression]) 
        + float(parsedMathExpression[placeInExpression + 2])
    except ValueError:
        print("enter in a math problem or type in q to quit")
    except IndexError:
        print("enter in a VALID math problem or type in q to quit")
        continue
    for s in range(len(parsedMathExpression)):
        try:
            if parsedMathExpression[placeInExpression + 1] == "+":
                answer += float(parsedMathExpression[placeInExpression + 2])
                placeInExpression += 2
                startOfExpression = False
            if parsedMathExpression[placeInExpression + 1] == "*":
                answer *= float(parsedMathExpression[placeInExpression + 2])
                placeInExpression += 2
                startOfExpression = False
            if parsedMathExpression[placeInExpression + 1] == "/":
                answer /= float(parsedMathExpression[placeInExpression + 2])
                placeInExpression += 2
                startOfExpression = False
            if parsedMathExpression[placeInExpression + 1] == "-":
                answer -= float(parsedMathExpression[placeInExpression + 2])
                placeInExpression += 2
                startOfExpression = False
        except IndexError:
            try:
             print(f"The answer is {str(answer)}")
             break
            except NameError:
             pass

    
            
            


            

