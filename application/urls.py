from django.urls import path
from application.views import *


urlpatterns = [
    path('', index, name='home'),
]
