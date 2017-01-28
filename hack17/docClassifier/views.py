from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms import *
import kmeans
# Create your views here.
ABS_PATH = '/Users/Ahmed/Downloads/hackathon17/GiveMeA-br-/'
CODEBOOK_PATH = ABS_PATH+'src/min_training.txt.32cents'

def handle_uploaded_file(f):
    return 1

def upload_file(request):
    if request.method == 'POST':
        form = DocumentURIForm(request.POST)
        if form.is_valid():
            res = handle_uploaded_file(request.POST['uri'])
            print res
            return render(request, 'classification.html', {'form': form,
            									'result': res})
    else:
        form = DocumentURIForm()
    return render(request, 'classification.html', {'form': form})

