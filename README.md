# Rate My Professor CCSU

Rate My Professor CCSU is a web application built using Django to allow students of Central Connecticut State University (CCSU) to review and rate their favorite professors. This project provides a platform for students to share their experiences and help others make informed decisions about their course selections.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (sign up, login, logout)
- Add, edit, and delete professor reviews
- Rate professors on various criteria
- Search for professors by name or department
- View average ratings and detailed reviews for each professor

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite (default database, can be replaced with PostgreSQL or MySQL)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/rate-my-professor-ccsu.git
    cd rate-my-professor-ccsu
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000` to see the application running.

## Usage

- Sign up for an account or log in if you already have one.
- Search for professors using the search bar.
- Click on a professor's name to view their profile and reviews.
- To add a review, navigate to the professor's profile and click "Add Review".
- Fill out the review form, including ratings for different criteria.
- Submit the review and it will be visible on the professor's profile.

## Project Structure

# Home
![rmpccsu](https://github.com/mrjasonwalton00/RateMyProfessor/assets/114825896/8a1b6c4a-a0a2-4d56-95f2-a73bfe02adce)

# Professor Page
![Screenshot 2024-05-18 at 4 44 37 PM](https://github.com/mrjasonwalton00/RateMyProfessor/assets/114825896/73659346-01d0-4768-a0b2-f9807e8a74ef)

# Review Page
![Review Page](https://github.com/mrjasonwalton00/RateMyProfessor/assets/114825896/abb8b77c-1757-4f06-b824-fb94697f1e12)

# Sign Up Page
<img width="927" alt="sign up" src="https://github.com/mrjasonwalton00/RateMyProfessor/assets/114825896/0874339f-bc2e-4d2b-af00-65d8dacf51b1">

# Login Page
<img width="943" alt="login" src="https://github.com/mrjasonwalton00/RateMyProfessor/assets/114825896/fafe28e5-fdba-4820-9969-6f382127fec8">

