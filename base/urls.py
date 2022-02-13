from django.urls import path
from . import views

urlpatterns = [
    path('logout', views.logoutUser, name="logout"),
    path('loging', views.loginPage, name="login"),
    path('', views.home, name="home"), #core url, cuando alguien visita el sitio directamente
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
]