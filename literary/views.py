from django.shortcuts import render
from literary.models import Literarysource
from literary.models import Textesource
from literary.forms import PostSearchForm

# Create your views here

# function
def literarysource(request):
    if request.method == 'POST':
        print('Received data:', request.POST['sourceName'])
        Literarysource.objects.create(title=request.POST['sourceName'],
                                      author=request.POST['sourceName'],
                                      url_q=request.POST['sourceName'],
                                      pdf_file=request.POST['sourceName'])

        all_sources = Literarysource.objects.all()

    return render(request, 'index.html', {'all_sources': all_sources})

# function
def textesource(request):
    if request.method == 'POST':
        print('Received data:', request.POST['textName'])
        Textesource.objects.create(essay=request.POST['textName'],
                                   essay_post=request.POST['textName'],
                                   project=request.POST['textName'])

        all_texte = Textesource.objects.all()

    return render(request, 'index.html', {'all_texte': all_texte})


# searchfunction
def post_search(request):
    form = PostSearchForm

    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            results = Literarysource.objects.filter(author__icontains=q)

    return render(request, 'index.html', {'form': form, 'results': results})

