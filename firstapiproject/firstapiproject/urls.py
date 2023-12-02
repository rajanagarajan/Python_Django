from django.contrib import admin
from django.urls import path
# from .views import home, raja
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('raja/', views.raja),
    path('user/<str:name>/', views.user)
]
