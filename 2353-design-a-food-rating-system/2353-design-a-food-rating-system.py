from collections import defaultdict
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_to_ratings = defaultdict(SortedList)
        self.food_to_cuisine = dict()
        self.food_to_rating = dict()
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.cuisine_to_ratings[cuisine].add([-rating, food])
            if food not in self.food_to_cuisine:
                self.food_to_cuisine[food] = cuisine
            if food not in self.food_to_rating:
                self.food_to_rating[food] = rating

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        self.cuisine_to_ratings[cuisine].discard([-self.food_to_rating[food], food])
        self.food_to_rating[food] = newRating
        self.cuisine_to_ratings[cuisine].add([-newRating, food])

    def highestRated(self, cuisine: str) -> str:
        if cuisine in self.cuisine_to_ratings:
            return self.cuisine_to_ratings[cuisine][0][1]
