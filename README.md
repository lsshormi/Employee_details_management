# Employee Management System

This project is a Django-based Employee Management System that allows users to manage employee records efficiently. It includes features such as listing employees, adding new employees, editing existing records, searching, sorting, and pagination.

## Features

1. Employee Listing
   - Responsive design for various screen sizes
   - Sortable columns for Name, Email, Mobile, and Date of Birth
   - Pagination for efficient data loading

2. Employee Management
   - Add new employees with photo upload
   - Edit existing employee information
   - Delete employees with confirmation

3. Search Functionality
   - Partial matching for names and email addresses

4. Image Handling
   - Automatic resizing of uploaded employee photos

5. User Interface
   - Bootstrap-based responsive design
   - Date picker for easy date selection

## Technology Stack

- Backend: Django 5.0.2
- Database: SQLite
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Additional Libraries:
  - Pillow 10.2.0 for image processing
  - django-crispy-forms 2.1 for form rendering
  - crispy-bootstrap4 2023.1 for Bootstrap 4 template pack

## Project Structure

```
employee_management/
│
├── employee_management/    # Django project directory
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── employees/              # Django app directory
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   ├── base.html
│   │   ├── employee_list.html
│   │   ├── employee_form.html
│   │   ├── pagination.html
│   │   └── delete_employee.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media/                  # For storing uploaded images
├── requirements.txt
└── manage.py
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/lsshormi/Employee_details_management.git
   cd employee_management
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database and update the `DATABASES` configuration in `settings.py`.

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000`

## Usage

1. Log in to the admin panel using the superuser credentials.
2. Navigate to the Employee Management dashboard.
3. Use the "Add Employee" button to create new employee records.
4. View, edit, or delete existing records from the employee list.
5. Use the search bar to find specific employees.
6. Sort the list by clicking on column headers.

## Future Improvements

- Implement user authentication for the main application
- Add more advanced filtering options
- Integrate with external HR systems
- Implement data export functionality

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
