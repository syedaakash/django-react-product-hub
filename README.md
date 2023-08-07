# Django-React Product Hub

Welcome to the Django-React Product Hub application! This project is aimed at creating a platform where users can authenticate,
search for items, and make selections, with all changes being stored in an SQLite database.

## Features

- User Authentication: Allow users to register and log in securely.
- Item Search: Enable users to search for items within the application.
- Selection Management: Allow users to select items and manage their choices.
- Database Storage: Store user selections and other relevant information in an SQLite database.

## Setup

1. Clone the repository to your local machine:
    git clone https://github.com/syedaakash/django-react-product-hub.git
2. Navigate to the project directory:
    cd product_hub
3. Set up the Django backend:
  - Install required Python packages:
     pip install -r requirements.txt
  - Apply database migrations:
    python manage.py migrate
  - Run the development server:
    python manage.py runserver
4. Set up the React frontend:
  - Navigate to the frontend directory:
    cd frontend
  - Install Node.js dependencies:
    npm install
  - Start the React development server:
    npm start
    
