import json

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserInfo
from django.contrib.auth.models import User

# 个人信息的编辑, HttpResponseRedirect实现URL转向，修改用户信息后，就跳转到用户的自己的信息来的
from django.http import HttpResponseRedirect
from .forms import UserProfileForm, UserInfoForm, UserForm

# 注册后跳转页面导入
from django.urls import reverse

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Wellcome You.You have been authenticated successfully")
            else:
                return HttpResponse("Sorry. Your username or password is not right.")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})

def user_update_pwd(request):
    user = request.user

    password_dict = json.loads(request.body)

    old_password = password_dict.get('old_password')
    new_password1 = password_dict.get('new_password1')
    new_password2 = password_dict.get('new_password2')

    if not all([old_password, new_password1, new_password2]):
        return JsonResponse({'code': 400, 'msg': "参数错误"})

    if old_password == new_password1:
        return JsonResponse({'code': 400, 'msg': '设置密码不可以和旧密码一样'})

    if new_password1 != new_password2:
        return JsonResponse({'code': 400, 'msg': '两次密码不一致'})

    is_true_password = check_password(old_password, user.password)
    if not is_true_password:
        return JsonResponse({'code': 400, 'msg': '当前密码输入不正确'})

    user.set_password(new_password1)
    user.save()
    ret = JsonResponse({'code': 200, 'msg': '修改密码成功'})
    # ret.delete_cookie('username')
    return ret

def user_logout(request):
    login_form = LoginForm()
    return render(request, "account/login.html", {"form": login_form})

def user_register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_from.save(commit=False) # 不保存到数据库，仅生成数据模型对象
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            # return HttpResponse("successfully")
            return HttpResponseRedirect(reverse("account:user_login"))
        else:
            return HttpResponse("sorry, your can not register.")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form": user_form, "profile": userprofile_form})

@login_required()
def myself(request):
    """展示个人信息的视图函数"""
    userprofile = UserProfile.objects.get(user=request.user) \
        if hasattr(request.user, 'userprofile') else UserProfile.objects.create(user=request.user)

    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user, 'userinfo') else \
        UserInfo.objects.create(user=request.user)

    return render(request, "account/myself.html",
                  {"user": request.user,
                   "userinfo": userinfo,
                   "userprofile": userprofile})

@login_required(login_url='/account/login/')
def mysql_edit(request):
    userprofile = UserProfile.objects.get(user=request.user) if \
        hasattr(request.user, 'userprofile') else \
        UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if \
        hasattr(request.user, 'userinfo') else \
        UserInfo.objects.create(user=request.user)
    if request.method == "POST":
        # 三个表对象实例化
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid() \
            * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data

            request.user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo_school = userinfo_cd['school']
            userinfo_company = userinfo_cd['company']
            userinfo_profession = userinfo_cd['profession']
            userinfo_address = userinfo_cd['address']
            userinfo_aboutme = userinfo_cd['aboutme']
            request.user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"birth": userprofile.birth, "phone": userprofile.phone})
        userinfo_form = UserInfoForm(initial={"school": userinfo.school,
                                              "company": userinfo.company,
                                              "profession": userinfo.profession,
                                              "address": userinfo.address,
                                              "aboutme": userinfo.aboutme})
        return render(request, "account/myself_edit.html",
                      {"user_form": user_form,
                       "userprofile_form": userprofile_form,
                       "userinfo_form": userinfo_form
                      })

@login_required(login_url='/account/login/')
def my_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id) if \
            hasattr(request.user, 'userinfo') else \
            UserInfo.objects.create(user=request.user)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request, 'account/imagecrop.html',)