from django.urls import path, include
from user import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('show/', views.show_user_info),
    path('move/', views.move_script_to_user)
]
