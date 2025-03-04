from flask import Flask, render_template, request, jsonify
import openai
import random
import sys
import io
import re
import time
from tasks import tasks
from deepdive import deepdive_questions
import LA_manager
import json

app = Flask(__name__)
openai.api_key = '0000'
# TODO: Set your OpenAI API key here

# Assuming this dictionary is used to store the start time for each user/task
start_times = {}

# Speicher
generated_feedback = {}


def extract_number_from_code(user_code):
    match = re.search(r'Zahl\s*=\s*(\d+)', user_code)
    if match:
        return match.group(1)
    return None


def check_code(task_id, user_code):
    task = tasks[task_id]
    if "*DeineTestzahl*" in task["solution"]:
        user_number = extract_number_from_code(user_code)
        if user_number is None:
            return False
        user_solution = task["solution"].replace("*DeineTestzahl*", user_number)
    else:
        user_solution = task["solution"]

    # API zur Überprüfung des Codes verwenden
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user",
             "content": f"Check if the following code solves the task correctly:\nTask: {task['description']}\nUser Code:\n{user_code}\nExpected Solution:\n{user_solution}\nIf the user's code is correct and produces the expected output, respond with 'Correct'. Otherwise, respond with 'Incorrect'"}
        ]
    )

    is_correct = response['choices'][0]['message']['content'].strip().lower() == "correct"

    # Output des Benutzer-Codes und des erwarteten Outputs vergleichen
    expected_output = run_code({"code": user_solution})["output"]
    user_output = run_code({"code": user_code})["output"]

    # Output Vergleich einbeziehen
    return is_correct and (user_output.strip() == expected_output.strip())


def get_feedback(task_id, user_code):
    task = tasks[task_id]
    if "*DeineTestzahl*" in user_code:
        user_number = extract_number_from_code(user_code)
        if user_number is None:
            user_number = "eine Zahl"  # Platzhalter, falls keine Zahl extrahiert werden kann
        user_code = user_code.replace("*DeineTestzahl*", user_number)

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant. Answer in German. Give short feedback answers. Don't be too strict with the feedback, the target group is students. Answer with text only and without code blocks. If the answer is wrong, don't say the correct answer directly, but give a hint. If you read *DeineTestzahl* in the solution, then this is just an example and has been replaced by the user with a number, so the value should be entered statically by the user. Do not mention replacing *DeineTestzahl* in the feedback. If the code is correct, do not provide any improvement suggestions."},
            {"role": "user",
             "content": f"Provide feedback on the following code without mentioning anything about replacing variables, placeholders, or testing different numbers:\nTask: {task['description']}\nCode:\n{user_code}"}
        ]
    )
    return response['choices'][0]['message']['content'].strip()


def replace_variables(template, variables):
    for var, values in variables.items():
        value = random.choice(values)
        template = template.replace(f"{{{var}}}", value)
    return template


def generate_feedback_questions(task_id):
    template = deepdive_questions.get(task_id, {})
    questions = template.get("questions", [])
    generated_questions = []
    for index, question in enumerate(questions):
        question_text = question["template"]
        if "variables" in question:
            question_text = replace_variables(question_text, question["variables"])

        correct_answer = question.get("correct_answer")
        if correct_answer is not None:
            if isinstance(correct_answer, list):
                correct_answer = [replace_variables(ans, question.get("variables", {})) for ans in correct_answer]
            else:
                correct_answer = replace_variables(correct_answer, question.get("variables", {}))

        if question["type"] == "single_choice" or question["type"] == "multiple_choice":
            wrong_answers = [replace_variables(ans, question.get("variables", {})) for ans in question["wrong_answers"]]
            all_answers = wrong_answers + ([correct_answer] if isinstance(correct_answer, str) else correct_answer if correct_answer is not None else [])
            all_answers.sort()

            generated_questions.append({
                "question": question_text,
                "type": question["type"],
                "options": all_answers,
                "correct_answer": correct_answer  # Speichern der korrekten Antwort
            })
        elif question["type"] == "freitext":
            generated_questions.append({
                "question": question_text,
                "type": question["type"],
                "answer": question["answer"]
            })
        elif question["type"] == "cloze":
            generated_questions.append({
                "question": question_text,
                "type": question["type"],
                "answers": question["answers"]
            }) 
    generated_feedback[task_id] = generated_questions  # Speichern der generierten Fragen und Antworten
    return generated_questions


def update_feedback(user, task_id, question_index, is_correct, score, max_score):
    # Beispielhafte Logik der Funktion
    print(f"Update Feedback: User: {user}, Task ID: {task_id}, Question Index: {question_index}, Is Correct: {is_correct}, Score: {score}, Max Score: {max_score}")


@app.route('/')
def home():
    task_id = "task1"  # Beispielhaft eine feste Aufgabe auswählen
    task = tasks[task_id]
    return render_template('home.html', task=task['description'], code=task['code'], task_id=task_id)


@app.route('/task/<task_id>')
def task(task_id):
    start_times[("test_user", task_id)] = time.time()
    task = tasks[task_id]
    return render_template('home.html', task=task['description'], code=task['code'], task_id=task_id)


