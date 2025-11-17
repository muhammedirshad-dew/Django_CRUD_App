# Employee Management System (Django CRUD)

<img width="677" height="751" alt="image" src="https://github.com/user-attachments/assets/631b4a9b-aa2b-4828-b692-47e7a5f878ab" />
<img width="944" height="780" alt="image" src="https://github.com/user-attachments/assets/449be0ae-3c4b-4c8c-8dea-6500f371430e" />
<img width="1919" height="868" alt="image" src="https://github.com/user-attachments/assets/a20e40a3-c5a7-478f-b47a-1346536d81a2" />
<img width="1896" height="860" alt="image" src="https://github.com/user-attachments/assets/d8325165-147b-4098-bfdb-33ea121dfc4c" />
<img width="1919" height="851" alt="image" src="https://github.com/user-attachments/assets/0add1627-ff5c-4b0e-821d-f2d58da1bda6" />

## Project Description
This is a simple web application built with Django to manage employee records. It provides basic CRUD (Create, Read, Update, Delete) functionalities for employee data, including personal details and profile pictures.

## Features
- **Create:** Add new employee records with details like name, email, contact, and profile picture.
- **Read:** View a list of all employees and their details.
- **Update:** Modify existing employee information.
- **Delete:** Remove employee records from the system.
- User authentication (Login, Signup).
- Profile picture upload and display.

## Technologies Used
- Python
- Django (Web Framework)
- HTML, CSS (Frontend)
- SQLite (Database)

## Setup and Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd <your-repository-name> # e.g., cd CRUD
```
*(Replace `<your-repository-url>` with your actual GitHub repository URL and `<your-repository-name>` with your repository's name)*

### 2. Create and Activate Virtual Environment
Navigate to the `CRUD` directory (where `env` and `myProject` are located).

```bash
# Navigate to the CRUD directory
cd CRUD

# Create a virtual environment (if you haven't already)
python -m venv env

# Activate the virtual environment
# On Windows (PowerShell):
.\env\Scripts\Activate.ps1
# On Windows (Command Prompt):
.\env\Scripts\activate.bat
# On macOS/Linux:
source env/bin/activate
```

### 3. Install Dependencies
Navigate into the `myProject` directory and install the required Python packages.

```bash
# Navigate to the myProject directory
cd myProject

# Install dependencies
pip install -r requirements.txt
```

### 4. Database Migrations
Apply the database migrations to create the necessary tables.

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)
To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

### 6. Run the Development Server
Start the Django development server.

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.

## Usage
- Open your web browser and go to `http://127.0.0.1:8000/`.
- You can sign up for a new account or log in if you have an existing one.
- Navigate through the application to add, view, edit, and delete employee records.
- Access the Django admin panel at `http://127.0.0.1:8000/admin/` using your superuser credentials.

## Project Structure
```
CRUD/
├── env/                  # Python Virtual Environment
└── myProject/            # Django Project Root
    ├── myProject/        # Main Django project settings
    ├── myApp/            # Employee management application
    │   ├── models.py     # Employee model definition
    │   ├── views.py      # Logic for CRUD operations
    │   ├── templates/    # HTML templates
    │   └── static/       # Static files (CSS)
    ├── media/            # Uploaded media files (e.g., profile pictures)
    ├── db.sqlite3        # SQLite database file
    ├── manage.py         # Django's command-line utility
    └── requirements.txt  # Project dependencies
```
