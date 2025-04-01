# Welcome to my sqlalchemy challenge; module 10 submission.

# First, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. Specifically, I used SQLAlchemy ORM queries, Pandas, and Matplotlib.
# I used SQLAlchemy's "create_engine()" function to connect to my SQLite database. Then I used the SQLAlchemy's "automap_base()" function to reflect my tables into classes, and then saved the references to the classes named "station" and "measurement".

![Screenshot 2025-04-01 152129](https://github.com/user-attachments/assets/97b8ec31-a1c2-47e2-bc76-112fff76433a)


# After creating the sesion from Python to the DataBase, I performed a precipitation analysis and then a station analysis by answering the questions in the following two subsections.

Precipitation Analysis:

![Screenshot 2025-04-01 152350](https://github.com/user-attachments/assets/a8b31eb0-a4ce-43b6-a745-af8b5086e4e1)

Station Analysis (Also made sure to close the session after I was done with the analysis):

![Screenshot 2025-04-01 152552](https://github.com/user-attachments/assets/b99a9a0c-e30b-4889-acd5-e38c4085e6e6)


# After completing my initial analysis, I then designed a Flask API based on the queries that I developed and created routes to from Flask to the DataBase.

Importing dependencies and DataBase Setup:

![Screenshot 2025-04-01 153008](https://github.com/user-attachments/assets/4bc4580b-3583-41da-b11c-43b691ab50d3)


Flask Setup and Flask Routes:

![Screenshot 2025-04-01 153214](https://github.com/user-attachments/assets/c8c64603-9077-4515-82eb-b1626dbd0bdf)


Flask Routes (Continued):

![Screenshot 2025-04-01 153402](https://github.com/user-attachments/assets/1038e7d5-5b9b-4850-985d-fcdb6220864a)


# After creating the Flask routes, I returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range


![Screenshot 2025-04-01 153737](https://github.com/user-attachments/assets/2cd8cd91-c7ff-4fd0-be99-400d211d8ecd)


# Thank you for reading my ReadMe!

