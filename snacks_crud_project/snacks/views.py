from django.db import models
from django.shortcuts import render
from django.views.generic import (
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    DeleteView,
                                    UpdateView,
                                    # View
                                    )

from .models import Snack
from django.urls import reverse_lazy

# Create your views here.

class ListSnackView(ListView):
    template_name = 'snack_list.html'
    model = Snack


class DetailSnackView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack


class CreateSnackView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['title', 'rate', 'description', 'purchaser']

class DeleteSnackView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')


class UpdateSnackView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['title', 'rate', 'description']
