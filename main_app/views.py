from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from .models import gym
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"

# OTHERS


class GymList(TemplateView):
    template_name = "gym_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["gym"] = gym.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["gym"] = gym.objects.all()
            # default header for not searching
            context["header"] = "Local Gyms"
        return context


class GymCreate(CreateView):
    model = gym
    fields = ['name', 'img', 'classes']
    template_name = "gym_create.html"

    def get_success_url(self):
        return reverse('gym_detail', kwargs={'pk': self.object.pk})


class GymDetail(DetailView):
    model = gym
    template_name = "gym_detail.html"


class GymUpdate(UpdateView):
    model = gym
    fields = ['name', 'img', 'classes']
    template_name = "gym_update.html"

    def get_success_url(self):
        return reverse('gym_detail', kwargs={'pk': self.object.pk})
