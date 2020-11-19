from urllib import request
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import Session
# Code editor import
import sys
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import subprocess
from subprocess import STDOUT, PIPE


# Create your views here.
def home(request):
    return render(request, 'mock_site/home.html')


def session(request):
    context = {'sessions': Session.objects.all()}
    return render(request, 'mock_site/user_sessions.html')

def session_detail(request, room_name):
    return render(request, 'mock_site/session_detail.html', {
        'room_name': room_name
    })

class UserSessionListView(ListView):
    model = Session
    template_name = 'mock_site/user_sessions.html'
    context_object_name = 'sessions'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))  # This is to get the username from the URL
        return Session.objects.filter(participant=user).order_by('-start_time')


class SessionDetailView(DetailView):
    model = Session


class SessionCreateView(LoginRequiredMixin, CreateView):
    model = Session
    fields = ['title', 'note', 'invitee_email']

    def form_valid(self, form):
        form.instance.participant = self.request.user
        receiver = form.instance.invitee_email

        subject = 'Mock Interview Invitation'
        message = "Hello,\n\nYour friend {} is inviting you to join a mock interview session. Click {} to join this session.".format \
            (self.request.user, 'http://127.0.0.1:8000/session/' + str(form.instance.video_id))

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [receiver],
            fail_silently=False)

        messages.add_message(
            message=('Email sent.'),
            request=self.request,
            level=messages.SUCCESS
        )

        def get_queryset(self):
            try:
                invitee = User.objects.get(email=receiver)
                Session.objects.create(participant=invitee,
                                           title=form.instance.title,
                                           note=form.instance.note,
                                           start_time=form.instance.start_time,
                                           invitee_email=self.request.user.email)
            except:
                pass

        get_queryset(self)

        return super().form_valid(form)


# Code Editor code
def run(cmd):
    print('start')
    print(cmd)
    print('end')

    language = cmd[0]
    if language in ['python', 'ruby']:
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                )
        stdout, stderr = proc.communicate()
        return proc.returncode, stdout, stderr
    elif language == 'cpp':
        cpp_cmd = "g++ " + cmd[1] + " `pkg-config --cflags --libs opencv` -lm  -o out2;./out2"

        s1 = subprocess.check_output(cpp_cmd, shell=True)
        print("TYPE ==> ", type(s1), " size : ", sys.getsizeof(s1))
        print(s1.decode("utf-8"))
        return 1, s1, None
    elif language == 'javascript':
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                )
        stdout, stderr = proc.communicate()
        return proc.returncode, stdout, stderr
    elif language == 'java':
        proc = subprocess.Popen(cmd,
                                stdout=PIPE,
                                stderr=STDOUT)
        input = subprocess.Popen(cmd, stdin=PIPE)
        print(proc.stdout.read())
        return proc.returncode, input, input
    elif language == 'c':
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                )
        stdout, stderr = proc.communicate()
        return proc.returncode, stdout, stderr
    else:
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                )
        stdout, stderr = proc.communicate()
        return proc.returncode, stdout, stderr


def result(request):
    s = request.POST['script']
    language = request.POST['language']
    temp_path = settings.STATIC_ROOT + "/code-editor/"
    file_name = ''
    if language == 'python':
        file_name = "temp.py"
    elif language == 'java':
        file_name = "Temp.java"
        # temp_path = "Temp"
    elif language == 'ruby':
        file_name = 'temp.rb'
    elif language == 'c':
        file_name = 'temp.c'
    elif language == 'cpp':
        file_name = 'temp.cpp'
    elif language == 'javascript':
        file_name = 'temp.js'
    else:
        file_name = "Temp.java"
    temp_path += file_name
    with open(temp_path, 'w') as f:
        f.write(s)
        f.close()
    _, out, err = run([language, temp_path])

    print('*****')
    print(out)
    print('-----')
    print(err)
    print('=====')

    if out:
        out_decoded = out.decode('utf-8')
    else:
        out_decoded = ''

    if err:
        if err.decode('utf-8') != '':
            spliter = file_name + '", '
            err_decoded = err.decode('utf-8').split(spliter)[1]
        else:
            err_decoded = ''
    else:
        err_decoded = ''

    data = {'output': "{0} {1}".format(out_decoded, err_decoded)}

    return JsonResponse(data)