@app.route('/deep-dive/<task_id>')
def deep_dive(task_id):
    questions = generate_feedback_questions(task_id)
    return render_template('deep-dive.html', questions=questions, task_id=task_id)

@app.route('/check-solution', methods=['POST'])
def check_solution():
    data = request.get_json()
    task_id = data['task_id']
    solution = data['solution']
    is_correct = check_code(task_id, solution)
    feedback = get_feedback(task_id, solution)

    # Use LA_manager to increment submission count
    LA_manager.update_feedback("test_user", task_id, 0, is_correct, 1)

    # Calculate the time taken since the task was loaded
    start_time = start_times.get(("test_user", task_id))
    if start_time is None:
        time_taken = 0
    else:
        time_taken = round(time.time() - start_time)
    LA_manager.update_time_taken_per_submit("test_user", task_id, 0, time_taken, is_correct)
    start_times[("test_user", task_id)] = time.time()
    app.logger.debug(f"Time taken for task {task_id}: {time_taken} and was {is_correct}")

    return jsonify(correct=is_correct, feedback=feedback)

@app.route('/check-deep-dive-answer', methods=['POST'])
def check_deep_dive_answer():
    data = request.get_json()
    task_id = data['task_id']
    question_number = data['question_index']
    user_answer = data['answer']

    question_data = generated_feedback[task_id][question_number]
    correct_answers = question_data.get('answers')
    correct_answer = question_data.get('correct_answer')
    answer = question_data.get('answer')
    question_type = question_data['type']

    # Überprüfen, ob die Antwort leer ist
    if question_type in ["freitext", "cloze", "single_choice"]:
        if isinstance(user_answer, str) and not user_answer.strip():
            return jsonify(correct=False, correct_answers=None)
    elif question_type == "multiple_choice":
        if isinstance(user_answer, list) and not user_answer:
            return jsonify(correct=False, correct_answers=None)

    if question_type == "freitext":
        request_message = f"Check the input for its content against the provided answer and determine if it matches in terms of content. if the spelling is a bit different dismiss the spelling mistakes and check if the answer could still be correct. If it matches, respond with 'Correct'. Otherwise, respond with 'Incorrect'.\n\nQuestion: {question_data['question']}\nUser Answer: {user_answer}\nExpected Answer: {answer}"
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": request_message}
            ]
        )
        model_response = response['choices'][0]['message']['content'].strip()
        is_correct = model_response == "Correct"
    elif question_type == "single_choice":
        is_correct = user_answer == correct_answer
    elif question_type == "multiple_choice":
        correct_answer_set = set(correct_answer.split(', ')) if isinstance(correct_answer, str) else set(correct_answer)
        user_answer_set = set(user_answer)
        is_correct = user_answer_set == correct_answer_set
    elif question_type == "cloze":
        is_correct = True
        for key, user_val in user_answer.items():
            key_without_braces = key.replace("{", "").replace("}", "")
            if key_without_braces in correct_answers:
                if user_val not in correct_answers[key_without_braces]:
                    is_correct = False
                    break
            else:
                is_correct = False
                break

    # Use LA_manager to increment submission count
    LA_manager.update_feedback("test_user", task_id, question_number + 1, is_correct, 1)

    return jsonify(correct=is_correct, correct_answers=correct_answers)

@app.route('/task-details/<task_id>', methods=['GET'])
def get_task_details(task_id):
    task = tasks.get(task_id)
    if task:
        return jsonify(description=task['description'], solution=task['solution'])
    else:
        return jsonify(description="Aufgabe nicht gefunden", solution=""), 404


@app.route('/run-code', methods=['POST'])
def run_code(data=None):
    if data is None:
        data = request.get_json()
    code = data['code']
    try:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        exec(code, {})
        sys.stdout = old_stdout
        return {"output": redirected_output.getvalue()}
    except Exception as e:
        return {"output": str(e)}


@app.route('/update-time', methods=['POST'])
def update_time():

    print(f"Request Headers: {request.headers}")
    print(f"Request Data: {request.data}")

    if request.content_type == 'text/plain;charset=UTF-8':
        data = request.get_data(as_text=True)
        data = json.loads(data)
    else:
        data = request.get_json()

    user_id = data['userId']
    task_id = data['taskId']
    time_spent = data['timeSpent']
    
    print(f"Received update-time request: user_id={user_id}, task_id={task_id}, time_spent={time_spent}")

    # Assuming 'update_feedback' is the function that updates your JSON file
    # You might need to adjust this part to correctly update the time spent on a specific question
    LA_manager.update_time_taken(user_id, task_id, time_spent)
    print(time_spent)

    return jsonify(success=True)


@app.route('/assessment')
def assessment():
    data = LA_manager.get_all_data()
    user_data = data.get("test_user", {})
    return render_template('assessment.html', data=user_data, user_id="test_user")

@app.route('/detailed_assessment/<task_id>')
def detailed_assessment(task_id):
    user_id = 'test_user'  # Assuming 'test_user' is the user ID for this example
    task_data = LA_manager.get_task_data(user_id, task_id)

    if not task_data:
        return "Task not found", 404

    return render_template('detailed_assessment.html', task_id=task_id, data=task_data)

    return render_template('detailed_assessment.html', user_id="test_user")

if __name__ == '__main__':
    app.run(debug=True)
