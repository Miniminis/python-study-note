from django.shortcuts import render, redirect
from .models import NewBoard
from .forms import BoardForm
from new_user.models import NewUser
from django.http import Http404
from django.core.paginator import Paginator



# Create your views here.
def detail(request, pk):
    try: 
        board = NewBoard.objects.get(pk=pk)
    except:
        raise Http404('게시글을 찾을 수 없습니다!')
        
    return render(request, 'detail.html', {'board' : board })

def write(request):
    if not request.session.get('user'): 
        return redirect('/newuser/login')

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
    all_boards = NewBoard.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 3)    # num per page

    boards = paginator.get_page(page)
    return render(request, 'list.html', {'boards' : boards})

    