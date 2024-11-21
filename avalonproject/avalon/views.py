from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RecordForm, RecordSimpleForm

def index(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        formSimple = RecordSimpleForm(request.POST)
        if form.is_valid():
            form.save()
            formSimple.save()

            # Adding a success message
            messages.success(request, 'Запись успешно создана!')

            return redirect('index')
        else:
            error = 'Некоторые поля заполнены неверно. Пожалуйста, проверьте их.'
            return render(request, 'avalon/index.html', {'form': form, 'formSimple': formSimple, 'error': error})

    else:
        form = RecordForm()
        formSimple = RecordSimpleForm()

    return render(request, 'avalon/index.html', {'form': form, 'formSimple': formSimple,})

def about(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        formSimple = RecordSimpleForm(request.POST)
        if form.is_valid():
            form.save()
            formSimple.save()

            # Adding a success message
            messages.success(request, 'Запись успешно создана!')

            return redirect('about')
        else:
            error = 'Некоторые поля заполнены неверно. Пожалуйста, проверьте их.'
            return render(request, 'avalon/aboutus.html', {'form': form, 'formSimple': formSimple, 'error': error})

    else:
        form = RecordForm()
        formSimple = RecordSimpleForm()

    return render(request, 'avalon/aboutus.html', {'form': form, 'formSimple': formSimple,})

def contacts(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        formSimple = RecordSimpleForm(request.POST)
        if form.is_valid():
            form.save()
            formSimple.save()

            # Adding a success message
            messages.success(request, 'Запись успешно создана!')

            return redirect('contacts')
        else:
            error = 'Некоторые поля заполнены неверно. Пожалуйста, проверьте их.'
            return render(request, 'avalon/contacts.html', {'form': form, 'formSimple': formSimple, 'error': error})

    else:
        form = RecordForm()
        formSimple = RecordSimpleForm()

    return render(request, 'avalon/contacts.html', {'form': form, 'formSimple': formSimple,})

def gallery(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        formSimple = RecordSimpleForm(request.POST)
        if form.is_valid():
            form.save()
            formSimple.save()

            # Adding a success message
            messages.success(request, 'Запись успешно создана!')

            return redirect('gallery')
        else:
            error = 'Некоторые поля заполнены неверно. Пожалуйста, проверьте их.'
            return render(request, 'avalon/gallery.html', {'form': form, 'formSimple': formSimple, 'error': error})

    else:
        form = RecordForm()
        formSimple = RecordSimpleForm()

    return render(request, 'avalon/gallery.html', {'form': form, 'formSimple': formSimple,})

def pricelist(request):
    return render(request, 'avalon/price-list.html')
