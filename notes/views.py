#from django.shortcuts import render
#from django.http import Http404
from typing import List
from django.http.response import HttpResponseRedirect
from django.db.models.query import QuerySet
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import NotesForm
from .models import Notes
# Create your views here.

class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = "/admin"

class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url ="/admin"

class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    #fields = ['title','text']
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/admin'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()
    
#def list (request):
    #all_notes = Notes.objects.all()
  #  return render(request, 'notes/notes_list.html',{'notes': all_notes})

class NotesDetailView(LoginRequiredMixin,DetailView):
    model = Notes
    context_object_name = "note"
    login_url ='/admin'
#def detail(request, pk):
 #   try:
     #   note = Notes.objects.get(pk=pk)
 #   except Notes.DoesNotExist:
       # raise Http404("Note does not exist")
    #return render(request, 'notes/notes_detail.html', {'note' : note})