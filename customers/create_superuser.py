from django.contrib.auth.models import User
from django.http import JsonResponse

def create_temp_superuser(request):
    if User.objects.filter(username="admin").exists():
        return JsonResponse({"message": "Superuser already exists"})

    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="AdminPass123"
    )
    return JsonResponse({"message": "Superuser created"})
