from django.shortcuts import render

from .models import Article
from .models import Author

def frontend(request, slug=None):
    """Vue.js will take care of everything else."""
    articles = Article.objects.all()
    authors = Author.objects.all()
    
    data = {
        'articles': articles,
        'authors': authors,
    }

    return render(request, 'myapp/template.html', data)
