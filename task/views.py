from django.shortcuts import render
from .models import Task, Task_type
import datetime
from django.http import HttpResponse, JsonResponse
import json
import hashlib

class Manage_task_tracker():
	def get_task_offer(request):
		if request.user.id == None:
			return HttpResponse(status=401)

		task_type = Task_type.objects.get(title="На рассмотрении")
		task = Task(active=True,
				    title=request.POST["title"],
				    content=request.POST["text"],
				    task_type=task_type,
				    author=request.user
		)
		task.save()
		return HttpResponse(status=200)

	def create_html_node(title:str,
						 content:str,
						 author:str,
						 task_type:str,
						 date_create:str):
		return "<div class='task-message'>"\
					"<div class='flex-row-sb wrap-task-title-state'>"\
    					"<div class='task-title'>"\
							f"{title}"\
    					"</div>"\
    					"<div class='task-state'>"\
        					f"{task_type}"\
    					"</div>"\
    				"</div>"\
    				"<div class='task-text'>"\
						f"{content}"\
    				"</div>"\
    				"<div class='flex-row-sb task-info-bar'>"\
    					"<div class='task-user-created'>"\
        					f"{author}"\
    					"</div>"\
    					"<div class='task-data-created'>"\
							f"{date_create}"\
    					"</div>"\
    				"</div>"\
    				"<div class='task-open-comments'>Открыть комментарии</div>"\
				"</div>"\
			"<div class='task-space-between'></div>"

	def get_task_list_current(request):
		result = ""
		for i in Task.objects.all():
			args = (i.title, i.content, i.author.username, i.task_type.title, i.date_create)
			if i.task_type.id == 1:  # На рассмотрении
				result += Manage_task_tracker.create_html_node(*args)
			elif i.task_type.id == 3:  # В процессе
				result += Manage_task_tracker.create_html_node(*args)

		ret = {"task_list": result}
		if "get_hash" in request.GET:
			return JsonResponse({"md5": hashlib.md5(json.dumps(ret).encode('utf-8')).hexdigest()})
		else:
			return JsonResponse(ret)

	def get_task_list_solved(request):
		result = ""
		for i in Task.objects.all():
			args = (i.title, i.content, i.author.username, i.task_type.title, i.date_create)
			if i.task_type.id == 2:  # Решено
				result += Manage_task_tracker.create_html_node(*args)

		ret = {"task_list": result}
		if "get_hash" in request.GET:
			return JsonResponse({"md5": hashlib.md5(json.dumps(ret).encode('utf-8')).hexdigest()})
		else:
			return JsonResponse(ret)

	def get_task_list_deffered(request):
		result = ""
		for i in Task.objects.all():
			args = (i.title, i.content, i.author.username, i.task_type.title, i.date_create)
			if i.task_type.id == 5:  # Отложено
				result += Manage_task_tracker.create_html_node(*args)
			elif i.task_type.id == 4:  # Отклонено
				result += Manage_task_tracker.create_html_node(*args)

		ret = {"task_list": result}
		if "get_hash" in request.GET:
			return JsonResponse({"md5": hashlib.md5(json.dumps(ret).encode('utf-8')).hexdigest()})
		else:
			return JsonResponse(ret)
