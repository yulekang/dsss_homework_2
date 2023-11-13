import random

def randomInteger(startNumber, endNumber):
    """
    Random integer.
    Generate random number between startNumber and endNumber.
    Parameters
    ----------
    startNumber : integer
        The number of the random to be started.
    endNumber : integer
        The number of the random to be ended.
    Returns
    -------
    output : integer
        An integer random between startNumber and endNumber.
    """
    return random.randint(startNumber, endNumber)


def randomOperator():
    """
    Random operator.
    Generate random operator in '+', '-', '*'.
    output : string
        One of the operator in '+', '-', '*'.
    """
    return random.choice(['+', '-', '*'])


def computeByOperator(number1, number2, operator):
    """
    Compute by operator.
    Calculate the result of two number through the given operator.
    Parameters
    ----------
    number1 : integer
        The first number of the calculation.
    number2 : integer
        The second number of the calculation.
    operator : string
        The operator of the calculation.
    Returns
    -------
    formulaString : string
        The formula string of the calculation.
    result : integer
        The result of the calculation.
    """
    formulaString = f"{number1} {operator} {number2}"
    if operator == '+': result = number1 + number2
    elif operator == '-': result = number1 - number2
    else: result = number1 * number2
    return formulaString, result

def math_quiz():
    """
    Generate two random integer and a operator.
    To compute the correct result, and compare to the user answer.
    """
    score = 0
    questionNumber = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # The loop for the questionNumber.
    for _ in range(questionNumber):
        # Get the two number and the operator.
        number1 = randomInteger(1, 10)
        number2 = randomInteger(1, 6)
        operator = randomOperator()

        # Generate the string and result of calculation.
        problem, answer = computeByOperator(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        
        # Get the answer of the user.
        userAnswer = input("Your answer: ")
        try:
            userAnswerInt = int(userAnswer)
        except:
            print("Please input integer!")
        else:
            # Compare the correct result and the answer of the user,then compute the score.
            if userAnswerInt == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{questionNumber}")

if __name__ == "__main__":
    math_quiz()
