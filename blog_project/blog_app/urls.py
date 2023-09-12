from django.urls import path,include
from . import views
import blog_app.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.admin_page, name = 'admins'),
    path('board/', views.board_page , name = 'board'),
    path('client/', views.client_page, name = 'client'),
    path('write/', views.write_page, name = 'write'),
    path('login/', blog_app.views.login, name='login'),
    path('signup/', blog_app.views.signup, name='signup'),
    path('logout/', blog_app.views.logout, name='logout'),
    path("<string:owner_id>/admin", views.admin_page, name="admins"),
    path("<string:owner_id>/post/<int:post_id>", views.post_page, name="post"),
    path("<string:owner_id>", views.client_page, name="client"),
    path("write/", views.write_page, name="write"),
    path("edit/", views.edit_page, name="edit"),
    path("delete/", views.delete_page, name="delete"),
]