from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from .forms import DocumentForm


# Create your views here.
def index(request):
    return render(request, 'upload_app/index.html')
    # return HttpResponse('I am index')


def parse_json(json):
    return json


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        context = {
            'uploaded_file_url': fs.url(filename)
        }
        return render(request, 'upload_app/upload.html', context)
    else:
        return render(request, 'upload_app/upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
    context = {
        'form': form,
    }
    return render(request, 'upload_app/model_upload.html', context)
