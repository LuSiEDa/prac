from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog

class BlogListView(ListView):
    # model = Blog
    queryset = Blog.objects.all().order_by('-created_at')
    template_name = 'blog_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q')

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q)
            )
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    # pk_url_kwarg = 'id' 로 해주면 path에서 <int:id>를 쓸 수 있는데... 굳이?

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(id__lte=50)
    # 전체 데이터 가져오는...

    # def get_object(self, queryset=None):
    #     object = super().get_object()
    #     object = self.model.objects.get(pk=self.kwargs.get('pk'))
    #     return object
    # 특정 데이터 가져오는...

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['test'] = 'CBV'
    #     return context
    # 템플릿에 넘길 context를 조작하는...


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = ('category', 'title', 'content')
    # success_url = reverse_lazy('cb_blog_list')
    # => 동적인 게 필요할땐 이게 아니라 별도의 함수를 만들어.

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


    # def get_success_url(self):
    #     return reverse_lazy('blog:blog_detail', kwargs={'pk':self.object.pk})

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    fields = ('category', 'title', 'content')

    # def get_success_url(self):
    #     return reverse_lazy('blog:blog_detail', kwargs={'pk':self.object.pk})
    # :이렇게 해도 상관은 없지만 지금은 다른 방식을 써보자.
    # models.py에 get_absolute_url 참조.

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(author=self.request.user)

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #
    #     if self.object.author != self.request.users:
    #         raise Http404
    #     return self.object

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        page = self.request.POST.get('page') or self.request.GET.get('page')
        if page:
            return reverse_lazy('blog_list') + f"?page={page}"
        return reverse_lazy('blog_list')
