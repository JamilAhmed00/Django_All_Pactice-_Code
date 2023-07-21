

from django import template
from django.template.loader import get_template

register = template.Library()

def my_template(value, arg):
    
    if arg == 'change':
        value = 'Rahim'
        return value
    

def show_courses():
    courses = [
        
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
        
    ]
    
    return { 'courses': courses }
    
    
courses_template = get_template('app1/courses.html')    
register.filter('change_name',my_template)
     
register.inclusion_tag(courses_template)(show_courses)