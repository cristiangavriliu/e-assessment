# E-Learning and Assessment Web Application

## Project Overview
This project was developed as part of a Group Project during the **E-Assessment and E-Learning** course at **Ludwig Maximilian University of Munich (LMU)** in the **Summer Semester of 2024**. The goal of this project is to build an interactive **e-learning and assessment web application** that facilitates learning basic coding principles.

## Features

- **Task-based coding exercises**: Users are given coding challenges to complete.
- **Real-time feedback**: Instant evaluation of coding solutions.
- **Deep dive questions**: Follow-up questions to enhance learning.
- **Learning analytics**: Visual representation of progress and performance.

## Image Collection

![img.png](README_IMG/S1.png)

## Tech Stack

### Frontend

- **HTML5**: Page structure.
- **CSS3**: Styling (layout, colors, fonts).
- **JavaScript**: Interactive elements.
- **Bootstrap**: Responsive UI components.
- **CodeMirror**: JavaScript-based code editor.

### Backend

- **Python**: Backend development.
- **Flask**: Web framework for handling requests.
- **Jinja2**: Template rendering engine.

### Data Storage

- **JSON**: Storing user data and task results.

### Visualization

- **Chart.js**: Interactive data visualization.

### Development Tools

- **virtualenv**: Isolated environment management.
- **pip**: Dependency installation.

## Important Files

- `app.py`: Main application script.
- `deepdive.py`: Handles deep dive questions.
- `LA_manager.py`: Learning analytics management.
- `tasks.py`: Manages coding tasks.
- `templates/`: HTML templates.
- `static/`: CSS, JavaScript, images.
- `requirements.txt`: List of dependencies.

## Setup Instructions

### Prerequisites

- **Python 3.6+**
- **Virtualenv**

### Cloning the Repository

```bash
git clone <https://gitlab.lrz.de/cristian.gavriliu/e-assessment.git>
cd <repository-directory>
```

### Setting Up the Virtual Environment

1. **Create a virtual environment:**

```bash
python3 -m venv venv
```

2. **Activate the virtual environment:**

   - **Windows:**

   ```bash
   venv\Scripts\activate
   ```

   - **macOS/Linux:**

   ```bash
   source venv/bin/activate
   ```

3. **Install required packages:**

```bash
pip install -r requirements.txt
```

4. **Freeze dependencies (for development use only):**

```bash
pip freeze > requirements.txt
```

## Running the Application

```bash
python app.py
```

