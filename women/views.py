from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy

from women.utils import DataMixin

from .forms import AddPostForm, UploadFileForm
from .models import Category, Women, TagPost, UploadFiles
from django.views.generic import ListView, DetailView , CreateView, UpdateView
from django.core.paginator import Paginator



class WomenHome(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    title_page = 'Asosiy Varaq'
    cat_selected = 0

    def get_queryset(self) -> QuerySet[Any]:
        return Women.published.all().select_related('cat')


@login_required()
def about(request):
    contact_list = Women.published.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'women/about.html',
                  { 'title': 'Sayt haqida', 'page_obj': page_obj })



class ShowPost(DataMixin ,DetailView):
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_content(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])



class AddPage(LoginRequiredMixin, DataMixin ,CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    title_page = 'Post qo\'shish'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdatePage(DataMixin, UpdateView):
    model = Women
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    title_page  = ' Update qilish'


def contact(request):
    return HttpResponse("Feedback Page")

def login(request):
    return HttpResponse("Login Page")


class WomenCategory(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        print('*************************', context['posts'][1])
        return self.get_mixin_content(context,
                                      title = 'Kategoriya - ' + cat.name,
                                      cat_selected=cat.pk
                                     )


class TagPostList(DataMixin ,ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_content(context, title= 'Teg - ' + tag.tag, )
    
    def get_queryset(self) -> QuerySet[Any]:
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')
