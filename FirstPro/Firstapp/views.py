from django.shortcuts import render

from django.http import HttpResponse

def contact(request):
    return HttpResponse('''
                        
                        <h1>hello this is my contact page</h1>
                        <a href = '/firstapp/about/'>About </a>
                        <a href = '/secondapp/courses/'>Courses </a>
                        <a href = '/secondapp/feedback/'>Feedback </a>
                        
                        ''')

def about(request):
    
    return HttpResponse('''
                        
                        <h1>This is my ABOUT PAGE</h1>
                        <a href = '/firstapp/contact/'>Contact </a>
                        <a href = '/secondapp/courses/'>Courses </a>
                        <a href = '/secondapp/feedback/'>Feedback </a>
                        
                        ''')