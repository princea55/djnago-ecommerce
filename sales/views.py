from django.shortcuts import render, redirect
from .models import BlogPost
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
# from school.midddleware.main import BlockMobileMiddleware
# from school.middleware.main import BlockMobileMiddleware
# from e_store.school.middleware.main import BlockMobileMiddleware


class BlogListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = "sales/blogs_list.html"

    # def get(self, request, *args, **kwargs):
    #     res = super().get(request, *args, **kwargs)
    #     record = res.__dict__.get('context_data').get('object_list')
    #     if record:
    #         res.__dict__.get('context_data').update({'object_list': record.exclude(created_by__isnull=True)})
    #     return res

    # def get_context_data(self, **kwargs):
    #     context = super(BlogListView, self).get_context_data(**kwargs)
    #     record = context.get('object_list')
    #     if record:
    #         context.update({'object_list': record.exclude(created_by__isnull=True)})
    #     return context

    def get_queryset(self):
        return self.model.objects.exclude(created_by__isnull=True)


class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = BlogPost
    fields = "__all__"
    success_message = "New Blog successfully added."
    template_name = "sales/create_blog.html"


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = "sales/detail_view_blog.html"
    pk_url_kwarg = 'id'


class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = BlogPost
    fields = "__all__"
    success_message = "Blog successfully updated."
    template_name = "sales/create_blog.html"
    pk_url_kwarg = 'id'


class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog-list")
    success_message = "Blog successfully deleted."
    pk_url_kwarg = 'id'
    template_name = "sales/blog_confirm_delete.html"

# class BlogPostView(View):
#
#     def get(self, request, *args, **kwargs):
#         id = kwargs.get('id')
#         if request.get_full_path() == '/create-blog':
#             form = BlogPostFormView()
#             return render(request, 'sales/create_blog.html', {'form': form})
#         elif request.get_full_path() == '/blog-list':
#             blogs = BlogPost.objects.all()
#             return render(request, 'sales/blogs_list.html', {'blogs': blogs})
#         elif request.get_full_path() == f'/detail-blog/{id}':
#             blog = BlogPost.objects.get(pk=id)
#             return render(request, 'sales/detail_view_blog.html', {'blog': blog})
#
#     def post(self, request):
#         form = BlogPostFormView(request.POST) or None
#         if form.is_valid():
#             form.save()
#             return redirect('blog-list')
