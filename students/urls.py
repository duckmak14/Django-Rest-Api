from django.urls import path
from . import views

urlpatterns = [
    path("list", view=views.list_students, name="list students"),
    path("", view=views.StudentView.as_view(), name="student"),
    path("<int:id>", view=views.StudentView.as_view(), name="student"),
    # path("<int:id>", view=views.get_detail, name="student_detail"),
    # path("create", view=views.create, name="create_students"),
    # path("update/<int:id>", view=views.update, name="update_student"),
    # path("delete/<int:id>", view=views.delete, name="delete_student"),
]