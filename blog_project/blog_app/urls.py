from django.urls import path, include
from . import views

urlpatterns = [
    path("<string:owner_id>/admin", views.admin_page, name="admins"),
    path("<string:owner_id>/post/<int:post_id>", views.post_page, name="post"),
    path("<string:owner_id>", views.client_page, name="client"),
    path("write/", views.write_page, name="write"),
    path("edit/", views.edit_page, name="edit"),
    path("delete/", views.delete_page, name="delete"),
]
