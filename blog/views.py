from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})




#In Django's ORM (Object-Relational Mapping), the __lte is a lookup syntax known as 
# "less than or equal to." It's used to filter querysets based on a specific condition.

"""In Django, the request object is typically passed as a parameter to views rather than being 
inherited from a superclass.

In the provided post_list function:

python code:
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
request is indeed used as a parameter. When Django receives an HTTP request, it routes it to an 
appropriate view function. This function then takes the request object as a parameter, allowing 
it to access information about the request (e.g., user session, request method, request headers).

So, in summary, request is not inherited from any superclass but is instead passed as a parameter 
to the view function to handle the incoming HTTP request."""