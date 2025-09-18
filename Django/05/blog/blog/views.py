from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from blog.models import Blog
from blog.forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')

    q = request.GET.get('q')
    if q:
        from django.db.models import Q
        blogs = blogs.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        )
        # blogs = blogs.filter(title__icontains=q)

    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    page_object = paginator.get_page(page)

    visits = int(request.COOKIES.get('visits', 0)) + 1
    request.session['count'] = request.session.get('count', 0) + 1
    context = {
        'object_list':page_object.object_list,
        'page_obj':page_object,
    }
    response = render(request, 'blog_list.html', context)
    response.set_cookie('visits', visits)

    return response
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog':blog}
    return render(request, 'blog_detail.html', context)

@login_required()
def blog_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        return redirect(reverse('fb:detail', kwargs={'pk':blog.pk}))

    form = BlogForm()
    context = {'form':form}

    return render(request, 'blog_create.html', context)


@login_required()
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    # if request.users != blog.author:
    #     raise Http404
    # 혹은 blog = get_object_or_404(Blog, pk=pk, author=request.users)
    # 같이 해서 걸러준다.
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        blog = form.save()
        # 여기서 작성자를 대조해서 확인 할 필요는 없다.
        return redirect(reverse('blog_detail', kwargs={'pk':blog.pk}))

    context = {
        'form':form
    }
    return render(request, 'blog_update.html', context)

@login_required()
@require_http_methods(['POST'])
def blog_delete(request, pk):
    # if request.method != 'POST':
    #     raise Http404

    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    blog.delete()

    return redirect(reverse('fb_list'))

