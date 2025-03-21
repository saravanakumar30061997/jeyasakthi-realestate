from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Blog

# Show all blogs with pagination
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    paginator = Paginator(blogs, 3)  # Show 3 items per page
    page_number = request.GET.get('page')  # Get page number from URL query params
    page_obj = paginator.get_page(page_number)  # Get the paginated page
    return render(request, 'blog/all_blogs.html', {"page_obj": page_obj, "context": blogs})

# Redirect from old ID URL to new slug-based URL
def redirect_to_slug(request, id):
<<<<<<< HEAD
    try:
        blog = Blog.objects.get(id=id)
        return redirect('blog:detail', slug=blog.slug, permanent=True)
    except Blog.DoesNotExist:
        return redirect('blog:all_blogs')  # Redirect to blog list or any fallback page
=======
    blog = Blog.objects.filter(id=id).first()
    
    if blog:
        return redirect('blog:detail', slug=blog.slug, permanent=True)  # 301 Permanent Redirect
    else:
        return redirect('blog:all_blogs')  # Redirect to index if ID is not found
>>>>>>> e4fdfab8f1661388ead89bb1197f360f2fa652c5

# Blog detail view using slug
def detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/detail.html', {'blog': blog})
