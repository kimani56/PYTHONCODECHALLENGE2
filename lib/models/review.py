class Review:
    reviews = [] 

    def _init_(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating

        Review.add_review(self)

    def rating(self):
        return self._rating
    
    def restaurant(self):
        return self._restaurant
    
    def rating(self):
        return self._rating
    

    @classmethod
    def all(cls):
        return cls.reviews
    
    @classmethod
    def add_review(cls, review):
        cls.reviews.append(review)
    