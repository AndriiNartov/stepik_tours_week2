from django.contrib import admin
from django.urls import path

from tours.views import custom_handler404, custom_handler500, departure_view, main_view,  tour_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='index'),
    path('departure/<str:departure>/', departure_view, name='departure'),
    path('tour/<int:id>/', tour_view, name='tour'),
]


handler404 = custom_handler404

handler500 = custom_handler500
