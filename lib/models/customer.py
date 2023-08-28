from .review import Review

class Customer:

    customers = []

    def _init_(self, given_name, family_name):

        self.given_name = given_name
        self.family_name = family_name
     

        Customer.add_customer(self)

    def given_name(self):
        return self.given_name
    
    def set_given_name(self, given_name):
        self.given_name = given_name

    def family_name(self):
        return self.family_name
    
    def set_family_name(self, family_name):
        self.family_name = family_name

    def full_name(self):
        return f'{self.given_name} {self.family_name}'
    
    def num_reviews(self):
        customer_reviews = self._get_customer_reviews()
        return len(customer_reviews)
    
    def _get_customer_reviews(self):
        customer_reviews = [review for review in Review.reviews if review.customer().full_name() == self.full_name()]
        return customer_reviews


    @classmethod
    def all(cls):
        return cls.customers
    
    @classmethod
    def add_customer(cls, customer):
        cls.customers.append(customer)

    @classmethod
    def find_by_name(cls, name):

        found = None
        for customer in cls.customers:
            if customer.full_name() == name:
                found = customer
                break

        return found
    
    @classmethod
    def find_all_by_given_name(cls, name):
        found_names = []
        for customer in cls.customers:
            if customer.given_name == name:
                found_names.append(customer)
        return found_names
            



     
