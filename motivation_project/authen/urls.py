from django.urls import path

from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('create_profile/', views.add_profile_details_view, name='create_profile'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),
]