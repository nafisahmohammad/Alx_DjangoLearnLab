from django.shortcuts import render
from .forms import ExampleForm

def example_form_view(request):
    form = ExampleForm()

    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            pass

    return render(request, 'bookshelf/form_example.html', {'form': form})

