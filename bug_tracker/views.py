from django.shortcuts import render
from .models import Bug, Bug_type
import datetime
from django.http import JsonResponse

def get_bug_report(request):
	if request.user.id == None:
		return JsonResponse({"state": False,
							 "error": "Для отправки сообщения об ошибке необходимо быть авторизованным."
		})
	bug_type = Bug_type.objects.get(title="На рассмотрении")
	bug = Bug(active=True,
			  title=request.POST["title"],
			  content=request.POST["text"],
			  bug_type=bug_type,
			  author=request.user
	)
	bug.save()
	return JsonResponse({"state": True})
