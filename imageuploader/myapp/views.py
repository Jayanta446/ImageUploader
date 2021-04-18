from django.shortcuts import render
from .forms import ImageForm
from .models import ImageModel
# Create your views here.

def home_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form_obj = ImageForm()
    images = ImageModel.objects.all()
    return render(request, 'myapp/home.html', {'form':form_obj, 'images':images})


