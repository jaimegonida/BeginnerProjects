import pyinputplus as pyip
import random, time

NUMBER_OF_QUESTION = 10
correct_answer = 0

for questionNumber in range(NUMBER_OF_QUESTION):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (questionNumber + 1, num1, num2)

    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
        blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)

    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitExeption:
        print('Out of tries')

    else:
        print('Correct!')
        correct_answer += 1

    time.sleep(1)

print('Score: %s / %s' % (correct_answer, NUMBER_OF_QUESTION))
