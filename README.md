# Book Management System

A web-based application to manage books with features such as searching, adding to a wishlist, marking books as read, and more. This system is designed for book enthusiasts to keep track of their reading journey.
Techstack includes HTML,BootStrap, jQuery, AJAX, Flask and Elastic

---

## Features
- **Search Books:**
  - Real-time search suggestions powered by fuzzy matching.
  - View detailed information about books.
- **Wishlist Management:**
  - Add books to your wishlist for future reading.
  - Remove books from the wishlist when no longer needed.
- **Read Books List:**
  - Mark books as read and maintain a separate list.
  - Remove books from the "Read" list.
- **Book Catalog Management:**
  - Add new books to the catalog with details like title, author, genre, and rating.
  - Edit or delete existing book records.

---

## Technologies Used

### Front-End
- **HTML5, CSS3**
- **Bootstrap 4.6.2**: Responsive UI components.
- **JavaScript (jQuery)**: Dynamic content and AJAX for seamless interaction.

### Back-End
- **Python**: Server-side logic.
- **Flask**: RESTful API framework.
- **SQLite/PostgreSQL** (or any database): Book data storage.

---

## Installation

### Prerequisites:
1. **Python** installed (v3.7 or later).
2. **Node.js** (optional, if you're using npm for front-end dependency management).
3. **Git** installed.
4. A virtual environment tool such as `venv` or `virtualenv`.

---

### Steps to Set Up Back-End:
1. Clone the repository:
   git clone https://github.com/abhikodi/BookManagementSystem.git cd
2. Set up a Python virtual environment:
   python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate
3. Install the required dependencies:
   pip install -r requirements.txt
4. Run the Flask app:
   flask run 
5. The back-end will be available at:
   http://localhost:5000


---

### Steps to Set Up Front-End:
The front-end is a static web application that communicates with the Flask API.

1. Ensure you have the required files in the `BookManagementSystem` directory:
- `index.html`: Main front-end HTML file.
- JavaScript and CSS files (Bootstrap and jQuery are included via CDN).

2. Open the `index.html` file directly in a browser or serve it locally:
- To open directly:
  - Locate the file in your project directory.
  - Double-click to open it in your browser.
- To serve locally:
  - Use a simple HTTP server, such as Python's built-in server:
    ```
    python -m http.server
    ```
  - Access the front-end at:
    ```
    http://localhost:8000
    ```

3. Ensure the front-end communicates with the back-end:
- Edit the `API_BASE` URL in the `index.html` script section to match your Flask server:
  ```javascript
  const API_BASE = "http://localhost:5000";
  ```

---


## Usage
1. Start the Flask server:
   flask run
2. Open the front-end by loading the `index.html` file in a browser or hosting it locally.
3. Use the navigation menu to:
- Search books.
- Add books to the wishlist.
- Manage read books.
- Add new books to the catalog.

---

   
