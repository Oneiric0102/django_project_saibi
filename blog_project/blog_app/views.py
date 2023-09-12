from django.shortcuts import render, redirect
from .models import Board
from .forms import PostForm


# Create your views here.
def admin_page(request):
    return render(request, "admin.html")
def board_page(request):
    return render(request, "board.html")
def client_page(request):
    return render(request, "client.html")
# def write_page(request):
#     return render(request, "write.html")

# post 만드는 기능 구현 (임시저장 기능 구현 및 forms.py와 연동)
def write_page(request):
    if request.method == 'POST':
        form = Board(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if 'save_draft' in request.POST:
                post.is_draft = True
            else:
                post.is_draft = False
            post.save()
            return redirect('board')  # 게시글 목록 페이지로 리디렉션
    else:
        form = PostForm()

    return render(request, 'write.html', {'form': form})