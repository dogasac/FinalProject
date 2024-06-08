# FinalProject
https://drive.google.com/file/d/1_QNkT608WrWzz3qzA4ptsZNcCiTfHVu8/view

When designing web applications using Flask and integrating HTML, CSS, a common goal is to create a user-friendly, dynamic, and responsive site. Here's a breakdown of the design approach, data model, assumptions, and challenges I would typically encounter in projects like creating a news portal or similar web application:

Data Model
User: This model handles user data and authentication.
Attributes: id, name, surname, email, password, city, country, profile_pic

News: This model stores news articles fetched or inputted into the system.
Attributes: id, title, content, image_url, category, source
The Flask application uses SQLAlchemy for ORM, with SQLite as the backend database. The User and News classes are mapped to database tables.

Assumptions
User Interaction: It's assumed that users interact with the system via a web interface, requiring features like logging in/out, managing profiles, and interacting with news articles.
Dynamic Content: The application dynamically generates content based on user interactions such as searches or filter selections.
Security: Basic security measures are assumed, such as hashing passwords and managing sessions for logged-in users.
Styling: The application uses Bootstrap for styling to ensure the interface is responsive and accessible on various devices.

Problems Encountered
Database Schema Changes: During development, modifications to the database schema (like adding or removing attributes) required careful management to avoid data loss and ensure compatibility.
Dropdown Interaction Without JavaScript: Using CSS for dropdown menus is limited to hover interactions. Implementing click-based dropdowns without JavaScript can be challenging.
