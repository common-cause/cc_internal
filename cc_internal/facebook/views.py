from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import FB_Post
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
	form = FbCreateForm(initial={'geography' : 'US', 'date' : date.today().isoformat()})
	return render(request,'facebook/createpost.html',{'form' : form})