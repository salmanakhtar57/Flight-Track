# Airport System - Django Project

This is a Django project that allows users to track flights, their duration, origin and destination, and also add passengers manually. Users can log in and out of their profiles as well.

## Getting Started

To get started with this project, you will need to have Python and Django installed on your system. Once you have these prerequisites, follow these steps:

1. Clone the repository onto your local machine.
2. Open the project in your preferred code editor.
3. In the terminal, navigate to the project directory.
4. Run the following command to install the required packages:
```pip install -r requirements.txt```
5. Run the following command to set up the database:
```python manage.py migrate```
6. Start the development server by running the following command:
```python manage.py runserver```
7. Visit http://127.0.0.1:8000/flights to see the project in action.

## Usage

Once you have the project up and running, you can use the following features:

#### Flights

1. List Flights: On the homepage, you can see a list of flights, their duration, origin, and destination.
2. Add Flight: You can add a new flight by clicking on the "Add Flight" button on the homepage. This will take you to a form where you can enter the flight details.
3. Update Flight: You can update a flight by clicking on the "Update" button next to the flight on the homepage. This will take you to a form where you can edit the flight details.
4. Delete Flight: You can delete a flight by clicking on the "Delete" button next to the flight on the homepage. This will remove the flight from the database.

#### Passengers

1. List Passengers: You can see a list of passengers for a particular flight by clicking on the "View Passengers" button next to the flight on the homepage.
2. Add Passenger: You can add a new passenger for a particular flight by clicking on the "Add Passenger" button on the passengers page. This will take you to a form where you can enter the passenger details.
3. Update Passenger: You can update a passenger by clicking on the "Update" button next to the passenger on the passengers page. This will take you to a form where you can edit the passenger details.
4. Delete Passenger: You can delete a passenger by clicking on the "Delete" button next to the passenger on the passengers page. This will remove the passenger from the database.

#### Authentication
1. Register: Users can register for an account by clicking on the "Register" link. This will take them to a form where they can enter their details.
2. Login: Users can log in to their account by adding username and password. This will take them to a form where they can enter their credentials.
3. Logout: Users can log out of their account by clicking on the "Logout" link in the navbar.

# Contributing

If you want to contribute to this project, please follow these steps:

## Fork the repository.

1. Create a new branch with a descriptive name (git checkout -b my-new-feature).
2. Make your changes.
3. Commit your changes (git commit -am 'Add some feature').
4. Push your changes to your fork (git push origin <your-changes>).
5. Create a pull request.