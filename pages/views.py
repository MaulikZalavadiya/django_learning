from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post

from django.urls import reverse_lazy



class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

class HomeDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'  

          
class HomeCreateView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class HomeUpdateView(UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']   

class HomeDeleteView(DeleteView): # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')     