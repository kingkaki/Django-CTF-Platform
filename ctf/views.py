from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.base import View
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator

from .models import Competition, Topic, Status
from .forms import *
# Create your views here.
class IndexView(View):
	def get(self, request):
		return HttpResponse("hello ctf")

class CompetitionView(View):
	@method_decorator(login_required)
	def get(self, request, competition_name):
		competition = get_object_or_404(Competition, name=competition_name)
		topics = Topic.objects.filter(competition=competition).order_by('release_time')
		return render(request, 'ctf/index.html', {
			'competition_name' : competition_name,
			'ctfs':topics,
		})


class TopicView(View):
	@method_decorator(login_required)
	def get(self, request, topic_id):
		form = TopicForm()
		topic = get_object_or_404(Topic, pk=topic_id)
		if topic.in_progress == False:
			raise Http404('error')
		has_solved = True
		if Status.objects.filter(topic_id=topic_id, player_id=request.user.id).count() == 0:
			has_solved = False
		return render(request, 'ctf/topic.html',{
			'topic' : topic,
			'form':form,
			'has_solved' : has_solved,
			}
		)

	@method_decorator(login_required)
	def post(self, request, topic_id):
		form = TopicForm(request.POST)
		topic = get_object_or_404(Topic, pk=topic_id)
		has_solved = Status.objects.filter(topic_id=topic_id, player_id=request.user.id).count()
		if topic.in_progress == False or has_solved!=0:
			raise Http404('error')
		if form.is_valid():
			data = form.cleaned_data
			if data['flag'] == topic.flag:
				status = Status()
				status.player = request.user
				status.topic = topic
				status.score = topic.score
				status.solve_time = timezone.now()
				status.save()

				topic.solve_num +=1
				topic.save()
				return render(request, 'ctf/topic.html', {
					'topic' : topic,
					'form':form,
					'msg':('success','提交成功!'),
				})

		return render(request, 'ctf/topic.html', {
					'topic' : topic,
					'form':form,
					'msg':('error','答案错误!'),
		})



