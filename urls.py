from django.conf.urls import url

from . import views

app_name = 'nutrition'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: nutritionCalculator/5/
    url(r'^(?P<food_id>[0-9]+)/$', views.details, name="details"),
    #name is ambiguous
    # ex: nutritionCalculator/5/results/
    url(r'^(?P<food_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: nutritionCalculator/5/vote/
    url(r'^(?P<food_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^add/$', views.add_food, name='add_food'),
    url(r'^generate/$', views.generate_nutrition, name='generate_nutrition')
]