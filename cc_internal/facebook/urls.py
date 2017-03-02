from django.conf.urls import url

from . import views

urlpatterns = [ url(r'^$',views.index, name='index'),
	url(r'post/(?P<post_id>[0-9]+)/$',views.postdetail,name='post_detail'),
	url(r'createpost',views.createpost,name='createpost'),]
	
