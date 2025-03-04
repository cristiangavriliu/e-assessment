import json

# Define the file path as a global constant
FEEDBACK_DATA_FILEPATH = "feedback_data.json"


def load_data():
    try:
        with open(FEEDBACK_DATA_FILEPATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_data(data):
    with open(FEEDBACK_DATA_FILEPATH, 'w') as file:
        json.dump(data, file, indent=4)


def update_feedback(user_id, task_id, question_id, response, attempts):
    data = load_data()

    # Ensure the user exists
    if user_id not in data:
        data[user_id] = {"Tasks": {}}

    # Ensure the task exists for the user
    if task_id not in data[user_id]["Tasks"]:
        data[user_id]["Tasks"][task_id] = {"Questions": [], "TimeTaken": 0}

    question_found = False
    for question in data[user_id]["Tasks"][task_id]["Questions"]:
        if question["QuestionID"] == question_id:
            question_found = True
            # Cumulate attempts
            question["Attempts"] += attempts
            # Update response if new response is true
            if not question["Response"]:
                question["Response"] = response
            break

    if not question_found:
        data[user_id]["Tasks"][task_id]["Questions"].append({
            "QuestionID": question_id,
            "Response": response,
            "Attempts": attempts
        })

    print(f"Updated data for user {user_id}: {data[user_id]}")
    # Save the updated data
    save_data(data)


def update_time_taken(user_id, task_id, time_taken):
    data = load_data()

    # Ensure the user exists
    if user_id not in data:
        data[user_id] = {"Tasks": {}}

    # Ensure the task exists for the user
    if task_id not in data[user_id]["Tasks"]:
        data[user_id]["Tasks"][task_id] = {"Questions": [], "TimeTaken": 0}

    # Cumulate time taken for the task
    data[user_id]["Tasks"][task_id]["TimeTaken"] += time_taken

    print(f"Updated time for user {user_id} for {task_id}")
    # Save the updated data
    save_data(data)


def update_time_taken_per_submit(user_id, task_id, question_id, time_taken, success):
    data = load_data()

    # Ensure the user exists
    if user_id not in data:
        data[user_id] = {"Tasks": {}}

    # Ensure the task exists for the user
    if task_id not in data[user_id]["Tasks"]:
        data[user_id]["Tasks"][task_id] = {"Questions": []}

    # Find or create the question
    question_found = False
    for question in data[user_id]["Tasks"][task_id]["Questions"]:
        if question["QuestionID"] == question_id:
            question_found = True
            # Ensure the Submissions key exists
            if "Submissions" not in question:
                question["Submissions"] = []
            # Append the new submission
            question["Submissions"].append([time_taken, success])
            break

    if not question_found:
        data[user_id]["Tasks"][task_id]["Questions"].append({
            "QuestionID": question_id,
            "Submissions": [[time_taken, success]]
        })

    # Save the updated data
    save_data(data)


# Example content from LA_manager.py
def get_task_data(user_id, task_id):
    with open('feedback_data.json', 'r') as file:
        feedback_data = json.load(file)
    user_data = feedback_data.get(user_id)
    if not user_data or 'Tasks' not in user_data or task_id not in user_data['Tasks']:
        return None
    return user_data['Tasks'][task_id]


def get_all_data():
    data = load_data()
    return data
