from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CommentForm
from .models import Post, Category, Tag, Comment


# Create your views here.

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload', 'category', 'tag']

    template_name = 'blog/post_update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionError

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostCreate(LoginRequiredMixin, CreateView): #UserPassesTestMixin
    model = Post
    fields = ['title', 'category', 'content', 'head_image',  'file_upload',  'tag']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated :
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            redirect('/blog/')

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if post.author == request.user:
        post.delete()
    return redirect('/') #redirect('posts:index')

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context

def categories_page(request, slug):

    if slug == 'no-category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    context = {
        'categories' : Category.objects.all(),
        'category_less_post_count' : Post.objects.filter(category=None).count(),
        'category' : category,
        'post_list' : post_list,
    }

    return render(request, 'blog/post_list.html', context)


def tag_page(request, slug):

    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    context = {
        'tag' : tag,
        'categories' : Category.objects.all(),
        'category_less_post_count' : Post.objects.filter(category=None).count(),
        'post_list' : post_list
    }

    return render(request, 'blog/post_list.html', context)

'''
def search(request):
        if request.method == 'POST':
            searched = request.POST['searched']
            post_list = Post.objects.filter(title__contains=searched)
            return render(request, 'blog/post_list.html', {'searched': searched, 'post_list': post_list})
        else:
            return render(request, 'blog/post_list.html', {})
'''

def add_comment(request, pk):
    if not request.user.is_authenticated:
        raise PermissionError

    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        comment_temp = comment_form.save(commit=False)
        comment_temp.post = post
        comment_temp.author = request.user
        comment_temp.save()

        return redirect(post.get_absolute_url())

'''
def update_comment(request, com_id, pk):
    my_com = Comment.objects.get(id=com_id)
    com_form = CommentForm(instance=my_com)
    if request.method == 'POST':
        update_form = CommentForm(request.POST, instance=my_com)
        if update_form.is_valid():
            update_form.save()
            return redirect('post_detail', pk)
    return render(request, 'post_detail.html', {'com_form': com_form})
'''
