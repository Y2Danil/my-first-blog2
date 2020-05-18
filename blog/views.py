from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
  Posts  = Post.objects.order_by('-published_date')
  return render(request, 'blog/post_list.html', {'Posts': Posts})