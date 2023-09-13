from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Board
from .serializers import BoardSerializer
from .forms import PostForm


# Create your views here.
# Board 데이터베이스 불러오기
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


# 게시판 페이지
def board_page(request):
    posts = Board.objects.all().order_by("-created_at")
    category = "none"
    return render(request, "board.html", {"posts": posts, "category": category})


# 카테고리별 게시판 페이지
def board_categorized(request, category):
    categorized_posts = Board.objects.filter(category_name=category).order_by(
        "-created_at"
    )
    context = {"posts": categorized_posts, "category": category}
    return render(request, "board.html", context)


def login_page(request):
    return render(request, "login.html")


############################################################################## 09/12추가5
# 회원 가입
@csrf_exempt
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == "POST":
        # password와 confirm에 입력된 값이 같다면
        if request.POST["password"] == request.POST["confirm"]:
            # user 객체를 새로 생성
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password"]
            )
            # 로그인 한다
            # auth.login(request, user)
            return redirect("/")
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, "signup.html")


# 로그인
@csrf_exempt
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == "POST":
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST["username"]
        password = request.POST["password"]

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)

        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect("/")
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(
                request, "login.html", {"error": "username or password is incorrect."}
            )
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, "login.html")


# 로그 아웃
@csrf_exempt
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == "POST":
        auth.logout(request)
        return redirect("/")

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, "login.html")


############################################################################## 09/12추가5


# post 만드는 기능 구현 (임시저장 기능 구현 및 forms.py와 연동)
def write_page(request):
    if request.method == "POST":
        form = Board(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if "save_draft" in request.POST:
                post.is_draft = True
            else:
                post.is_draft = False
            post.save()
            return redirect("board")  # 게시글 목록 페이지로 리디렉션
    else:
        form = PostForm()

    return render(request, "write.html", {"form": form})


# 게시글 조회 기능 구현
def post_page(request, post_id):
    post = Board.objects.get(id=post_id)
    next_post = (
        Board.objects.filter(created_at__gt=post.created_at)
        .order_by("created_at")
        .first()
    )
    prev_word = (
        Board.objects.filter(created_at__lt=post.created_at)
        .order_by("created_at")
        .last()
    )
    context = {"post": post, "next_post": next_post, "prev_word": prev_word}
    return render(request, "post.html", context)


# 수정하기
def edit(request, post_id):
    post_write = get_object_or_404(post_id=post_id)
    if request.method == "POST":
        update_form = PostForm(request.POST, instance=post_write)
        if update_form.is_valid():
            update_form.save()
        return redirect("index")
    else:
        update_form = PostForm(instance=post_write)
        return render(request, "edit.html", {"edit_form": update_form})


# 삭제하기
def delete(request, post_id):
    post_write = get_object_or_404(Board, id=post_id)
    post_write.delete()
    return redirect("board")
