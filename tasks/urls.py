from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import (
    dashboard, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, 
    CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete,
    PriorityList, PriorityCreate, PriorityUpdate, PriorityDelete,
    SubTaskList, SubTaskCreate, SubTaskUpdate, SubTaskDelete,
    NoteList, NoteCreate, NoteUpdate, NoteDelete
)

urlpatterns = [
    # Dashboard requires login
    path("", login_required(dashboard), name="dashboard"),

    # Task URLs
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),

    # Category URLs
    path("categories/", CategoryList.as_view(), name="category_list"),
    path("categories/create/", CategoryCreate.as_view(), name="category_create"),
    path("categories/<int:pk>/update/", CategoryUpdate.as_view(), name="category_update"),
    path("categories/<int:pk>/delete/", CategoryDelete.as_view(), name="category_delete"),

    # Priority URLs
    path("priorities/", PriorityList.as_view(), name="priority_list"),
    path("priorities/create/", PriorityCreate.as_view(), name="priority_create"),
    path("priorities/<int:pk>/update/", PriorityUpdate.as_view(), name="priority_update"),
    path("priorities/<int:pk>/delete/", PriorityDelete.as_view(), name="priority_delete"),

    # Subtask URLs
    path("subtasks/", SubTaskList.as_view(), name="subtask_list"),
    path("subtasks/create/", SubTaskCreate.as_view(), name="subtask_create"),
    path("subtasks/<int:pk>/update/", SubTaskUpdate.as_view(), name="subtask_update"),
    path("subtasks/<int:pk>/delete/", SubTaskDelete.as_view(), name="subtask_delete"),

    # Note URLs
    path("notes/", NoteList.as_view(), name="note_list"),
    path("notes/create/", NoteCreate.as_view(), name="note_create"),
    path("notes/<int:pk>/update/", NoteUpdate.as_view(), name="note_update"),
    path("notes/<int:pk>/delete/", NoteDelete.as_view(), name="note_delete"),
]