import django
from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.http import JsonResponse

from django.contrib.auth.models import User
import urllib

import os
from page.models import Page

class Home_view(TemplateView):

	template_name = "home.html"

	def get(self, request):
		page = Manage.get_page_data(request)
		try:
			page_now_main = Manage.get_page_branch(page)[-2].title
		except IndexError:
			page_now_main = False

		try:
			user = User.objects.get(id=request.user.id)
		except:
			user = None

		try:
			ajax_checkbox = request.COOKIES["ajax_checkbox"] == "true"
		except:
			ajax_checkbox = False

		try:
			edit_checkbox = request.COOKIES["edit_checkbox"] == "true"
		except:
			edit_checkbox = False

		page.css.open(mode='r')
		page_css_text= page.css.read()
		page.css.close()

		page.js.open(mode='r')
		page_js_text= page.js.read()
		page.js.close()
		print(page.js.url)

		if ("is_ajax" in request.GET) & ajax_checkbox:
			result = {
				"title": page.title,
				"html": page.html,
				"css_url":  page.css.url,
				"css_text": page_css_text,
				"js_url":  page.js.url,
				"js_text": page_js_text,
				"content_list": Manage.get_html_content_list_ajax(page),
				"is_ajax": ajax_checkbox,
				"is_edit": edit_checkbox,
			}
			return JsonResponse(result)
		
		ctx = {
			"title": page.title,
			"html": page.html,
			"css_url":  page.css.url,
			"css_text": page_css_text,
			"js_url":  page.js.url,
			"js_text": page_js_text,
			"page_now_main": page_now_main,
			"user": user,
			"is_ajax": ajax_checkbox,
			"is_edit": edit_checkbox
		}
		print(page.title)
		if ajax_checkbox:
			ctx["content_list"] = Manage.get_html_content_list_ajax(page)
		else:
			ctx["content_list"] = Manage.get_html_content_list(page)
		return render(request, self.template_name, ctx)

class Manage():
	def get_page_data(request):
		try:
			get = int(request.GET["page"])
		except:
			get = 1
		page = Page.objects.get(id=get)
		return page

	def get_page_branch(page):
		result = [page]
		master = page
		while master != master.master_page:
			master = master.master_page
			result.append(master)
		return result

	def get_page_list(page):
		def test(i):
			tmp = []
			for slave in i.slave_pages.all():
				if_selected = slave.title in result_titles
				if_selected_master = slave.title == page.title
				tmp.append({
							slave.id: {
									"id": slave.id,
									"title": slave.title,
									"element": slave,
									"if_selected": if_selected,
									"if_selected_master": if_selected_master,
									"selected": test(slave)
								 }
						 })
			return tmp

		result = Manage.get_page_branch(page)
		result_titles = [i.title for i in result]
		return test(result[len(result)-1])

	def get_html_content_list_ajax(page):
		html_content_list = ""
		content_list = Manage.get_page_list(page)
		for el in content_list:
			for key, val in el.items():
				if val["if_selected"]:
					for i in val["selected"]:
						key2, val2 = tuple(i.items())[0]
						if val2["if_selected_master"]:
							html_content_list += f"<a class=\"box-element box-element-inner selected selected-master\" onclick=\"ajaxUpdatePage('{key2}')\">{val2['title']}</a>"
						else:
							html_content_list += f"<a class=\"box-element box-element-inner selected\" onclick=\"ajaxUpdatePage('{key2}')\">{val2['title']}</a>"
					if val["if_selected_master"]:
						html_content_list += f"<a class=\"box-element selected selected-master\" onclick=\"ajaxUpdatePage('{key}')\">{val['title']}</a>"
					else:
						html_content_list += f"<a class=\"box-element selected\" onclick=\"ajaxUpdatePage('{key}')\">{val['title']}</a>"
				else:
					html_content_list += f"<a class=\"box-element\" onclick=\"ajaxUpdatePage('{key}')\">{val['title']}</a>"

		return html_content_list

	def get_html_content_list(page):
		html_content_list = ""
		content_list = Manage.get_page_list(page)
		for el in content_list:
			for key, val in el.items():
				if val["if_selected"]:
					for i in val["selected"]:
						key2, val2 = tuple(i.items())[0]
						if val2["if_selected_master"]:
							html_content_list += f"<a class=\"box-element box-element-inner selected selected-master\" href='/?page={key2}'>{val2['title']}</a>"
						else:
							html_content_list += f"<a class=\"box-element box-element-inner selected\" href='/?page={key2}'>{val2['title']}</a>"
					if val["if_selected_master"]:
						html_content_list += f"<a class=\"box-element selected selected-master\" href='/?page={key}'>{val['title']}</a>"
					else:
						html_content_list += f"<a class=\"box-element selected\" href='/?page={key}'>{val['title']}</a>"
				else:
					html_content_list += f"<a class=\"box-element\" href='/?page={key}'>{val['title']}</a>"

		return html_content_list

	def save_page(request):
		if request.user.id == None:
			return JsonResponse({})
		page = Page.objects.get(id=int(request.POST["page"]))
		page.html = request.POST["data"]
		page.title = request.POST["page_name"]

		page.css.open(mode='w')
		page.css.write(request.POST['css'])
		page.css.close()

		page.js.open(mode='w')
		page.js.write(request.POST['js'])
		page.js.close()

		page.save()
		return JsonResponse({})
