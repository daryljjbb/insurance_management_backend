# core/urls.py
from django.urls import path
from . import views

# core/urls.py
urlpatterns = [
    # This handles GET /api/customers/ (The list you see in your screenshot)
    path('customers/', views.CustomerListCreateView.as_view()),
    path('policies/', views.PolicyListCreateView.as_view()),

    # ✨ ADD THIS LINE: This handles GET /api/customers/1/ (The specific customer)
    path('customers/<int:pk>/', views.CustomerDetailView.as_view()),

    path('login/', views.api_login, name='api_login'),
    path('logout/', views.api_logout, name='api_logout'),
    path('register/', views.api_register, name='api_register'),
    path('me/', views.me, name='me'),
]