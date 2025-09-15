from django.shortcuts import render
from todolist.models import ToDoList
from django.http import Http404

def todolist(request):
    tdls = ToDoList.objects.all().values_list('id', 'title')
    result = [{'pk': tdl[0], 'title':tdl[1]} for i, tdl in enumerate(tdls)]
    return render(request, 'todolist.html', {'data':result})



def todo_info(request, pk):
    try:
        tdl = ToDoList.objects.get(pk=pk)
        info = {
            'title': tdl.title,
            'description': tdl.description,
            'start_date': tdl.start_date,
            'end_date': tdl.end_date,
            'is_completed': tdl.is_completed,
        }
        return render(request, 'todo_info.html', {'data':info})
    except:
        raise Http404
