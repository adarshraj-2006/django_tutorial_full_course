from django.shortcuts import render
from .models import Note
from django.http import Http404,HttpResponseRedirect
from django.views.generic import CreateView,ListView,DetailView,UpdateView,TemplateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

from .forms import NotesForm

class HomeView(TemplateView):
     template_name='home/welcome.html'
class LogoutInterfaceView(LogoutView):
    next_page='notes/logout.html'
class LoginInterfaceView(LoginView):
     template_name='notes/login.html'



class NotesDeleteView(DeleteView):

     model=Note
     success_url='/notes'
     context_object_name = 'note'
     template_name='notes/notes_delete.html'

class NotesUpdateView(UpdateView):
     model=Note
     form_class=NotesForm
     success_url='/notes'     
     template_name='notes/notes_form.html'

class NotesCreateView(LoginRequiredMixin, CreateView):
     model=Note
     form_class=NotesForm
     success_url='/notes'
     template_name='notes/notes_form.html'

     def form_valid(self,form):
          self.object=form.save(commit=False)
          self.object.user=self.request.user
          self.object.save()
          return HttpResponseRedirect(self.get_success_url())
class NoteList(LoginRequiredMixin, ListView):
     model = Note
     context_object_name = 'notes'      
     template_name ='notes/notes_list.html'
     login_url='/admin/login/'

     def get_queryset(self):
          return self.request.user.notes.all()
     
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

