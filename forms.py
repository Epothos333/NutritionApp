from django import forms

class FoodForm(forms.Form):
    ingredient_name = forms.CharField(label='Ingredient Name', max_length=100)
    proteins = forms.IntegerField(max_value=100, min_value=0)
    fats = forms.IntegerField(max_value=100, min_value=0)
    carbs = forms.IntegerField(max_value=100, min_value=0)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )