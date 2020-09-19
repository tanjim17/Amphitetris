from django.urls import path
from . import views as home_views
app_name = 'home'

urlpatterns = [
    path('', home_views.homepage, name='main-page'),
    path('about/', home_views.about_page, name='about')
]