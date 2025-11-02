# Todo Web App

A fully functional Todo List web application built with Django. This app allows users to create, manage, and organize their daily tasks with user authentication.

## Features

✨ **User Authentication**
- User registration with duplicate username validation
- Secure login/logout system
- Session management

📝 **Todo Management**
- Create new todos with title and description
- Mark todos as complete/incomplete
- Edit existing todos
- Delete todos
- View all your todos in one place
- Todos are sorted by creation date (newest first)

🎨 **Modern UI**
- Beautiful gradient design
- Responsive layout for mobile and desktop
- Smooth animations and transitions
- Interactive edit modal
- Font Awesome icons

## Project Structure

```
ToDoList/
├── manage.py
├── db.sqlite3
└── todo/
    ├── models.py          # Database models (ToDo, User)
    ├── views.py           # View functions (signup, login, CRUD operations)
    ├── urls.py            # URL routing
    ├── settings.py        # Django settings
    ├── admin.py           # Admin panel configuration
    ├── templates/
    │   ├── signup.html    # User registration page
    │   ├── login.html     # User login page
    │   └── todo.html      # Main todo list page
    └── static/
        └── todo/
            ├── auth.css   # Styles for login/signup pages
            └── todo.css   # Styles for todo list page
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd F:\Django_project\ToDoList
   ```

2. **Install Django (if not already installed):**
   ```bash
   pip install django
   ```

3. **Run migrations (already done, but for reference):**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage Guide

### Getting Started

1. **Sign Up:**
   - Visit `http://127.0.0.1:8000/signup/`
   - Enter a unique username, email, and password
   - Click "Sign Up"

2. **Login:**
   - Visit `http://127.0.0.1:8000/login/`
   - Enter your username/email and password
   - Click "Login"

3. **Create Todos:**
   - After logging in, you'll see the todo list page
   - Enter a title (required) and description (optional)
   - Click "Add" to create a new todo

4. **Manage Todos:**
   - **Complete/Uncomplete:** Click the circle icon next to a todo
   - **Edit:** Click the "Edit" button, make changes, and save
   - **Delete:** Click the "Delete" button (confirms before deleting)

5. **Logout:**
   - Click the "Logout" button in the header

## Database Model

### ToDo Model
```python
class ToDo(models.Model):
    sno = AutoField (primary key)
    title = CharField (max 200 characters)
    description = TextField (optional)
    completed = BooleanField (default: False)
    date = DateTimeField (auto-created)
    user = ForeignKey (linked to User)
```

## URL Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | login | Home page (redirects to login) |
| `/signup/` | signup | User registration |
| `/login/` | login | User login |
| `/logout/` | logout | User logout |
| `/todo/` | todo_home | View all todos |
| `/todo/add/` | add_todo | Create new todo |
| `/todo/update/<id>/` | update_todo | Edit todo |
| `/todo/delete/<id>/` | delete_todo | Delete todo |
| `/todo/toggle/<id>/` | toggle_todo | Toggle completion |
| `/admin/` | admin | Django admin panel |

## Features in Detail

### Security
- CSRF protection on all forms
- Password hashing
- Login required decorators on protected views
- User-specific todo isolation

### Validation
- Username uniqueness check
- Required field validation
- User-specific data access (users can only see/modify their own todos)

### User Experience
- Success/error messages for all actions
- Smooth animations and transitions
- Responsive design for all screen sizes
- Confirmation before deleting todos
- Form value persistence on errors

## Technology Stack

- **Backend:** Django 5.2.7
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript
- **Icons:** Font Awesome 6.0
- **Authentication:** Django built-in auth system

## Troubleshooting

### Server won't start
```bash
# Make sure you're in the correct directory
cd F:\Django_project\ToDoList

# Check if port 8000 is already in use
# Use a different port:
python manage.py runserver 8080
```

### Static files not loading
```bash
# Make sure DEBUG=True in settings.py
# Verify static files exist in: todo/static/todo/
```

### Database errors
```bash
# Reset migrations (caution: deletes data)
python manage.py flush
python manage.py migrate
```

## Future Enhancements

Potential features to add:
- [ ] Todo categories/tags
- [ ] Due dates and reminders
- [ ] Priority levels
- [ ] Search and filter functionality
- [ ] Todo sharing between users
- [ ] Export todos to CSV/PDF
- [ ] Dark mode toggle
- [ ] Email notifications
- [ ] REST API for mobile apps

## License

This project is open source and available for educational purposes.

## Author

Created as a Django learning project - Todo Web Application

---

**Server Status:** ✅ Running on http://127.0.0.1:8000/

Enjoy organizing your tasks! 📝✨
