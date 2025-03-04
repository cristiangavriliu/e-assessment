document.addEventListener('DOMContentLoaded', function () {
    const taskId = document.getElementById('task-id').value;

    fetch(`/task-details/${taskId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('task-description').textContent = data.description;

            const solutionEditor = CodeMirror.fromTextArea(document.getElementById('task-solution'), {
                lineNumbers: true,
                mode: 'python',
                theme: 'monokai',
                readOnly: true
            });
            solutionEditor.setValue(data.solution);
        });

    document.querySelectorAll('.form-check-input[type="radio"]').forEach(function (radio) {
        radio.addEventListener('mousedown', function (event) {
            if (radio.checked) {
                radio.wasChecked = true;
            } else {
                radio.wasChecked = false;
            }
        });

        radio.addEventListener('click', function (event) {
            if (radio.wasChecked) {
                radio.checked = false;
                radio.wasChecked = false;
            }
        });
    });

    document.querySelectorAll('.question-container').forEach(function (container, index) {
        const textarea = container.querySelector('textarea');
        if (textarea) {
            const codeEditor = CodeMirror.fromTextArea(textarea, {
                lineNumbers: true,
                mode: 'python',
                theme: 'monokai'
            });
            container.codeEditor = codeEditor;
        }

        // Ensure only one radio button is selected per question
        const radioButtons = container.querySelectorAll('.form-check-input[type="radio"]');
        radioButtons.forEach(function (radio) {
            radio.addEventListener('click', function () {
                radioButtons.forEach(function (otherRadio) {
                    if (otherRadio !== radio) {
                        otherRadio.checked = false;
                    }
                });
            });
        });

        container.querySelector('button').addEventListener('click', function () {
            submitAnswer(index, container);
        });
    });
});


function submitAnswer(index, container) {
    let answer;
    const feedback = document.getElementById(`feedback${index + 1}`);
    
    if (container.querySelector('.form-check-input[type="radio"]')) {
        const options = container.querySelectorAll('.form-check-input[type="radio"]');
        options.forEach(option => {
            if (option.checked) {
                answer = option.value;
            }
        });
    } else if (container.querySelector('.form-check-input[type="checkbox"]')) {
        answer = [];
        const options = container.querySelectorAll('.form-check-input[type="checkbox"]');
        options.forEach(option => {
            if (option.checked) {
                answer.push(option.value);
            }
        });
    } else if (container.querySelector('textarea')) {  
        answer = container.querySelector('textarea').value;
    } else if (container.querySelectorAll('input[type="text"]').length > 1) {
        answer = {};
        const inputs = container.querySelectorAll('input[type="text"]');
        inputs.forEach(input => {
            answer[input.name] = input.value;
        });
    } else {
        answer = container.querySelector('input[type="text"]').value;
    }

    const taskId = document.getElementById('task-id').value;

    fetch('/check-deep-dive-answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            task_id: taskId,
            question_index: index,
            answer: answer,
        }),
    })
    .then(response => response.json())
    .then(data => {
        feedback.textContent = data.correct ? 'Richtig!' : 'Falsch, probiere es erneut!';
        
        if (container.querySelector('input[type="text"]')) {
            const inputs = container.querySelectorAll('input[type="text"]');
            inputs.forEach(input => {
                const key = input.name.replace(/[{}]/g, '');
                const correctAnswers = data.correct_answers[key];
                if (correctAnswers.includes(input.value)) {
                    input.style.borderColor = 'green';
                } else {
                    input.style.borderColor = 'red';
                }
            });
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function resetSelection(container) {
    const radioOptions = container.querySelectorAll('.form-check-input[type="radio"]');
    radioOptions.forEach(option => {
        option.checked = false;
    });

    const checkboxOptions = container.querySelectorAll('.form-check-input[type="checkbox"]');
    checkboxOptions.forEach(option => {
        option.checked = false;
    });

    const textInputs = container.querySelectorAll('input[type="text"]');
    textInputs.forEach(input => {
        input.value = '';
        input.style.borderColor = '';
    });

    const codeEditor = container.codeEditor;
    if (codeEditor) {
        codeEditor.setValue('');
    }
}

let startTime = Date.now();
console.log("Start time set:", startTime);

function sendTimeSpent() {
    let endTime = Date.now();
    let timeSpent = (endTime - startTime) / 1000;  // time spent in seconds
    let taskId = document.getElementById('task-id').value;

    console.log("Sending time spent data:", {
        userId: 'test_user',
        taskId: taskId,
        timeSpent: timeSpent
    });

    let data = JSON.stringify({
        userId: 'test_user',
        taskId: taskId,
        timeSpent: timeSpent
    });

    if (navigator.sendBeacon) {
        navigator.sendBeacon('/update-time', data);
    } else {
        fetch('/update-time', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',  // Setzen des richtigen Content-Type Headers
            },
            body: data
        });
    }
}

window.addEventListener('beforeunload', sendTimeSpent);

// Toggle popup menu visibility
function togglePopupMenu() {
    const popupMenu = document.getElementById('popup-menu');
    popupMenu.style.display = popupMenu.style.display === 'block' ? 'none' : 'block';
}

// Close the popup if clicked outside
window.addEventListener('click', function (event) {
    const popupMenu = document.getElementById('popup-menu');
    const button = document.getElementById('floating-button');
    if (!popupMenu.contains(event.target) && !button.contains(event.target)) {
        popupMenu.style.display = 'none';
    }
});