from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse

from .models import Food

def index(request):
    latest_food_list = Food.objects.order_by('-calories')[:5]
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