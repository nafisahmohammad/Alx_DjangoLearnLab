from django.urls import path
from .views import view_book, create_book, edit_book, delete_book

urlpatterns = [
    path("view/", view_book, name="view_book"),
    path("create/", create_book, name="create_book"),
    path("edit/", edit_book, name="edit_book"),
    path("delete/", delete_book, name="delete_book"),
]
