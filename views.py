from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse

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

def get_food_details(request):
    form_class = FoodForm


    # if request.method == 'POST':
    #     form = FoodForm(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('/thanks/')
    #
    # else:
    #     form = FoodForm()

    return render(request, 'nutritionCalculator/add.html', {'form': form_class})