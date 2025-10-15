"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from To_Do_List.views import HomePageView, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, SubTaskListView, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView, NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView, PriorityListView, PriorityCreateView, PriorityDeleteView, PriorityUpdateView, CategoryListView, CategoryDeleteView, CategoryCreateView, CategoryUpdateView
from To_Do_List import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),  # allauth routes
    path('', views.HomePageView.as_view(), name='home'),

    path('task_list', TaskListView.as_view(), name='task-list'),
    path('subtask_list', SubTaskListView.as_view(), name='subtask-list'),
    path('note_list', NoteListView.as_view(), name='note-list'),
    path('priority_list', PriorityListView.as_view(), name='priority-list'),
    path('category_list', CategoryListView.as_view(), name='category-list'),

    path('task_list/add', TaskCreateView.as_view(), name='task-add'),
    path('note_list/add', NoteCreateView.as_view(), name='note-add'),
    path('subtask_list/add', SubTaskCreateView.as_view(), name='subtask-add'),
    path('priority_list/add', PriorityCreateView.as_view(), name='priority-add'),
    path('category_list/add', CategoryCreateView.as_view(), name='category-add'),

    path('task_list/<pk>',TaskUpdateView.as_view(), name='task-update'),
    path('note_list/<pk>',NoteUpdateView.as_view(), name='note-update'),
    path('subtask_list/<pk>',SubTaskUpdateView.as_view(), name='subtask-update'),
    path('priority_list/<pk>',PriorityUpdateView.as_view(), name='priority-update'),
    path('category_list/<pk>',CategoryUpdateView.as_view(), name='category-update'),

    path('task_list/<pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('note_list/<pk>/delete', NoteDeleteView.as_view(), name='note-delete'),
    path('subtask_list/<pk>/delete', SubTaskDeleteView.as_view(), name='subtask-delete'),
    path('priority_list/<pk>/delete', PriorityDeleteView.as_view(), name='priority-delete'),
    path('category_list/<pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),
    
]
