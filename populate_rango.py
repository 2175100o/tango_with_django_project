import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    #create dictionarys for each cat with pages
    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/",
         "views": 50},
        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/",
         "views": 35},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/",
         "views": 20} ]

    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 10},
        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/",
         "views": 70},
        {"title":"How to Tango with Django",
         "url":"http://www.tangowithdjango.com/",
         "views": 900} ]

    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/",
         "views": 25},
        {"title":"Flask",
         "url":"http://flask.pocoo.org",
         "views": 43} ]

    #combine cats
    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages} }


    #add cats/pages to db
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

# Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

#methods for adding pages
def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    if name == 'Python':
        c.views = 128
        c.likes = 64
    elif name == 'Django':
        c.views = 64
        c.likes = 32
    elif name == 'Other Frameworks':
        c.views = 32
        c.likes = 16
    c.save()
    return c
# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
