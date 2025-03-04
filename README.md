# E-Learning and Assessment Web Application

This project aims to create an e-learning and assessment web application to help users learn basic coding principles. Users receive a main task prompting them to complete coding exercises, and after successful completion, they can answer some deep dive questions.

## Features

- Task-based coding exercises
- Real-time feedback on coding solutions
- Deep dive questions for further assessment
- Learning analytics and assessment overview

## Image Collection
![img.png](README_IMG/img.png)
![img.png](README_IMG/img.png)

## Important Files

- `app.py`: Main application script
- `deepdive.py`: Script for handling deep dive questions
- `LA_manager.py`: Learning analytics manager script
- `tasks.py`: Script for managing tasks
- `templates/`: HTML templates
- `static/`: Static files (CSS, JS, images)
- `requirements.txt`: List of required packages



## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- Virtualenv

### Cloning the Repository

```bash
git clone <https://gitlab.lrz.de/cristian.gavriliu/e-assessment.git>
cd <repository-directory>
```

## Setting Up the Virtual Environment
1. **Create a virtual environment:**
```bash
python3 -m venv venv
  ``` 
2. **Activate the virtual environment:**
   <br>  On Windows:
   ```bash
      venv\Scripts\activate
   ```
      On macOS and Linux:
   ```bash
      source venv/bin/activate
   ```
3. **Install the required packages:**
```bash
pip install -r requirements.txt
```

4. Freezing the requirements (only neccecary during development to add new requirements to list)
```bash
pip freeze > requirements.txt
```


## Running the Application

```bash
python app.py
```

## Tech Stack

### Frontend

- **HTML5**: Used for structuring the web pages.
- **CSS3**: Used for styling the web pages, including layout, colors, and fonts.
- **JavaScript**: Used to create interactive elements on the web pages.
- **Bootstrap**: Front-end framework for faster and easier web development, providing responsive design and pre-styled components.
- **CodeMirror**: Browser-based text editor implemented in JavaScript, used for creating the code editor interface.

### Backend

- **Python**: Programming language used for backend development.
- **Flask**: Micro web framework for Python, used to build the web application and handle HTTP requests.
- **Jinja2**: Templating engine for Python, used by Flask for rendering HTML templates with dynamic data.

### Data Storage

- **JSON**: Lightweight data interchange format used to store user data and task results.

### Visualization

- **Chart.js**: JavaScript library used for creating interactive charts to visualize data.

### Development Tools

- **virtualenv**: Tool for creating isolated Python environments, ensuring that dependencies are managed on a per-project basis.
- **pip**: Package installer for Python, used to install the required dependencies.
