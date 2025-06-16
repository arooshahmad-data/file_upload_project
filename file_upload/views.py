from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FileForm
from .models import *
# Create your views here.

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user
            file_instance.save()
            return redirect('upload_file')
    else:
        form = FileForm()
    files = File.objects.all()
    return render(request, 'file_upload.html', {'form': form, 'files': files}) 