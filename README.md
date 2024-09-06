ToDo App
A simple task management web application built using Django. Users can create, edit, view, and delete tasks, with the option to mark tasks as completed or incomplete.

Features
Add, edit, and delete tasks
Mark tasks as completed or incomplete
View task details
Responsive design with a clean UI
Navigation between pages (Home, Task List, About Us)


Installation

1. Clone the repository:
   git clone https://github.com/your-username/todo-app.git
   

2. Navigate to the project directory:
   cd todo-app
   
   
3. Create and activate a virtual environment:
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   

4. Install the required packages:
   pip install -r requirements.txt

   
5. Run migrations:
   python manage.py migrate


6. Start the development server:
   python manage.py runserver

Usage
Visit http://127.0.0.1:8000 in your browser to start using the ToDo App.

File Structure
todo/
│
├── templates/
│   ├── about.html
│   ├── base.html
│   └── home.html
│
├── todo/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── todoapp/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── images/
│   │       └── logo.png
│   ├── templates/todoapp/
│   │   ├── add_task.html
│   │   ├── delete_task.html
│   │   ├── edit_task.html
│   │   ├── task_detail.html
│   │   └── task_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
└── .gitattributes
