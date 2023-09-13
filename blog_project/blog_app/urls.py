from django.urls import path, include
from . import views
import blog_app.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.board_page, name="board"),
    path("<slug:category>", views.board_categorized, name="board_categorized"),
    path("post/<int:post_id>", views.post_page, name="post"),
    path("write/", views.write_page, name="write"),
    path("login/", blog_app.views.login, name="login"),
    path("signup/", blog_app.views.signup, name="signup"),
    path("logout/", blog_app.views.logout, name="logout"),
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("delete/<int:post_id>", views.delete, name="delete"),
]
