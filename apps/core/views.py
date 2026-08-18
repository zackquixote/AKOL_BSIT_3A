from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    return HttpResponse("Hello from Django! This is a simple view response.")


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'core/post_list.html', {'posts': posts})