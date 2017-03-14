from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from .models import FB_Post, Geography
from django.template import loader
from .forms import *
from datetime import date


def index(request):
	post_list = FB_Post.objects.order_by('-post_date')
	template = loader.get_template('facebook/index.html')
	context = {'post_list' : post_list}
	return HttpResponse(template.render(context, request))
	
def postdetail(request,post_id):
	post = get_object_or_404(FB_Post,pk=post_id)
	return render(request,'facebook/postdetail.html',{'post' : post})
	
def createpost(request):
	if request.method == 'POST':
		form = FbCreateForm(request.POST)
		if form.is_valid():
			clean = form.cleaned_data
			new_post = FB_Post.code_and_create(clean['geography'],clean['issue'],clean['subissue'],clean['post_type'],clean['post_date'],clean['alert_id'])
			new_post.save()
			return HttpResponseRedirect(new_post.get_edit_url())
	else:
		form = FbCreateForm(initial={'geography' : Geography.objects.filter(option_code='US')[0], 'post_date' : date.today()})
	
	return render(request,'facebook/createpost.html',{'form' : form})
	
def editpost(request,post_id):
	post = get_object_or_404(FB_Post,pk=post_id)
	if request.method == 'POST':
		form = FbLinkForm(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponseRedirect(post.get_absolute_url())
	else:
		form = FbLinkForm(instance=post)
	
	return render(request,'facebook/editpost.html',{'form' : form, 'post' : post})