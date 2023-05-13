from django.urls import path
from . import views
urlpatterns = [
    path("list_all_labs/", views.list_all_labs, name="list_all_labs"),
    path("add_lab/", views.add_lab, name="add_lab"),
    path("edit_lab/<str:lab_id>/", views.edit_lab, name="edit_lab"),
    path("delete_lab/<str:lab_id>/", views.delete_lab, name="delete_lab"),
]