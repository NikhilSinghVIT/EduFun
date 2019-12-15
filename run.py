from flask import Flask,render_template
import random

app = Flask('__main__')

app.config['SECRET_KEY'] = '545fb2177c820f95a09d3eadcfa9dbaf'

@app.route('/')
def questions():
    questions = [{
                    'qid': 'q1',
                    'question':'When was Battle of Panipat held?',
                    'options':['1923','2321','3231','2221'],
                    'correct':'1923'
                },
                {
                    'qid': 'q2',
                    'question':'When was Battle of Panipat held?',
                    'options':['1923','2321','3231','2221'],
                    'correct':'1923'
                },
                {
                    'qid': 'q3',
                    'question':'When was Battle of Panipat held?',
                    'options':['1923','2321','3231','2221'],
                    'correct':'1923'
                },
                {
                    'qid': 'q4',
                    'question':'When was Battle of Panipat held?',
                    'options':['1923','2321','3231','2221'],
                    'correct':'1923'
                },
                {
                    'qid': 'q5',
                    'question':'When was Battle of Panipat held?',
                    'options':['1923','2321','3231','2221'],
                    'correct':'1923'
                }]                    

    return render_template('question.html', questions=questions)

    

if __name__ == '__main__':
    app.run(debug=True)
