from django.views.generic import ListView 
from django.views.generic.base import TemplateView
from django.shortcuts import render

from apps.post.models import Post

# Create your views here.

class IndexPostView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_403_view(request, exception=None):
    return render(request, '403.html', status=403)

class AboutView(TemplateView):
    template_name = 'about.html'
    