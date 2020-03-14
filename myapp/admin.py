from django.contrib import admin

from .models import Article
from .models import Author

# register models to use in admin site
admin.site.register(Article)
admin.site.register(Author)
