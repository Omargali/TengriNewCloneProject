from .models import Post
from django.core.paginator import Paginator

def index(request):

    featured_post = Post.objects.filter(category='featured').order_by('-created')[:1]
    politics = Post.objects.filter(category='politics').order_by('-created')[:2]
    business_and_economy = Post.objects.filter(category='business_economy').order_by('-created')[:2]
    culture = Post.objects.filter(category='culture').order_by('-created')[:2]
    technology = Post.objects.filter(category='technology').order_by('-created')[:2]
    sports = Post.objects.filter(category='sports').order_by('-created')[:2]
    education = Post.objects.filter(category='education').order_by('-created')[:2]

    context = {
        'featured_post': featured_post,
        'politics': politics,
        'business_and_economy': business_and_economy,
        'culture': culture,
        'technology': technology,
        'sports': sports,
        'education': education,
    }

    return render(request, 'core/index.html', context)

def post_detail(request, pk):
    post_detail = Post.objects.get(pk=pk)
    context = {'post_detail': post_detail}
    return render(request, 'core/post_detail.html', context)

from django.shortcuts import render

def politics(request):
    politics_posts = Post.objects.filter(category='politics').order_by('-created')
    context = {
        'politics_posts': politics_posts,
        'category': 'politics',
    }
    return render(request, 'core/categories.html', context)

def business(request):
    # Your logic for the business view goes here
    business_posts = Post.objects.filter(category='business_economy').order_by('-created')
    context = {
        'business_posts': business_posts,
        'category': 'business_economy',  # Устанавливаем значение переменной category
    }
    return render(request, 'core/categories.html', context)

def culture(request):
    # Your logic for the culture view goes here
    culture_posts = Post.objects.filter(category='culture').order_by('-created')
    context = {
        'culture_posts': culture_posts,
        'category': 'culture',
    }
    return render(request, 'core/categories.html', context)

def technology(request):
    # Your logic for the technology view goes here
    technology_posts = Post.objects.filter(category='technology').order_by('-created')
    context = {
        'technology_posts': technology_posts,
        'category': 'technology',
    }
    return render(request, 'core/categories.html', context)

def sports(request):
    # Your logic for the sports view goes here
    sports_posts = Post.objects.filter(category='sports').order_by('-created')
    context = {
        'sports_posts': sports_posts,
        'category': 'sports',
    }
    return render(request, 'core/categories.html', context)

def education(request):
    # Your logic for the education view goes here
    education_posts = Post.objects.filter(category='education').order_by('-created')
    context = {
        'education_posts': education_posts,
        'category': 'education',
    }
    return render(request, 'core/categories.html', context)

def search_results(request):
    query = request.GET.get('q')
    order = request.GET.get('order', 'desc')

    if query:
        search_results = Post.objects.filter(title__icontains=query)
        if order == 'asc':
            search_results = search_results.order_by('created')
        else:
            search_results = search_results.order_by('-created')
    else:
        search_results = []

    context = {
        'search_results': search_results,
        'order': order
    }
    return render(request, 'core/search_results.html', context)



