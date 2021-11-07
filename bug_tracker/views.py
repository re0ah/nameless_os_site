from django.shortcuts import render
from .models import Bug, Bug_type
import datetime
from django.http import HttpResponse, JsonResponse

class Manage_bug_tracker():
	def get_bug_report(request):
		if request.user.id == None:
			return HttpResponse(status=401)

		bug_type = Bug_type.objects.get(title="На рассмотрении")
		bug = Bug(active=True,
				  title=request.POST["title"],
				  content=request.POST["text"],
				  bug_type=bug_type,
				  author=request.user
		)
		bug.save()
		return HttpResponse(status=200)

	def create_html_node(title:str,
						 content:str,
						 author:str,
						 bug_type:str,
						 date_create:str):
		return "<div class='bug-message'>"\
					"<div class='flex-row-sb wrap-bug-title-state'>"\
    					"<div class='bug-title'>"\
							f"{title}"\
    					"</div>"\
    					"<div class='bug-state'>"\
        					f"{bug_type}"\
    					"</div>"\
    				"</div>"\
    				"<div class='bug-text'>"\
						f"{content}"\
    				"</div>"\
    				"<div class='flex-row-sb bug-info-bar'>"\
    					"<div class='bug-user-created'>"\
        					f"{author}"\
    					"</div>"\
    					"<div class='bug-data-created'>"\
							f"{date_create}"\
    					"</div>"\
    				"</div>"\
    				"<div class='bug-open-comments'>Открыть комментарии</div>"\
				"</div>"\
			"<div class='bug-space-between'></div>"

	def get_bug_list_current(request):
		result = ""
		for i in Bug.objects.all():
			args = (i.title, i.content, i.author.username, i.bug_type.title, i.date_create)
			if i.bug_type.id == 1:  # На рассмотрении
				result += Manage_bug_tracker.create_html_node(*args)
			elif i.bug_type.id == 3:  # В процессе
				result += Manage_bug_tracker.create_html_node(*args)
			elif i.bug_type.id == 4:  # Отклонено
				result += Manage_bug_tracker.create_html_node(*args)

		return JsonResponse({"bug_list": result})

	def get_bug_list_solved(request):
		result = ""
		for i in Bug.objects.all():
			args = (i.title, i.content, i.author.username, i.bug_type.title, i.date_create)
			if i.bug_type.id == 2:  # Исправлено
				result += Manage_bug_tracker.create_html_node(*args)

		return JsonResponse({"bug_list": result})
