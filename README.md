# Phone_Number_Scanner
prototype - numbers are manually inputed 
# Scam Number Checker App

This is a simple Kivy-based application that connects to a MongoDB database to check if a phone number is listed as a scam. The app allows users to insert sample data into the database and check phone numbers.

## Features

- Insert sample phone numbers into a MongoDB collection.
- Check if a phone number is listed as a scam.
- Display results in a popup message.

## Requirements

- Python 3.x
- Kivy
- pymongo
- MongoDB

## Installation

1. **Install the required Python packages:**

	```sh
	pip install kivy pymongo
	```

2. **Ensure MongoDB is installed and running:**

	- Download and install MongoDB from the [official MongoDB website](https://www.mongodb.com/try/download/community).
	- Start the MongoDB server by running the following command in a terminal:

  	```sh
  	mongod
  	```

## Usage

1. **Run the application:**

	```sh
	python scam_number_checker.py
	```

2. **Using the application:**

	- **Create Collection:** Click the "Create Collection" button to insert sample data into the MongoDB collection.
	- **Check Number:** Enter a phone number in the format `xxx-xxx-xxxx` and click the "Check Number" button to see if the number is listed as a scam.

## Code Overview

The application is built using the Kivy framework for the GUI and pymongo to interact with MongoDB. Here are the main components:

- **ScamNumberCheckerApp:** The main application class that sets up the Kivy UI.
- **create_collection:** Inserts sample data into the MongoDB collection.
- **check_number:** Checks if a given phone number is listed in the MongoDB collection.
- **show_popup:** Displays the results in a popup message.

## MongoDB Setup

Ensure that the MongoDB server is running on `localhost:27017`. The app connects to a MongoDB database named `scam_numbers` and a collection named `numbers`. The sample data includes the following phone numbers:

- `123-456-7890`
- `987-654-3210`
- `555-123-4567`

<img width="632" alt="Capture" src="https://github.com/rich-kwk/Phone_Number_Scanner/assets/118232144/cbdf56be-ea60-446f-8751-489990e45b8b">
<img width="623" alt="Capture2" src="https://github.com/rich-kwk/Phone_Number_Scanner/assets/118232144/96bea79e-806e-4aaf-9a1e-b98687d47116">


