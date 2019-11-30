from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Student
from .forms import StudentForm, DeleteStudentForm
from django.core.exceptions import ObjectDoesNotExist

def show(request):
    return render(request, 'main/home.html', {'students' : Student.objects.all()})

def insert(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'{name}\'s record has been created!')
            return redirect('data-show')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()

    return render(request, 'main/insert.html', {'form': form})

def delete(request):

    '''form = InventoryForm()
        inventory = Inventory.objects.all()
        item_id = int(request.POST.get('item_id'))  
        item = Inventory.objects.get(id=item_id)       
        item.delete() '''

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        '''field_name = 'name'
        obj = Student.objects.all()
        student = getattr(obj, field_name)
        form = DeleteStudentForm(request.POST)'''
        student = request.POST.get('name')
        try:
            Student.objects.get(name= student).delete()
            messages.success(request,  f'{student}\'s record has been deleted!')
        except ObjectDoesNotExist:
            messages.warning(request,  f'{student}\'s record does not exist!')
        return redirect('data-show')

    else:
        form = DeleteStudentForm()
    return render(request, 'main/delete.html', {'form' : form})


def about(request):
    return render(request, 'main/about.html')
