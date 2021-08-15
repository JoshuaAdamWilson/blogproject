from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  ordering = ['-date_created']
  # ordering = ['-id']

def CategoryView(request, search_word):
  category_posts = Post.objects.filter(category=search_word)
  return render(request, 'categories.html', {'search_word': search_word, 'category_posts': category_posts})

class ArticleDetailView(DetailView):
  model = Post
  template_name = 'article_detail.html'

class AddPostView(CreateView):
  model = Post
  form_class = PostForm
  template_name = 'add_post.html'
  # fields = '__all__'
  # fields = ('title', 'body')

class AddCategoryView(CreateView):
  model = Category
  # form_class = PostForm
  template_name = 'add_category.html'
  fields = '__all__'
  # fields = ('title', 'body')

class UpdatePostView(UpdateView):
  model = Post
  form_class = EditForm
  template_name = 'update_post.html'
  # fields =['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
  model = Post
  template_name = 'delete_post.html'
  success_url = reverse_lazy('home')
