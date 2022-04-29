from django.shortcuts import render, redirect
from .models import Posts
from .forms import AddPostForm
from django.core.mail import EmailMessage

# Create your views here.
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Posts.objects.create(**form.cleaned_data)
                return redirect('add_page')
            except:
                form.add_error(None, 'Error in filling')
    else:
        form = AddPostForm()
    return render(request, 'lecture10_app/addpage.html', {'tittle': 'Мақаланы қосу', 'form' : form})

def send_message(request):
    email = EmailMessage(
        'Hello',
        'Body',
        '200103297@stu.sdu.edu.kz',
        ['akzholnurik2@gmail.com'],
        headers={'Message-ID': 'foo'}
    )
    email.send(fail_silently=False)
    return render(request, 'lecture10_app/successfull.html')