from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from transformers import pipeline
import question_generator
import jpg_url_to_lines
import process
import main

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET'])
def quizform():
    return render_template('quiz.html', form=request.form)

@app.route('/submit', methods=['POST'])
def submit():
    url = request.form['url']
    session['image_url'] = url
    lines = jpg_url_to_lines.extract_text_from_image(url)
    questions = question_generator.get_questions_dict(lines)
    ai_answers = main.get_answers(questions, url)
    session['questions'] = questions
    session['ai_answers'] = ai_answers
    return redirect(url_for('quizquestions'))

# @app.route('/quiz/questions', methods=['GET', 'POST'])
# def quizquestions():
#     if request.method == 'GET':
#         questions = session.get('questions')
#         if questions:
#             return render_template('quiz.html', questions=questions, url=session.get('image_url'))
#         else:
#             return redirect(url_for('quizform'))
#     else:
#         questions = session.get('questions')
#         if not questions:
#             return redirect(url_for('quizform'))
#         else:
#             answers = {}
#             for question_id in request.form.getlist('question_ids[]'):
#                 answer = request.form.get(question_id)
#                 answers[question_id] = answer
#             session['answers'] = answers
            
#             ai_answers = session.get('ai_answers')
            
#             # Combine user's answers and AI answers for display
#             results = {}
#             for question_id, user_answer in answers.items():
#                 print(question_id)
#                 result = {'question': questions[question_id], 'user_answer': user_answer, 'ai_answer': ai_answers[question_id]}
#                 results[question_id] = result
#             print(results)
            
#             # Store combined answers in session
#             session['results'] = results
            
#             return render_template('quiz_review.html', results=results)

@app.route('/quiz/questions', methods=['GET', 'POST'])
def quizquestions():
    if request.method == 'GET':
        questions = session.get('questions')
        if questions:
            return render_template('quiz.html', questions=questions, url=session.get('image_url'))
        else:
            return redirect(url_for('quizform'))
    else:
        questions = session.get('questions')
        if not questions:
            return redirect(url_for('quizform'))
        else:
            answers = {}
            for question_id in request.form.getlist('question_ids[]'):
                answer = request.form.get(question_id)
                answers[question_id] = answer
            session['answers'] = answers
            
            ai_answers = session.get('ai_answers')
            
            # Combine user's answers and AI answers for display
            results = {}
            for question_id, user_answer in answers.items():
                result = {'question': questions[question_id], 'user_answer': user_answer, 'ai_answer': ai_answers[question_id]}
                results[question_id] = result
            
            return render_template('results.html', results=results)




@app.route('/quiz/grade', methods=['GET''POST'])
def quizgrade():
    results = session.get('results')
    checked_answers = request.form.getlist('checked_answers[]')
    score = 0
    for result in results:
        if result['user_answer'] == result['ai_answer'] and str(result['question']['id']) in checked_answers:
            score += 1
    score_percentage = int((score / len(results)) * 100)
    return redirect(url_for('results', score=score_percentage))


if __name__ == '__main__':
    app.run(debug=True)


 