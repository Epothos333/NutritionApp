from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
    food_choice = models.CharField(max_length=200)
    fats = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    proteins = models.IntegerField(default=0)
    allergen = models.BooleanField(default=False)

    def get_calories(self):
        calories = self.fats * 9 + self.carbs * 4 + self.proteins * 4
        return calories

    def __str__(self):
        return "The food is: " + self.food_choice