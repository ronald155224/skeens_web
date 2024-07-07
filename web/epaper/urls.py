# epaper/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('epaper/', views.EPaperView.as_view(), name='epaper'),
    path('thanks/', views.EPaperThanksView.as_view(), name='thanks'),
    path('directthanks/', views.EPaperHomeDirectThanksView.as_view(), name='homedirectthanks'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]