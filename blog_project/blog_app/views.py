from django.shortcuts import render


# Create your views here.
def admin_page(request):
    return render(request, "admin.html")
def board_page(request):
    return render(request, "board.html")
def client_page(request):
    return render(request, "client.html")
def write_page(request):
    return render(request, "write.html")