from django.contrib import admin
from django.urls import path

from tours import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('departure/<str:departure>/', views.departure_view),
    path('tour/<int:id>/', views.tour_view),
]
