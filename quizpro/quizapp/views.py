# from django.shortcuts import render,redirect
# from .models import Question
# from django.db import models
# from .forms import SignupForm
# from django.contrib.auth.decorators import login_required
#
# from django.contrib.auth import authenticate, login
# @login_required
#
# def quiz_disp(request):
# 	questions=Question.objects.all()
# 	# tot_mark=0
# 	if 'mark' not in request.session:
# 		request.session['mark'] = 0
#
# 	if request.method=='POST':
# 		request.session['mark'] = 0
# 		for i in questions:
# 			# i.mark=0
# 			sub_ans=request.POST.get(f'sel{i.id}')
# 			if sub_ans==i.corr_ans:
# 				request.session['mark'] += 1
# 				# i.save()
#
# 		return redirect('/quizapp/result/')
# 	return render(request,'quiz.html',{'questions': questions})
# def results_disp(request):
# 	tot_mark=0
# 	questions=Question.objects.all()
# 	tot_mark = (request.session['mark'])*10
#
# 	# for i in questions:
# 	# 	tot_mark+=i.mark
# 	#
#
# 	return render(request,'result.html', {'tot_mark': tot_mark,'questions': questions})
#
# def signup(request):
# 	if request.method == 'POST':
# 		form = SignupForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('login')
# 	else:
# 		form = SignupForm()
# 	return render(request, 'usersignup.html', {'form': form})
#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('quiz_disp')
#         else:
#             return render(request, 'userlogin.html')
#     else:
#         return render(request, 'userlogin.html')



from django.shortcuts import render, redirect,HttpResponse
from .models import Question
from django.db import models
# from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout

# @login_required
def quiz_disp(request):
    if request.user.is_authenticated:

        questions = Question.objects.all()
    # tot_mark=0
        if 'mark' not in request.session:
            request.session['mark'] = 0

        if request.method == 'POST':
            request.session['mark'] = 0
            for i in questions:
            # i.mark=0
                sub_ans = request.POST.get(f'sel{i.id}')
                if sub_ans == i.corr_ans:
                    request.session['mark'] += 1
            # i.save()

            return redirect('/quizapp/result/')
        return render(request, 'quiz.html', {'questions': questions})

    else:
        return render(request,'error.html')

def results_disp(request):
    if request.user.is_authenticated:
        questions = Question.objects.all()
        tot_mark = (request.session['mark']) * 10
        return render(request, 'result.html', {'tot_mark': tot_mark, 'questions': questions})
    else:
        return render(request,'error.html')


def signup(request):
    # if request.method == 'POST':
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.is_staff = form.cleaned_data['is_staff']
    #         user.save()
    #         return redirect('login')
    # else:
    #     form = SignupForm()
    # return render(request, 'usersignup.html', {'form': form})
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  # Set staff status to True
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request,user)
            return redirect(u_login)  # Redirect to home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'usersignup.html', {'form': form})

    # if request.method == 'POST':
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # user.password=make_password(form.cleaned_data['password'])
    #         # user.save()
    #         return redirect('/quizapp/login')
    # else:
    #     form = SignupForm()
    # return render(request, 'usersignup.html', {'form': form})

def u_login(request):
    # return render(request, 'quiz.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            # login(request, user)
            # return redirect('/quizapp/exam/')
            return redirect('quiz_disp')

    return render(request,'userlogin.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')




