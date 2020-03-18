# code written by Matthew Quinn

import time
import random
import operator

print('Welcome to Quickmafs by Matthew Quinn.')
print('This game tests your ability to quickly solve math problems.')
print('Please select your difficulty:')
print('[1] Easy')
print('[2] Medium')
print('[3] Hard')
difficulty = input('[4] Extreme\n>>> ').upper()
difficultyloop = 1
while(difficultyloop == 1):
    if difficulty == '1' or difficulty == 'EASY':
        difficulty = 1
        difficultyword = 'Easy'
        difficultyloop = 0
    elif difficulty == '2' or difficulty == 'MEDIUM':
        difficulty = 2
        difficultyword = 'Medium'
        difficultyloop = 0
    elif difficulty == '3' or difficulty == 'HARD':
        difficulty = 3
        difficultyword = 'Hard'
        difficultyloop = 0
    elif difficulty == '4' or difficulty == 'EXTREME':
        difficulty = 4
        difficultyword = 'Extreme'
        difficultyloop = 0
    else:
        difficulty = input('Please enter a valid difficulty.\n>>> ').upper()

def randop(x, y):
    operator = random.randint(0, 3)
    if operator == 0:
        return str(x) + '+' + str(y)
    elif operator == 1:
        return str(x) + '-' + str(y)
    elif operator == 2:
        return str(x) + '*' + str(y)
    elif operator == 3:
        return str(x) + '/' + str(y)

def mathproblem():
    w = random.randint(1, 9)
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    z = random.randint(1, 9)
    subproblem1 = '(' + randop(w, x) + ')'
    subproblem2 = '(' + randop(y, z) + ')'
    return randop(subproblem1, subproblem2)

def answercheck(user, problem):
    w = int(problem[1])
    x = int(problem[3])
    y = int(problem[7])
    z = int(problem[9])
    operator1 = problem[2]
    operator2 = problem[5]
    operator3 = problem[8]
    if operator1 == '+':
        ans1 = operator.add(w, x)
    elif operator1 == '-':
        ans1 = operator.sub(w, x)
    elif operator1 == '*':
        ans1 = operator.mul(w, x)
    elif operator1 == '/':
        ans1 = operator.truediv(w, x)

    if operator3 == '+':
        ans3 = operator.add(y, z)
    elif operator3 == '-':
        ans3 = operator.sub(y, z)
    elif operator3 == '*':
        ans3 = operator.mul(y, z)
    elif operator3 == '/':
        ans3 = operator.truediv(y, z)

    if operator2 == '+':
        answer = operator.add(ans1, ans3)
    elif operator2 == '-':
        answer = operator.sub(ans1, ans3)
    elif operator2 == '*':
        answer = operator.mul(ans1, ans3)
    elif operator2 == '/':
        if ans3 == 0:
            answer = 'UNDEFINED'
            if answer == str(user).upper():
                return True
            return False
        else:
            answer = operator.truediv(ans1, ans3)

    global expected
    expected = round(answer)

    if user == 'UNDEFINED':
        return False
    elif expected == int(user):
        return True
    return False

def round(x):
    if float(x) != int(x) and float(str(x)[str(x).index('.') + 1]) >= 5:
        if x > 0:
            return int(x) + 1
        elif x < 0:
            return int(x) - 1
    return int(x)

print('Difficulty ' + difficultyword + ' has been selected.')
time.sleep(2)
allowedseconds = 11 - 1.5*difficulty
score = 0
print('You have ' + str(allowedseconds) + ' seconds to finish the following math problem.')
time.sleep(2)
print('All answers should be rounded to the nearest whole number. Type "undefined" for any undefined answers.')
time.sleep(2)
input('Press enter to begin.\n>>> ')

while(True):
    error = 0
    expected = 'undefined'
    starttime = time.monotonic()
    thisproblem = mathproblem()
    print(thisproblem)
    user = input('>>> ').upper()

    totaltime = time.monotonic() - starttime
    stringtotaltime = str(totaltime)
    pos = stringtotaltime.index('.')
    formattime = stringtotaltime[:pos+3]

    if user != 'UNDEFINED':
        for x in user:
            if x.isdigit() == False and x != '-':
                answercheck(-82, thisproblem)
                print('That is not a valid answer, it should only be digits. The answer was ' + str(expected) + '. You answered in ' + str(formattime) + ' seconds.')
                score = score - 100
                print('Your score is ' + str(score) + '.')
                input('Press enter to begin the next problem.\n>>> ')
                error = 1
                break
                
    if user == '':
        answercheck(-82, thisproblem)
        print('That is not a valid answer, it should only be digits. The answer was ' + str(expected) + '. You answered in ' + str(formattime) + ' seconds.')
        score = score - 100
        print('Your score is ' + str(score) + '.')
        input('Press enter to begin the next problem.\n>>> ')
        error = 1

    if error == 0 and answercheck(user, thisproblem) == True and totaltime <= allowedseconds:
        print('Correct!')
        score = score + 100 + 25*(difficulty-1)
        print('Your score is ' + str(score) + '. You answered in ' + str(formattime) + ' seconds.')
        input('Press enter to begin the next problem.\n>>> ')

    elif error == 0 and answercheck(user, thisproblem) == True and totaltime > allowedseconds and error == 0:
        print('Ran out of time! However, your answer was correct. You answered in ' + str(formattime) + ' seconds.')
        score = score - 100
        print('Your score is ' + str(score) + '.')
        input('Press enter to begin the next problem.\n>>> ')

    elif error == 0 and answercheck(user, thisproblem) == False and totaltime <= allowedseconds and error == 0:
        print('Incorrect. The answer was ' + str(expected) + '. You answered in ' + str(formattime) + ' seconds.')
        score = score - 100
        print('Your score is ' + str(score) + '.')
        input('Press enter to begin the next problem.\n>>> ')

    elif error == 0:
        print('Ran out of time, and your answer was incorrect. The answer was ' + str(expected) + '. You answered in ' + str(formattime) + ' seconds.')
        score = score - 100
        print('Your score is ' + str(score) + '.')
        input('Press enter to begin the next problem.\n>>> ')
