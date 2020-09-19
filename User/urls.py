from django.urls import path
from User import views as user_views
app_name = 'user'

urlpatterns = [
    path('test_index/', user_views.test_index, name='test'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
]

