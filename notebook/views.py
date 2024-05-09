from django.shortcuts import render, get_object_or_404
from django.views import View

from notebook.models import Notebook


# Create your views here.
class notesView(View):
    queryset = Notebook.published.all()
    context_object_name = "notes"
    paginate_by = 6
    template_name = "notes/note/list.html"

def notes_detail(request, year, month, day, slug):
    note = get_object_or_404(Notebook, slug=slug, status='published',
                             published_date__year=year, published_date__month=month,
                             published_date__day=day)
    return render(request, 'notes/note/detail.html', {'note': note})