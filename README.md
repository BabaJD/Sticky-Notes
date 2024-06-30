# Sticky Notes App

A simple yet powerful Django-based sticky notes application that allows you to create, view, update, and delete notes with customizable styling.

## Features

*   Create, read, update, and delete (CRUD) operations for sticky notes.
*   Customizable background colors for each note.
*   Search and filtering functionality to find notes quickly.
*   Sorting options to organize notes by date or title.
*   Responsive design for optimal viewing on different devices.
*   Basic accessibility features for improved usability.

## Technologies Used

*   **Django:** The web framework used to build the application.
*   **Python:** The programming language used for the backend logic.
*   **Bootstrap:** A CSS framework for styling and layout.
*   **HTML, CSS, JavaScript:**  For the frontend structure, styling, and interactions.
*   **SQLite (or your preferred database):** For storing the note data.

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/sticky-notes.git
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv env
    ```

3.  **Activate the Virtual Environment:**
    ```bash
    source env/bin/activate  # Linux/macOS
    .\env\Scripts\activate    # Windows
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser (Optional):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

8.  **Access the App:**
    Open your web browser and go to `http://127.0.0.1:8000/`.