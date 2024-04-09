from django.shortcuts import render
from .models import ProfileModel, SkillModel, CategoryModel, AboutModel, ServiceModel, ProjectModel, BlogModel

from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.



def home_page(request):
    profile = ProfileModel.objects.last()
    skills = SkillModel.objects.order_by()
    categories = CategoryModel.objects.all()
    offers = ServiceModel.objects.all()
    about = AboutModel.objects.all()
    projects = ProjectModel.objects.all()
    blogs = BlogModel.objects.all()
    
    return render(request, "index.html", 
                  {'profile': profile, 
                   'skills': skills, 
                   'categories': categories, 
                   'offers': offers, 
                   'about':about, 
                   'projects':projects,
                   'blogs': blogs
                   })


def project_detail(request, pk):
    project = get_object_or_404(ProjectModel, id=pk)
    return render(request, 'portfolio-details.html', {'project' : project})

def single_page(request, pk):
    page = get_object_or_404(ProjectModel, id=pk)
    return render(request, 'single-blog.html', {'blog' : page})


def blog_page(request, pk):
    blogs = BlogModel.objects.all()
    
    if request.method == "POST":
        search = request.POST.get('search')
        blogs = BlogModel.objects.filter(title__icontains = search)

    p = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    try:
        page_objects = p.get_page(page_number)
    except PageNotAnInteger:
        page_objects =  p.page(1)
    except EmptyPage:
        page_objects = p.page(p.num_pages)
    
    return render(request, 'blog.html', {'blogs': page_objects})


def blog_page_wiev(request, pk):
    page = get_object_or_404(BlogModel, id=pk)
    page.view_count += 1
    page.save()
    
    lot_of = BlogModel.objects.filter()
    
    return render(request, 'blog.html')

def about_page(request):
    return render(request, 'about-us.html')


def portfolio_page(request):
    return render(request, 'portfolio.html')