from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.admin_page, name = 'admins'),
    path('board/', views.board_page , name = 'board'),
    path('client/', views.client_page, name = 'client'),
    path('write/', views.write_page, name = 'write'),
]