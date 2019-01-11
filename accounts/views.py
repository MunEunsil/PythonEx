from django.shortcuts import render

# Create your views here.

# TODO : 회원가입 만들거임!
from .forms import RForm
def register(request):
    if request.method == 'POST':
        #회원가입 정보 입력 후
        user_form = RForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)                     #db에 저장하지말고 메모리에서만 만들어라! 인스턴스만 만들라는소리 비번을 아직 안했으니까
            new_user.set_password(user_form.cleaned_data['password'])   #비번 암호화 해서 저장하려는것
            new_user.save() #이때 db에 저장되는거임
            return render(request, 'registration/register_done.html', {'new_user': new_user})

    else:
        # 회원가입 정보 입력받을 때
        user_form = RForm()

    return render(request, 'registration/register.html', {'form': user_form})

        #form.as_p의 이름이 이 때 정해짐