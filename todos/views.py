from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from todos.customforms import TodoForm
from todos.models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils.timezone import datetime
from django.contrib import messages
from user.models import Profile
from django.views.generic import UpdateView,DeleteView
# Create your views here.
class TodoListView(LoginRequiredMixin,TemplateView):
    template_name = 'todos/index.html'
    title = 'Todos List'
    def get(self,request):
        if Todo.objects.filter(user=request.user).count() > 0:
            todos = Todo.objects.filter(user=request.user).all()
        else:
            todos = False
        return render(request,self.template_name,{'title':self.title,'todos':todos})

class CreateTodoView(LoginRequiredMixin,TemplateView):
    template_name = 'todos/create.html'
    title = 'Create Todos'
    success_url = reverse_lazy('todos:home')
    def get(self,request):
        form = TodoForm()
        return render(request,self.template_name,{'title':self.title,'forms':form})
    
    def post(self,request):
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            status = form.cleaned_data.get('status')
            todo = Todo(user=request.user,title=title,status=status)
            todo.save()
            return redirect(self.success_url)
        return render(request,self.template_name,{'title':self.title,'forms':form})

@login_required
def markDone(request,pk=None):
    if request.method == 'GET':
        todo = get_object_or_404(Todo,id=pk)
        if todo:
            title = todo.title
            todo.delete()
            messages.success(request,f'{title} is done successfully.')
            return redirect('todos:home')
        messages.warning(request,'something went wrong!')
        return redirect('todos:home')

class TodoUpdateView(UpdateView):
    """
    for updating the todos made by user
    """
    model = Todo
    fields = [
        'title',
        'status',
    ]
    template_name='todos/create.html'
    context_object_name = 'forms'
    success_url = reverse_lazy('todos:home')

class TodoRemoveView(LoginRequiredMixin,DeleteView):
    model = Todo
    success_url = reverse_lazy('todos:home')
    template_name = 'todos/todo_confirm_delete.html'
    context_object_name = 'todo'
    
