Restaurant Review System

This is a Python program for managing customer reviews of different restaurants. It includes classes like Customer, Review, and Restaurant to help users keep track of customer feedback.

Features

Customer Profiles: Create customer profiles with their names.
Write Reviews: Customers can write reviews for restaurants, including ratings.
Restaurant Stats: Analyze restaurant reviews for unique customers and average ratings.


Usage

Clone the repository: git clone https://github.com/kimani56/PYTHONCODECHALLENGE2.git
Ensure you have Python (version X.X or higher) installed.
Install dependencies using pip install package-name.
Run the program: python main.py
Classes
Customer
Represents customers and their reviews.

__init__(given_name, family_name): Create a new customer.
full_name(): Get the customer's full name.
num_reviews(): Get the count of customer reviews.
Review
Enables customers to write restaurant reviews.

__init__(customer, restaurant, rating): Create a review.
rating(): Get the review's rating.
restaurant(): Get the reviewed restaurant.
customer(): Get the customer who wrote the review.
Restaurant
Analyze restaurant reviews.

__init__(name): Create a restaurant.
restaurant_name(): Get the restaurant's name.
reviews(): Get reviews for the restaurant.
customers(): Get unique customers who reviewed the restaurant.
average_star_rating(): Calculate the average rating.


Contributing
Feel free to contribute by opening issues or pull requests. Your input is valued!

License
This project is licensed under the MIT License.

author
Gift kimani
  
Contact

giftkimani86@gmail.com