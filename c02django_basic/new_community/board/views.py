from django.shortcuts import render, redirect
from .models import NewBoard
from .forms import BoardForm
from new_user.models import NewUser

# Create your views here.
def detail(request, pk):
    board = NewBoard.objects.get(pk=pk)
    return render(request, 'detail.html', {'board' : board })

def write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            username = NewUser.objects.get(pk=user_id)

            board = NewBoard()
            board.title = form.cleaned_data['title']
            board.content = form.cleaned_data['content']
            board.writer = username
            board.save()

            return redirect('/board')
    else :
        form = BoardForm()
    
    return render(request, 'write.html', {'form' : form})

def board(request):
    boards = NewBoard.objects.all().order_by('-id')
    return render(request, 'list.html', {'boards' : boards})