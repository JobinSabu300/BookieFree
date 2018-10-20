from django.shortcuts import render
from django.http import HttpResponse
from . import models


import sys
sys.path.insert(0, 'libg')
from customize import *

from pprint import pprint



def home(request):
   return render(request, 'index.html', {'s1books':books, 's2books':nfbooks})

def request_book(request):
   return render(request, 'request_book.html', {})

def team(request):
   return render(request, 'team.html', {})

def about(request):
   return render(request, 'about.html', {})

def signup(request):
   return render(request, 'signup.html', {})

def fiction(request):
   return render(request, 'categories.html', {'books':fbooks})

def non_fiction(request):
   return render(request, 'categories.html', {'books':nfbooks})

def search(request):
   q = request.GET.get("q", None)
   if q:
        return render(request, 'search.html', {'books': get_infoz(q)})

   else:
        message = 'Empty'#creat error page

def download(request):
    md5= request.GET.get("id", None)
    if md5:
        download_f(md5)
        return render(request, 'index.html', {'s1books': books, 's2books': nfbooks})


class Book:
   def __init__(self, img_url, name, author, ratings):
      self.img_url = img_url
      self.title = name
      self.author = author
      self.ratings = ratings

"""
vv={'img_url':'static/images/test.jpg','title':'dd','author':'jobin','ratings':''}"""
books = [
   Book("static/images/test.jpg","Book Of Pook", "Jobin Sabu", 5),
   Book("static/images/s8.jpg","Out of the Box", "Bhavay Khanna", 4),
   Book("static/images/s2.jpg","Avengers", "Chetan Bhagath", 3),
   Book("static/images/s3.jpg","Good Deals", "Simon Sinek", 4),
   Book("static/images/s4.jpg","Jungle Book", "Blalaswani", 5),
   Book("static/images/s5.jpg","Python", "Albert Einstein", 3),
]

fbooks = [
   Book("static/images/test.jpg","testbook", "Jobin Sabu", 5),
   Book("static/images/s8.jpg","Out of the Box", "Bhavay Khanna", 4),
   Book("static/images/s2.jpg","Avengers", "Chetan Bhagath", 3),
   Book("static/images/s3.jpg","Good Deals", "Simon Sinek", 4),
   Book("static/images/s4.jpg","Jungle Book", "Blalaswani", 5),
   Book("static/images/s5.jpg","Python", "Albert Einstein", 3),
   Book("static/images/s9.jpg","testbook2", "Jobin Sabu", 5),
   Book("static/images/s3.jpg","Out of the Box", "Bhavay Khanna", 4),
   Book("static/images/s5.jpg","Avengers", "Chetan Bhagath", 3),
   Book("static/images/s4.jpg","Good Deals", "Simon Sinek", 4),
   Book("static/images/s8.jpg","Jungle Book", "Blalaswani", 5),
   Book("static/images/s4.jpg","Python", "Albert Einstein", 3),
]

nfbooks = [
   Book("static/images/s9.jpg","testbook2", "Jobin Sabu", 5),
   Book("static/images/s3.jpg","Out of the Box", "Bhavay Khanna", 4),
   Book("static/images/s5.jpg","Avengers", "Chetan Bhagath", 3),
   Book("static/images/s4.jpg","Good Deals", "Simon Sinek", 4),
   Book("static/images/s8.jpg","Jungle Book", "Blalaswani", 5),
   Book("static/images/s4.jpg","Python", "Albert Einstein", 3),
]