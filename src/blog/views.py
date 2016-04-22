from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def blog_list(request):
    queryset_list = Post.objects.all()

    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset, "title": "List"}
    print 'sss:%s' % queryset_list[0].image.url
    return render(request, 'blog_list.html', context)


def blog_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {"title": instance.title, "instance": instance}
    return render(request, 'blog_detail.html', context)


