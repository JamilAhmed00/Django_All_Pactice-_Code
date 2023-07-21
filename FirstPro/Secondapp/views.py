
# Create your views here.

from django.shortcuts import render

from django.http import HttpResponse

def courses(request):
    return HttpResponse('''
                        <h1>hello this is my COURSES page</h1>
                        <a href = '/secondapp/feedback/'>Feedback </a>
                        <a href = '/firstapp/contact/'>Contact </a>
                        <a href = '/firstapp/about/'>About </a>
                        
                        
                        ''')

def feedback(request):
    return HttpResponse('''
                        
                        <h1>This is my FEEDBACK PAGE</h1>
                        <a href = '/secondapp/courses/'>Courses </a>
                        <a href = '/firstapp/contact/'>Contact </a>
                        <a href = '/firstapp/about/'>About </a>
                        
                        
                        ''')


