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
			args = (i.title,
				    i.content,
					i.author.username,
					i.task_type.title,
					i.date_create.strftime("%m/%d/%Y, %H:%M:%S")
			)
			if i.task_type.id == 1:  # На рассмотрении
				result += Manage_task_tracker.create_html_node(*args)
			elif i.task_type.id == 3:  # В процессе
				result += Manage_task_tracker.create_html_node(*args)

		ret = {"task_list": result}
		if "get_hash" in request.GET:
			return JsonResponse({"md5": hashlib.md5(json.dumps(ret).encode('utf-8')).hexdigest()})
		else:
			return JsonResponse(ret)

	def create_html_node_solved(title:str,
						 		content:str,
						 		author:str,
						 		task_type:str,
						 		date_create:str,
						 		date_resolve:str,
								_id:str,
								if_last_comment:bool,
								comments):
		task = f"""<div id="wrap_task_tracker_solved">
				<div class="wrap-task-message">
				<div class="task-message">
					<div class="flex-row-sb wrap-task-title-state">
						<div class="task-title">{title}</div>
						<div class="task-state">{task_type}</div>
					</div>
					<div class="task-text-wrap">
						<div class="task-wrap-solved"><div class="task-data-created task-data-solved">Выполнено: {date_resolve}</div></div>
			<div class="task-text">
				{content}
			</div>
			</div>
					<div class="flex-row-sb task-info-bar">
						<div class="task-user-created">{author}</div>
						<div class="task-data-created">Создано: {date_create}</div>
					</div>
			</div>
					<input id="task_{_id}" class="task-open-comments" type="checkbox" checked></input>
					<label for="task_{_id}" class="task-open-comments-label"></label>
					<div class="wrap-task-comments">
			"""
		comments_html = ""
		for i in comments:
			answers_html = ""
			for j in i.answer.all():
				answers_html += f"""
					<div class="task-comment-answer">
						<div class="flex-row-sb task-info-bar">
							<div class="task-user-created">{j.author}</div>
							<div class="task-data-created">{j.date.strftime("%m/%d/%Y, %H:%M:%S")}</div>
						</div>
						<div class="task-text-wrap">
							<div class="task-text">{j.content}</div>
						</div>
						<div class="task-open-comments-label task-btn-answer">
							Ответить
						</div>
					</div>
				"""

			comments_html += f"""
					<div class="task-comments">
						<div class="flex-row-sb task-info-bar">
							<div class="task-user-created">{i.author}</div>
							<div class="task-data-created">{i.date.strftime("%m/%d/%Y, %H:%M:%S")}</div>
						</div>
						<div class="task-text-wrap">
							<div class="task-text">{i.content}</div>
						</div>
						<div class="task-open-comments-label task-btn-answer">
							Ответить
						</div>
						{answers_html}
					</div>
			"""
		if not if_last_comment:
			end = """
 			       </div>
					</div>
					<div class="task-space-between"></div>
				</div>"""
			return task + comments_html + end
		else:
			end = """
 			       </div>
					</div>
					<div class="task-space-end"></div>
				</div>"""
			return task + comments_html + end

	def get_task_list_solved(request):
		result = ""
		i = 0
		tasks = Task.objects.filter(task_type=Task_type.objects.get(id=2))
		while i < len(tasks):
			args = (tasks[i].title,
				    tasks[i].content,
					tasks[i].author.username,
					tasks[i].task_type.title,
					tasks[i].date_create.strftime("%m/%d/%Y, %H:%M:%S"),
					tasks[i].date_resolve.strftime("%m/%d/%Y, %H:%M:%S"),
					str(tasks[i].id),
					i == (len(tasks) - 1),
					tasks[i].comments.all()
			)
			result += Manage_task_tracker.create_html_node_solved(*args)
			i += 1

		ret = {"task_list": result}
		if "get_hash" in request.GET:
			return JsonResponse({"md5": hashlib.md5(json.dumps(ret).encode('utf-8')).hexdigest()})
		else:
			return JsonResponse(ret)

	def get_task_list_deffered(request):
		result = ""
		for i in Task.objects.all():
			args = (i.title,
				    i.content,
					i.author.username,
					i.task_type.title,
					i.date_create.strftime("%m/%d/%Y, %H:%M:%S")
			)
			if i.task_type.id == 5:  # Отложено
				result += Manage_task_tracker.create_html_node(*args)
			elif i.task_type.id == 4:  # Отклонено
				result += Manage_task_tracker.create_html_node(*args)

		ret = {"task_list": result}
		if "get_hash" in request.GET:
			return JsonResponse({"md5": hashlib.md5(json.dumps(ret).encode('utf-8')).hexdigest()})
		else:
			return JsonResponse(ret)
