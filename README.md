# Expense Tracker Application

## Overview

This Python application is an Expense Tracker designed to help users manage their expenses and achieve financial freedom. It allows users to log their expenses, view statistics using pie charts and bar plots, and track their income and expenses over time.

## Libraries Used

The following libraries are used in this application:

1. **tkinter**: This library is used for building the graphical user interface (GUI) of the application.
2. **customtkinter**: This is a custom library that provides additional functionality and styling for tkinter widgets.
3. **PIL (Python Imaging Library)**: This library is used for working with images, specifically for displaying images within the GUI.
4. **psycopg2**: This library is used to interact with PostgreSQL databases. It enables the application to perform database operations such as inserting and retrieving data.
5. **matplotlib**: This library is used for data visualization. It is utilized to create pie charts and bar plots to represent expense data.

## Installation

To run this application, you need to install the required libraries. You can do this using pip, the Python package manager. Run the following command in your terminal or command prompt:

 `pip install tkinter customtkinter Pillow psycopg2 matplotlib`

## Usage

To use the Expense Tracker application:

1. Run the Python script provided.
2. The application will launch, displaying the login page.
3. You can either log in with existing credentials or sign up as a new user.
4. After logging in, you can enter your expenses, including the amount, type, date, and any comments.
5. The application will display a summary of your expenses as well as visualizations such as pie charts and bar plots.
6. You can navigate between different pages using the buttons provided.

## Additional Notes

- Ensure you have a PostgreSQL server running locally with the required database ("Expense Tracker") and user credentials configured as specified in the code.
- Make sure to have the necessary image files ("background.jpg", "download.jpg", "side.png") in the same directory as the Python script, or update the file paths accordingly.
- This application provides a basic framework for an Expense Tracker and can be further expanded with additional features and functionalities as needed.
