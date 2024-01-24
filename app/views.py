from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.
def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST'and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            MUFDO.set_password(password)
            MUFDO.save()
            MPFDO=pfd.save(commit=False)
            MPFDO.user_name=MUFDO
            MPFDO.save()

            send_mail('Registration',
                      'Thank you your Registration is Successful..',
                      'brahmeswarammaathinti@gmail.com',
                      [MUFDO.email],
                      fail_silently=True
            )
            return HttpResponse('Registaration is successfull.....')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'registration.html',context=d)

