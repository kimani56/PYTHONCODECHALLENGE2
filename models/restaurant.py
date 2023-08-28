from models.review import Review

class Restaurant:

    def __init__(self, name):
        self._name = name

    def restaurant_name(self):
        return self._name
    
    def reviews(self):
        return[review for review in Review.reviews if review.restaurant().name() == self._name]
    
    def customers(self):
        unique_customers = set([reviews.customer()for reviews in self.reviews()])
        return unique_customers
    
    def average_star_rating(self):

        restaurant_review = self.reviews()
        average = sum([review.rating() for review in restaurant_review]) / len(restaurant_review)
        return average
