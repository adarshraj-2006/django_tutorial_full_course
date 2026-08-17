from django.shortcuts import render
from .models import Note
from django.http import Http404
from django.views.generic import CreateView,ListView,DetailView
# Create your views here.

from .forms import NotesForm

class NotesCreateView(CreateView):
     model=Note
     form_class=NotesForm
     success_url='/notes'
     template_name='notes/notes_form.html'
class NoteList(ListView):
     model = Note
     context_object_name = 'notes'      
     template_name ='notes/notes_list.html'

class NoteDetail(DetailView):
     model = Note
     context_object_name = 'note'
     template_name = 'notes/notes_detail.html'

def list(request):
    
    all_notes=Note.objects.all()
    

    return render(request,'notes/notes_list.html',{'notes':all_notes})

def detail(request,pk):
    try:
        note =Note.objects.get(pk=pk)
    except Note.DoesNotExist:
            raise Http404("Note does not exist")
    return render(request,'notes/notes_detail.html',{'notes':note})

