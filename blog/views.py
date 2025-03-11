from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    paginator = Paginator(blogs, 3)  # Show 3 items per page
    page_number = request.GET.get('page')  # Get page number from URL query params
    page_obj = paginator.get_page(page_number)  # Get the paginated page
    return render(request,'blog/all_blogs.html',{"page_obj":page_obj,"context":blogs})

def detail(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request,'blog/detail.html',{'blog':blog})
