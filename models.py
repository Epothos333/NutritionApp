from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
    food_choice = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)

    def is_it_fattening(self):
        return self.calories >= 100

    def __str__(self):
        return self.food_choice

class Choice(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text