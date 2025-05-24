# Expense Tracker - django mini project

**Expense Tracker** is a Django-based web application designed to help users manage personal finances. Authenticated users can create yearly budgets, add monthly entries, input incomes, and categorize expenses. The UI is styled for clarity and ease of use, with secure access to ensure each user can only manage their own data.

---

## Features

- User registration and login
- Year and month based budget creation
- Add income and categorized expenses
- View and update budget amounts
- Data protection: users only see their own data
- Modern responsive design with contextual color usage

## 📚 Project Structure

```bash
expense_tracker/
├── base/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── static/
├── db.sqlite3
├── manage.py

```

Installation

Clone the repository:

```bash
git clone https://github.com/Dmate889/Expense_Tracker.git
cd Expense_Tracker
```

Create virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Apply migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```
Visit in your browser:
http://127.0.0.1:8000


##Usage

- Register / Login
- Create Year → Add Month → Input Salary / Expenses
- Adjust budgets and view categorized expenses

##User Permissions

All financial data is user-specific and isolated. Users cannot access or modify other users' entries.

##Tech Stack

- Python 3.13
- Django 5.2
- SQLite (default DB)
- HTML5 & CSS3