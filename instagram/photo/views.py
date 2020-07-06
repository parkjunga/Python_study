from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo

# Create your views here.

class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'

class PhotoCreate(CreateView):
    model = Photo
    fields = ['text','image'] # 모델 활용하여 생성할 때 채워야 할 필드확인 후 아래 템플릿으로 넘어감
    template_name_suffix = '_create'
    success_url = '/' # 성공시 메인으로

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text','image']
    template_name_suffix = '_update'

class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    success_url = '/'

class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'
