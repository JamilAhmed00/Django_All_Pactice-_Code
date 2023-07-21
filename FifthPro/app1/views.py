from django.shortcuts import render

from . forms import contactForm
from . forms import studentdata

from . forms import passwordValidationProject

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
    
    
def about(request):
    
    if request.method == 'POST':
        
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, "./app1/about.html",{'name': name,'email': email, 'select': select})
    
    else:
        return render(request, "./app1/about.html")


def forms(request):

    return render(request, "./app1/forms.html")


def djangoForm(request):
    
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        # form = contactForm(request.POST)
        if form.is_valid():
        
            file = form.cleaned_data['file']
            with open('./app1/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
    
        #file = form.cleaned_data['file']
            print(form.cleaned_data)
            return render(request, "./app1/djangoform.html", {'form': form})
    
    else:
        form = contactForm()
        
    return render(request, "./app1/djangoform.html", {'form': form})



def studentform(request):
    
    if request.method == 'POST':
        form = studentdata(request.POST, request.FILES)
        if form.is_valid():
        
            print(form.cleaned_data)
            # return render(request, "./app1/djangoform.html", {'form': form})
            
    
    else:
        form = studentdata()
        
    return render(request, "./app1/djangoform.html", {'form': form})



def passwordValidation(request):
    
    if request.method == 'POST':
        form = passwordValidationProject(request.POST, request.FILES)
        if form.is_valid():
        
            print(form.cleaned_data)
            # return render(request, "./app1/djangoform.html", {'form': form})
            
    
    else:
        form = passwordValidationProject()
        
    return render(request, "./app1/djangoform.html", {'form': form})