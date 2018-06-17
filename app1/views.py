from django.shortcuts import render
from .forms import UserDetailsForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'app1/index.html')


def display_form(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        print(dir(form))
        if form.is_valid():
            form.save()

            return redirect('app1_index')
    else:
        form = UserDetailsForm()
    context = {'form': form}
    return render(request, 'app1/display_form.html', context)
