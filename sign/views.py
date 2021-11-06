import django
from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.http import JsonResponse

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

import os

class Sign_in_view(TemplateView):
	template_name = "sign_in.html"

	def get(self, request):
		ctx = {"user": ""}
		return render(request, self.template_name, ctx)

	def post(self, request):
		ctx = {"user": request.POST["user"]}
		try:
			user = User.objects.get(username=request.POST["user"])
		except:
			try:
				user = User.objects.get(email=request.POST["user"])
			except:
				ctx["error"] = "Пользователя не существует"
				return render(request, self.template_name, ctx)

		user = authenticate(username=request.POST["user"], password=request.POST["password"])
		if user == None:
			ctx["error"] = "Неправильный пароль"
			return render(request, self.template_name, ctx)
		else:
			login(request, user)
			return HttpResponseRedirect("/")

class Sign_up_view(TemplateView):

	template_name = "sign_up.html"

	def get(self, request):
		ctx = {}
		try:
			ctx["error"] = request.GET["error"]
		except:
			pass
		
		return render(request, self.template_name, ctx)

	def post(self, request):
		ctx = {"username": request.POST['username'],
			   "email": request.POST['email'],
		}

		try:
			user = User.objects.get(username=request.POST["username"])
			ctx["error"] = "Имя пользователя занято"
			return render(request, self.template_name, ctx)
		except User.DoesNotExist:
			pass

		try:
			user = User.objects.get(username=request.POST["email"])
			ctx["error"] = "E-mail занят"
			return render(request, self.template_name, ctx)
		except User.DoesNotExist:
			pass

		if request.POST["password"] != request.POST["rep_password"]:
			ctx["error"] = "Пароли не совпадают"
			return render(request, self.template_name, ctx)


		new_user = User(username=request.POST["username"],
						email=request.POST["email"],
						is_active=True,
		)
		new_user.set_password(request.POST["password"])
		new_user.save()

		login(request, new_user)
		return HttpResponseRedirect("/")

def redirect_logout(response):
	logout(response)
	return HttpResponseRedirect("/")

