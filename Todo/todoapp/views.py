from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Todo

# Create your views here.
class ListTodoView(ListView):
    model = Todo
    context_object_name = "tasks"

class DetailTodoView(DetailView):
    model = Todo
    context_object_name = "task"

class CreateTodoView(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy('list')

class UpdateTodoView(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy('list')

class DeleteTodoView(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url =reverse_lazy('list')

