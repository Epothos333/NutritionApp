from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
    food_choice = models.CharField(max_length=200)
    fats = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    proteins = models.IntegerField(default=0)
    allergen = models.BooleanField(default=False)

    # def calories(self, fats, carbs, proteins):
    #     fat_cals = fats * 9
    #     carb_cals = carbs * 4
    #     protein_cals = proteins * 4
    #
    #     return fat_cals + carb_cals + protein_cals

    def __str__(self):
        return "This food has " + str(self.proteins) + " grams of protein."

class Choice(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text