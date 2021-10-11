from django.shortcuts import render, redirect, reverse
# from django.urls import reverse
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import gym, Skill, Mastered
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mastered"] = Mastered.objects.all()
        return context



# OTHERS
class GymList(TemplateView):
    template_name = "gym_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["gym"] = gym.objects.filter(
                name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["gym"] = gym.objects.filter(user=self.request.user)
            context["header"] = "Local Gyms"
        return context


class GymCreate(CreateView):
    model = gym
    fields = ['name', 'img', 'classes']
    template_name = "gym_create.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GymCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
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


class GymDelete(DeleteView):
    model = gym
    template_name = "gym_delete_confirmation.html"
    success_url = "/gym/"


class SkillCreate(View):

    def post(self, request, pk):
        technique = request.POST.get("technique")
        # class_took = request.POST.get("class_took")
        gyms = gym.objects.get(pk=pk)
        Skill.objects.create(technique=technique, gyms=gyms)
        return redirect('gym_detail', pk=pk)


class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("gym_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
