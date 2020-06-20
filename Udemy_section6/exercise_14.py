"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
n = 0
finalScore = 0
questionsAndAnswers = open('questions.txt', 'r')
questions = [line.strip() for line in questionsAndAnswers.readlines()]
questionsAndAnswers.close()

for q in questions:
    separate = q.split('=')
    print(separate[0] + '=')
    answerFile = separate[1]

    answerUser = input("Enter the answer: ")
    if answerFile == answerUser:
        n = n +1
    finalScore = n/len(questions)

resultScore = open('result.txt', 'w')
resultScore.write('Your final score is {}'.format(finalScore))
resultScore.close()
