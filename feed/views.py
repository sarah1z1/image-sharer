#from django.shortcuts import render   //this is used for fuction-based view and we're gonna use class-based view

# Create your views here.

from typing import Any, Dict
from django.views.generic import TemplateView, DetailView,FormView
from .models import Post
from .forms import PostForm
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = 'home.html'     #look for a file called home.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context


class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post


class AddPostView(FormView):
    template_name = 'new_post.html'
    success_url = '/'
    form_class = PostForm

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.INFO, "Your Post is Submitted Successfully!")
        return super().form_valid(form)
