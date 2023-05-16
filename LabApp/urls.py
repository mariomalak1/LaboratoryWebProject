from django.urls import path
from . import views
urlpatterns = [
    path("", views.all_projects, name="all_projects"),
    path("home", views.home, name="home"),

    path("list_all_labs/", views.list_all_labs, name="list_all_labs"),
    path("add_lab/", views.add_lab, name="add_lab"),
    path("edit_lab/<str:lab_id>/", views.edit_lab, name="edit_lab"),
    path("delete_lab/<str:lab_id>/", views.delete_lab, name="delete_lab"),

    path("list_all_reports/", views.list_all_reports, name="list_all_reports"),
    path("add_report/", views.add_report, name="add_report"),
    path("add_report/<str:lab_id>/", views.add_report, name="add_report"),
    path("edit_report/<str:report_id>/", views.edit_report, name="edit_report"),
    path("delete_report/<str:report_id>/", views.delete_report, name="delete_report"),

    path("add_pc/", views.add_pc, name="add_pc"),
]
