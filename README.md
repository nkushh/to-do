# To-Do App - Django REST API with JavaScript Frontend

## Overview

This project is a full-stack to-do application built with Django REST Framework for the backend API and vanilla JavaScript with Bootstrap for the frontend. It was developed to improve my API development skills and JavaScript proficiency.

## Features

- **Task Management**:
  - Create new tasks
  - List all tasks
  - Mark tasks as complete/incomplete
  - Delete tasks

- **API Features**:
  - RESTful endpoints
  - Built with Django REST Framework's generic views
  - JSON responses

- **Frontend Features**:
  - Responsive Bootstrap interface
  - Custom CSS styling
  - JavaScript functions using `fetch()` for API communication
  - Dynamic DOM manipulation

## Technologies Used

### Backend
- Python 3.x
- Django
- Django REST Framework

### Frontend
- Vanilla JavaScript (ES6+)
- Bootstrap 5
- Custom CSS
- Fetch API for HTTP requests

## Installation

### Prerequisites
- Python 3.8+
- Node.js (for frontend dependencies if any)
- pip

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app
2. **Set up a virtual environment (recommended)**
```
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

3. **Install Python dependencies**

```
pip install -r requirements.txt
```

4. **Database setup**

```
python manage.py migrate
```
5. **Run the development server**

```
python manage.py runserver
```

6. **Access the application**

Backend API: http://localhost:8000/

Frontend: http://localhost:8000/

**API Endpoints**
```
Endpoint	Method	Description

/api/tasks/	GET	List all tasks

/api/tasks/	POST	Create a new task

/api/tasks/<id>/	GET	Retrieve a specific task

/api/tasks/<id>/	PUT/PATCH	Update a task (mark as complete/incomplete)

/api/tasks/<id>/	DELETE	Delete a task
```

**Project Structure**

text
```todo-app/
├── backend/               # Django project files
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL routing
│   └── ...
├── todo/                  # Todo app
│   ├── models.py          # Task model
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── urls.py            # App URL routing
│   └── ...
├── static/                # Static files
│   ├── css/
│   │   ├── styles.css     # Custom CSS
│   │   └── ...
│   └── js/
│       ├── main.js        # Main JavaScript file
│       └── ...
├── templates/             # HTML templates
│   └── base.html          # Base template
├── requirements.txt       # Python dependencies
└── README.md              # This file
```
All API interactions use the fetch() API with proper error handling.


**Future Improvements**

- Task categories/tags

- Due dates and reminders

- Drag-and-drop task ordering
