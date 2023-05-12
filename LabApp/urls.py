from django.urls import path
from . import views
urlpatterns = [
    path("list_all_labs/", views.list_all_labs, name="list_all_labs")
]
