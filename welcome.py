import logging

import sleep from time

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch

global numbers = [1,2,3,4,5,6,7,8,9,'last', 'hold']

def Intro():

    welcome_msg = render_template('welcome')

    return statement(welcome_msg)


def Explain_Project():


    #prompt for explanation, if yes go to Project_list, elif hold, elif repeat, else break
    prompt_msg = render_template('prompt')

    return statement(prompt_msg)

@ask.intent("AnswerIntent", convert={'reply': int})

def Project_list():

    i = 1
    #use switch statement or it's alternative
    while (i != 0):
        if [reply] == 1:
            msg = render_template('first_project')
            sleep(30)
            Explain_Project()
            return statement(msg)

        elif [reply] == 2:
            msg = render_template('second_project')
            sleep(30)
            Explain_Project()
            return statement(msg)

        elif [reply] == 3:
            msg = render_template('third_project')
            sleep(30)
            Explain_Project()
            return statement(msg)

        elif [reply] == NULL:
            #msg = render_template('wait')
            sleep(30)
            sleep(30)
            Explain_Project()
            return statement(msg)

        elif [reply] == '0':
            msg = render_template('last')
            i = 0

        else:
            #repeat

if __name__ == '__main__':

    app.run(debug=True)
