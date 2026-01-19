from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import add_book, edit_book, delete_book

urlpatterns = [
    # Existing views
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Authentication views
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

    # Role-based access views
    path("admin-role/", views.admin_view, name="admin_view"),
    path("librarian-role/", views.librarian_view, name="librarian_view"),
    path("member-role/", views.member_view, name="member_view"),

    # Custom permission views (⚠️ checker-required paths)
    path("add_book/", add_book, name="add_book"),
    path("edit_book/", edit_book, name="edit_book"),
    path("delete_book/", delete_book, name="delete_book"),
]





