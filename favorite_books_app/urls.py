from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('create_book', views.createbook),
    path('add_to_favorites/<int:book_id>', views.addtofavorites),
    path('show_book/<int:book_id>', views.showbook),
    path('show_book/update_book/<int:book_id>', views.updatebook),
    path('delete_book/<int:book_id>', views.deletebook),
    path('unfavorite_book/<int:book_id>', views.unfavoritebook),
]


