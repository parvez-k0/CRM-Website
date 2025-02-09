# CRM Website

## Overview
This is a **Customer Relationship Management (CRM) Website** built using **Django**. The project provides a platform to manage customer interactions, track sales, and enhance business productivity. It includes user authentication, data security, and an intuitive dashboard for easy navigation.

## Features
- User Authentication (Login/Signup)
- Customer Data Management
- Sales Tracking and Reports
- Secure Role-Based Access Control
- Interactive Dashboard
- CRUD Operations for Customers and Sales Records
- Responsive UI with Bootstrap

## Tech Stack
- **Backend**: Django, Python
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default) / PostgreSQL (optional)
- **Other Tools**: Django Authentication, Django Admin Panel

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Virtualenv (optional but recommended)

## Steps to Install and Run
### Clone the repository
```git clone https://github.com/parvez-k0/CRM-Website.git```

### Navigate into the project directory
```cd CRM-Website```

### Create a virtual environment (optional but recommended)
```python -m venv venv```

### Activate the virtual environment
### On Windows
```venv\Scripts\activate```
### On macOS/Linux
```source venv/bin/activate```

### Install dependencies
```pip install -r requirements.txt```

### Apply database migrations
```python manage.py migrate```

### Create a superuser (for admin access)
```python manage.py createsuperuser```

### Run the server
```python manage.py runserver```



## Usage
- Admins can log in via `http://127.0.0.1:8000/admin/`.
- Users can register and manage customer information.
- Sales and interactions can be tracked via the dashboard.

## Contributing
If you wish to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

## Contact
For any queries, reach out via [LinkedIn](https://www.linkedin.com/in/mohd-parvez-khan) or email at `your-email@example.com`.
