from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from todo.models import Todo
from todo.forms import TodoForm
# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required
def todolist(request):
    #alltodos = Todo.objects.all()
    alltodos = Todo.objects.filter(user=request.user)
    return render(request,'todolist.html',{'todos':alltodos})
@login_required
def todoadd(request):
    todoform=TodoForm(request.POST or None)
    if todoform.is_valid():
        todo = todoform.save()
        todo.user = request.user
        todo.save()
        return redirect('todolist')
    return render(request,'todoadd.html',{'form':todoform})
@login_required
def todoedit(request,pk):
    todo = get_object_or_404(Todo,pk=pk)
    todoform = TodoForm(request.POST or None,instance=todo)
    if todoform.is_valid():
        todoform.save()
        return redirect('todolist')
    return render(request,'todoadd.html',{'form':todoform})
@login_required
def tododelete(request,pk):
    todo = get_object_or_404(Todo,pk=pk)
    if request.method=='POST':
        todo.delete()
        return redirect('todolist')
    return render(request,'tododelete.html',{'todo':todo})
