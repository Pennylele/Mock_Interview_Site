from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
)
from .models import Session


# Create your views here.
def home(request):
    return render(request, 'mock_site/home.html')


def session(request):
	context = {'sessions': Session.objects.all()}
	return render(request, 'mock_site/user_sessions.html')


class UserSessionListView(ListView):
	model = Session
	template_name = 'mock_site/user_sessions.html'
	context_object_name = 'sessions'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username')) # This is to get the username from the URL
		return Session.objects.filter(participant=user).order_by('-start_time')


class SessionDetailView(DetailView):
	model = Session


class SessionCreateView(LoginRequiredMixin, CreateView):
	model = Session
	fields = ['title', 'note']

	def form_valid(self, form):
		form.instance.participant = self.request.user
		return super().form_valid(form)




