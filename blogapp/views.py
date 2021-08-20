from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Comment, Post, Category
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

# def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  ordering = ['-date_created']
  # ordering = ['-id']

  # def get_context_data(self, *args, **kwargs):
  #   category_menu = Category.objects.all()
  #   context = super(HomeView, self).get_context_data(*args, **kwargs)
  #   context["category_menu"] = category_menu
  #   return context

def CategoryListView(request):
  category_list = Category.objects.all().order_by('name')
  return render(request, 'category_list.html', { 'category_list': category_list })


def CategoryView(request, search_word):
  category_posts = Post.objects.filter(category=search_word.replace('-', ' '))
  return render(request, 'categories.html', {'search_word': search_word.replace('-', ' '), 'category_posts': category_posts})


def LikeView(request, pk):
  post = get_object_or_404(Post, id=request.POST.get('post_id'))
  liked = False
  if post.likes.filter(id=request.user.id).exists():
    post.likes.remove(request.user)
    liked = False
  else:
    post.likes.add(request.user)
    liked = True
  return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class ArticleDetailView(DetailView):
  model = Post
  template_name = 'article_detail.html'

  def get_context_data(self, *args, **kwargs):
    context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
    stuff = get_object_or_404(Post, id=self.kwargs['pk'])
    total_likes = stuff.total_likes()
    liked = False
    if stuff.likes.filter(id=self.request.user.id).exists():
      liked = True
    context["total_likes"] = total_likes
    context["liked"] = liked
    return context


class AddPostView(CreateView):
  model = Post
  form_class = PostForm
  template_name = 'add_post.html'
  # fields = '__all__'
  # fields = ('title', 'body')


class AddCommentView(CreateView):
  model = Comment
  form_class = CommentForm
  template_name = 'add_comment.html'
  # fields = '__all__'
  def form_valid(self, form):
    form.instance.post_id = self.kwargs['pk']
    return super().form_valid(form)

  # success_url = reverse_lazy('home')
  def get_success_url(self):
    return reverse_lazy('article-detail', kwargs={'pk': self.kwargs['pk']})


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
