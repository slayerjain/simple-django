# Django + Django REST Framework Sample Project

This is a simple Django project that includes:

- A **Book** model with fields for `title`, `author`, and `published_date`.
- **Django REST Framework** for API endpoints (list, create, retrieve, update, delete).
- Basic **template-based views** (ListView, DetailView) to display a minimal UI.

---

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Migrations](#database-migrations)
  - [Creating a Superuser](#creating-a-superuser)
  - [Running the Server](#running-the-server)
- [Usage](#usage)
  - [Admin Panel](#admin-panel)
  - [UI (Template) Views](#ui-template-views)
  - [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

---

## Getting Started

### Prerequisites

- **Python 3.7+** (or any later version)
- **pip** (Python package installer)

*(Optional)* It’s best practice to use a virtual environment to isolate dependencies.  
You can use [venv](https://docs.python.org/3/library/venv.html) or [virtualenv](https://pypi.org/project/virtualenv/) to do so.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/slayerjain/simple-django.git
   ```

2.	Navigate into the project folder:
```
cd simple-django
```


3.	(Optional) Create and activate a virtual environment:
```
python -m venv venv
```

#### macOS/Linux
```
source venv/bin/activate
```

#### Windows
```
venv\Scripts\activate
```


4.	Install the dependencies:

```
pip install -r requirements.txt
```


### Database Migrations

Run the following commands to set up the local database and apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```

### Creating a Superuser

If you want to access the Django admin panel, create a superuser account:
```

python manage.py createsuperuser
```

Follow the prompts to create your admin credentials.

### Running the Server

Start the Django development server:
```

python manage.py runserver
```

You can now view the project at http://127.0.0.1:8000/.

### Usage

#### Admin Panel

Access the admin site at:

http://127.0.0.1:8000/admin/

Log in with the superuser credentials you created. From here, you can manage Book objects (create, update, delete).

#### UI (Template) Views

- **Book List Page**: http://127.0.0.1:8000/books/  
    Displays a list of all books in the database.
- **Book Detail Page**: http://127.0.0.1:8000/books/<id>/  
    Displays details of a specific book by its ID (replace `<id>` with a valid integer).

#### API Endpoints

Using the Django REST Framework, you can also interact with the database via RESTful API calls:

1. **List & Create**:
     - **Endpoint**: `GET /api/books/`  
         Returns a JSON list of all books.
     - **Endpoint**: `POST /api/books/`  
         Creates a new book (requires JSON data in the request body, e.g. `{"title": "...", "author": "...", "published_date": "YYYY-MM-DD"}`).

2. **Retrieve, Update & Delete**:
     - **Endpoint**: `GET /api/books/<id>/`  
         Retrieves a single book by its ID.
     - **Endpoint**: `PUT /api/books/<id>/` or `PATCH /api/books/<id>/`  
         Updates an existing book by its ID.
     - **Endpoint**: `DELETE /api/books/<id>/`  
         Deletes the specified book by its ID.

### Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add some feature"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Create a Pull Request

### License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as per the license terms.


