from django.urls import path
from . import views

urlpatterns = [
    path('' , views.Reg, name="reg"),
    path('login/' , views.logIn, name="login"),
    path('index/' , views.index, name="index"),

    path('ForWard/' , views.receivData, name="ForWard"),
    path('Left/' , views.receivData, name="Left"),
    path('Stop/' , views.receivData, name="Stop"),
    path('Right/' , views.receivData, name="Right"),
    path('BackWard/' , views.receivData, name="BackWard"),
    path('ForWard_Led/' , views.receivData, name="ForWard_Led"),
    path('backWard_Led/' , views.receivData, name="backWard_Led"),
    path('Power/' , views.receivData, name="Power"),
    path('zmor/' , views.receivData, name="zmor"),

]