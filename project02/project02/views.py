from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.http import urlencode

from config.settings import UPLOAD_DIR
from frame.custdb import UserDB
from frame.error import ErrorCode


def index(request):

    return render(request, 'index.html')
def index2(request):

    return render(request, 'index2.html')
def index3(request):

    return render(request, 'index3.html')
def index4(request):

    return render(request, 'index4.html')
def login(request):

    return render(request, 'login.html')


def logout(request):
    if request.session['suser'] != None:
        del request.session['suser'];
    return render(request, 'index.html')

def quit(request):
    id = request.GET['id'];
    user = UserDB().selectone(id);
    context = {'u': user};
    return render(request, 'quit.html',context)
def quitimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    try:
        user = UserDB().selectone(id);
        if pwd == user.pwd:
            UserDB().delete(id)
        else:
            raise Exception;
        return render(request, 'quitok.html');
    except:
        context = {
            'msg': ErrorCode.e0003
        };
        return render(request, 'quit.html', context);

def loginimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    next = 'index.html'
    try:
        user = UserDB().selectone(id);
        if pwd == user.pwd:
            request.session['suser'] = {'id': user.id , 'name':user.name };
            context = {
                'loginuser': user
            };
        else:
            raise Exception;
    except:
        next = 'login.html'
        context = {
            'msg': ErrorCode.e0003
        };

    return render(request, next, context);

def signup(request):

    return render(request, 'signup.html')
def registerok(request):
    user = UserDB().selectone(id);
    context = {'u': user};
    return render(request, 'registerok.html',context)
def useraddimpl(request):

    id = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    email = request.POST['email'];

    if id != '' and pwd != ''and name != ''and email != '':
        try:
            UserDB().insert(id, pwd, name,'basic.png',email);
            user = UserDB().selectone(id)
            context = {
                'u': user
            };
            return render(request, 'registerok.html', context);
        except:
            context = {
                'msg': ErrorCode.e0001
            };
            return render(request, 'signup.html', context);
    else:
        context = {
            'msg': ErrorCode.e0004
        };
        return render(request, 'signup.html', context);

def quitok(request):
    del request.session['suser'];
    return render(request, 'quitok.html')

def profile(request):
    id = request.GET['id'];
    user = UserDB().selectone(id);
    context = {'u': user};
    return render(request, 'profile.html',context)


def ud_profile(request):
    id = request.GET['id'];
    user = UserDB().selectone(id);
    context = {'u': user};
    return render(request, 'ud_profile.html',context)

def userupdateimpl(request):
    id  = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    oldimg = request.POST['oldimg'];
    email = request.POST['email'];
    imgname = '';

    if 'newimg' in request.FILES:
        newimg = request.FILES['newimg']
        imgname = newimg._name

        fp = open('%s/%s' % (UPLOAD_DIR, imgname), 'wb')
        for chunk in newimg.chunks():
            fp.write(chunk);
            fp.close();
    else:
        imgname = oldimg;
    UserDB().update(id,pwd,name, imgname,email);
    qstr = urlencode({'id': id})
    return HttpResponseRedirect('%s?%s' % ('profile', qstr))

