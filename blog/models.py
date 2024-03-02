"""How will we model blog posts then? We want to build a blog, right?

We need to answer the question: What is a blog post? What properties should it have?

Well, for sure our blog post needs some text with its content and a title, right? It would be also 
nice to know who wrote it – so we need an author. Finally, we want to know when the post was created 
and published.

Post
--------
title
text
author
created_date
published_date
What kind of things could be done with a blog post? It would be nice to have some method that 
publishes the post, right?

So we will need a publish method.

Since we already know what we want to achieve, let's start modeling it in Django!

Django model
Knowing what an object is, we can create a Django model for our blog post.

A model in Django is a special kind of object – it is saved in the database. A database is a 
collection of data. This is a place in which you will store information about users, your blog posts, 
etc. We will be using a SQLite database to store our data. This is the default Django database 
adapter – it'll be enough for us right now.

You can think of a model in the database as a spreadsheet with columns (fields) and rows (data)."""
from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    
    
    """Double-check that you use two underscore characters (_) on each side of str. This convention is used frequently in Python and sometimes we also call them "dunder" (short for "double-underscore").

It looks scary, right? But don't worry – we will explain what these lines mean!

All lines starting with from or import are lines that add some bits from other files. So instead of copying and pasting the same things in every file, we can include some parts with from ... import ....

class Post(models.Model): – this line defines our model (it is an object).

class is a special keyword that indicates that we are defining an object.
Post is the name of our model. We can give it a different name (but we must avoid special characters and whitespace). Always start a class name with an uppercase letter.
models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
Now we define the properties we were talking about: title, text, created_date, published_date and author. To do that we need to define the type of each field (Is it text? A number? A date? A relation to another object, like a User?)

models.CharField – this is how you define text with a limited number of characters.
models.TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
models.DateTimeField – this is a date and time.
models.ForeignKey – this is a link to another model.
We will not explain every bit of code here since it would take too much time. You should take a look at Django's documentation if you want to know more about Model fields and how to define things other than those described above (https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types).

What about def publish(self):? This is exactly the publish method we were talking about before. def means that this is a function/method and publish is the name of the method. You can change the name of the method if you want. The naming rule is that we use lowercase and underscores instead of spaces. For example, a method that calculates average price could be called calculate_average_price.

Methods often return something. There is an example of that in the __str__ method. In this 
scenario, when we call __str__() we will get a text (string) with a Post title.

Also notice that both def publish(self): and def __str__(self): are indented inside our class. 
Because Python is sensitive to whitespace, we need to indent our methods inside the class. 
Otherwise, the methods won't belong to the class, and you can get some unexpected behavior.

If something is still not clear about models, feel free to ask your coach! We know it is 
complicated, especially when you learn what objects and functions are at the same time. But 
hopefully it looks slightly less magic for you now!
=========================================the purpose of _ _ str_ _() function  =========================================

In Python, the __str__() method is a special method that is called when you use the built-in str() 
function or when an object is converted to a string implicitly (e.g., when you print the object). 
Its purpose is to return a string representation of the object.

Here's a real-life example to help understand its purpose:

Let's say you have a Car class representing different cars in a car dealership. Each car has 
attributes like make, model, and year. When you print a Car object, you want it to display a 
user-friendly representation of the car's details.

python
Copy code
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
Now, when you create a Car object and print it, the __str__() method will be called automatically 
to provide a string representation:

python
Copy code
my_car = Car("Toyota", "Camry", 2020)
print(my_car)  # Output: 2020 Toyota Camry
In this example, the __str__() method allows us to define how a Car object should be displayed as 
a string. This makes the output more meaningful and readable for users when they interact with 
instances of the Car class
================================================================================================











"""