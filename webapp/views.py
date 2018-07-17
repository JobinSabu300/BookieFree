from django.shortcuts import render
from django.http import HttpResponse
from . import models


def home(request):
   return render(request, 'index.html', {'s1books':books, 's2books':nfbooks})

def fiction(request):
   return render(request, 'categories.html', {'books':fbooks})

def non_fiction(request):
   return render(request, 'categories.html', {'books':nfbooks})




class Book:
   def __init__(self, img_url, name, author, ratings):
      self.img_url = img_url
      self.name = name
      self.author = author
      self.ratings = ratings



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