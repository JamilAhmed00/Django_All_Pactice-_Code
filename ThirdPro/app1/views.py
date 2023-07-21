from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, './app1/index.html', {'author':'Jamil', 'courses': [
        
        {
            'id': 1,
            'Course': 'C',
            'Teacher': 'JJJJ'
        },
        {
            'id': 2,
            'Course': 'C++',
            'Teacher': 'TTTT'
        },
        {
            'id': 3,
            'Course': 'Python',
            'Teacher': 'PPP'
        },
        
    ]})