# Restaurant Review System

The Restaurant Review System is a comprehensive Python program designed to facilitate the management, analysis, and tracking of customer reviews for various restaurants. This program is equipped with intuitive classes such as Customer, Review, and Restaurant, all of which seamlessly integrate to empower users to effectively oversee customer feedback and gain valuable insights into restaurant performance.

## Features

### Customer Profiles: 
Create customer profiles with their names.This helps in identifying customers when they write reviews.

### Write Reviews: 
Customers can write reviews for restaurants, including ratings.Each review includes a rating to express their satisfaction with the restaurant.

### Restaurant Statistics: 
Analyze restaurant reviews for unique customers and average ratings.

. Unique Customers: The system effortlessly identifies the unique customers who have contributed reviews for a particular restaurant. This aids in understanding the breadth of customer engagement.

. Average Ratings: The program computes the average star rating for a restaurant based on the collective ratings provided by customers. This consolidated measure serves as a quick reference for gauging restaurant quality.



## installation

1. Clone the repository: git clone https://github.com/kimani56/PYTHONCODECHALLENGE2.git
2. Ensure you have Python (version X.X or higher) installed.
3. Install dependencies using pip install package-name.
4. Navigate to the project directory and execute the program


## usage
CLASSES

a) CUSTOMER
Represents customers and their reviews.

__init__(given_name, family_name): Create a new customer.
full_name(): Get the customer's full name.
num_reviews(): Get the count of customer reviews.

b) REVIEW
Enables customers to write restaurant reviews.

__init__(customer, restaurant, rating): Create a review.
rating(): Get the review's rating.
restaurant(): Get the reviewed restaurant.
customer(): Get the customer who wrote the review.


C) RESTAURANT
Analyze restaurant reviews.

__init__(name): Create a restaurant.
restaurant_name(): Get the restaurant's name.
reviews(): Get reviews for the restaurant.
customers(): Get unique customers who reviewed the restaurant.
average_star_rating(): Calculate the average rating.


## Contributing
Feel free to contribute by opening issues or pull requests. Your input is valued!

## License
This project is licensed under the MIT License.

## author
Gift kimani
  
## Contact
giftkimani86@gmail.com

## FAQ'S
Should you have any queries, suggestions, or feedback pertaining to the project, do not hesitate to reach out.

