document.addEventListener("DOMContentLoaded", function() {
    var editor = CodeMirror.fromTextArea(document.getElementById('solution'), {
        lineNumbers: true,
        mode: 'python',
        theme: 'monokai',
        indentUnit: 4,
        tabMode: 'shift',
    });

    function showLoading() {
        document.getElementById('loading-circle').style.display = 'block';
    }

    function hideLoading() {
        document.getElementById('loading-circle').style.display = 'none';
    }

    document.getElementById('get-feedback-button').addEventListener('click', function() {
        var solution = editor.getValue();
        var taskId = document.getElementById('task-id').value;

        showLoading();

        // Submit Code
        fetch('/check-solution', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ task_id: taskId, solution: solution }),
        })
        .then(response => response.json())
        .then(data => {
            hideLoading();
            if (data.correct) {
                document.getElementById('feedback').textContent = 'Korrekt!';
                document.getElementById('feedback').classList.add('text-success');
                document.getElementById('feedback').classList.remove('text-danger');
                document.getElementById('deep-dive-button').disabled = false;  // Aktivieren des Buttons
            } else {
                document.getElementById('feedback').textContent = 'Falsch, bitte versuchen Sie es erneut.';
                document.getElementById('feedback').classList.add('text-danger');
                document.getElementById('feedback').classList.remove('text-success');
            }
            document.getElementById('written-feedback').textContent = data.feedback;

            // API Feedback anzeigen
            var apiFeedback = document.getElementById('api-feedback');
            apiFeedback.textContent = data.feedback;
            apiFeedback.style.display = 'block';
        });

        // Run Code
        fetch('/run-code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: solution }),
        })
        .then(response => response.json())
        .then(data => {
            var output = document.getElementById('output');
            output.textContent = data.output;
            output.style.display = 'block';
        });
    });

    document.getElementById('reset-button').addEventListener('click', function() {
        var originalCode = document.querySelector('textarea[name="solution"]').textContent;
        editor.setValue(originalCode);
        document.getElementById('output').style.display = 'none';
        document.getElementById('api-feedback').style.display = 'none'; // API Feedback ausblenden
        document.getElementById('written-feedback').textContent = ''; // Geschriebenes Feedback löschen
        document.getElementById('feedback').textContent = ''; // Feedback Text löschen
        document.getElementById('deep-dive-button').disabled = true; // Button wieder deaktivieren
    });
});

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