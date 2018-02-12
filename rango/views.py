from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    #Constuct a dictionary to pass to the template engine as its context
    #Note the key boldmessage is the same as {{boldmessage}} in the template
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    
    context_dict = {'pages': page_list,
                    'categories': category_list}

    #Return a rendered response to send to the client
    #We make use of the shortcut function to make our lives easier
    #Note that the first parameter is teh template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #Construct Dictionary
    context_dict = {'firstline' : "Rango says here is the about page.",
                    'madeby' : "This tutorial has been put together by Samuel Owen-Hughes."}

    #Render Request    
    return render(request, 'rango/about.html', context = context_dict)

def show_category(request, category_name_slug):
    #dictionary
    context_dict = {}

    try:
        #does given slug exist as category
        category = Category.objects.get(slug=category_name_slug)
        #get associated pages
        pages = Page.objects.filter(category=category)
        #update dictionary
        context_dict['pages'] = pages
        #also add cats for verification
        context_dict['category'] = category
    except Category.DoesNotExist:
        #only here if not found anything, do nothing
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)
