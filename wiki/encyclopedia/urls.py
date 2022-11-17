from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new_page", views.new_page, name="new_page"),
    path("wiki/random", views.random_page, name="random"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/<str:title>/edit", views.edit_page, name="edit_page"),
]
