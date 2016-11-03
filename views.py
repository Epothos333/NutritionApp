from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from .models import Food
from .forms import FoodForm


def index(request):
    latest_food_list = Food.objects.all()[:5]
    context = {'latest_food_list': latest_food_list}
    return render(request, 'nutritionCalculator/index.html', context)


def details(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    return render(request, 'nutritionCalculator/detail.html', {'food': food})


def results(request, food_id):
    response = "You're looking at the results of food id %s"
    return HttpResponse(response % food_id)


def vote(request):
    return HttpResponse("You're not voting because You haven't registered to my lfie")


def add_food(request):
    form_class = FoodForm()

    ingredient_name = request.POST.get(
        'ingredient_name'
        , '')
    fats = request.POST.get(
        'fats'
        , '')
    carbs = request.POST.get(
        'carbs'
        , '')
    proteins = request.POST.get(
        'proteins'
        , '')

    newFood = Food(food_choice=ingredient_name, fats=fats, proteins=proteins, carbs=carbs);
    newFood.save()

    # Food Constructor? then save?

    return render(request, 'nutritionCalculator/add.html', {'form': form_class})


def generate_nutrition(request):
    food_list = Food.objects.all()[:5]
    fat_list = []
    carb_list = []
    protein_list = []

    for food in food_list:
        fat_list.append(food.fats)
        carb_list.append(food.carbs)
        protein_list.append(food.proteins)

    context = {'food_list': food_list,
               'calories': 100,
               'fat_list': fat_list,
               'carb_list': carb_list,
               'protein_list': protein_list}
    return render(request, 'nutritionCalculator/generate.html', context)
