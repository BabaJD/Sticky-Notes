# Sticky Notes App

## Description

This Django-based sticky notes application simplifies your note-taking and organization. It's a versatile tool for quickly jotting down ideas, reminders, or to-do lists. The app boasts customizable styling, search capabilities, and a responsive design for seamless use across devices.

**Key Features:**

* **CRUD Operations:** Easily create, read, update, and delete your notes.
* **Customization:** Personalize each note's background color.
* **Search & Filtering:** Quickly locate specific notes.
* **Sorting:** Organize notes by date or title.
* **Responsiveness:** Optimized for different screen sizes (desktop, tablet, mobile).
* **Accessibility:** Includes basic features for improved usability.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/<your-username>/sticky-notes.git
   ```

2. **Create a Virtual Environment:** (Recommended for isolating project dependencies)

   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment:**

   ```bash
   source env/bin/activate  # Linux/macOS
   .\env\Scripts\activate   # Windows
   ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations:** (Creates the database structure)

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser:** (Optional, for admin access)

   ```bash
   python manage.py createsuperuser
   ```

## Usage

1. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

2. **Access the App:** Open your web browser and navigate to `http://127.0.0.1:8000/`.

**Interacting with the App:**
   
* Click the "Create Note" button to add a new note.
* Edit existing notes by clicking on them.
* Delete notes using the trash icon.
* Customize note colors using the color picker.
* Use the search bar and filters to find specific notes.

## Technologies Used

* **Django:** Web framework 
* **Python:** Programming language
* **Bootstrap:** CSS framework
* **HTML, CSS, JavaScript:** Frontend technologies
* **SQLite (or preferred database):** Data storage

## Credits

* **Author:** Babajide Abraham Alamu

