from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),  # welcome/ → home view
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
]
