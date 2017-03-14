from django.conf.urls import url

from . import views

urlpatterns = [ url(r'^$',views.index, name='index'),
	url(r'posts/(?P<post_id>[0-9]+)/$',views.postdetail,name='postdetail'),
	url(r'createpost',views.createpost,name='createpost'),
	url(r'edit/(?P<post_id>[0-9]+)/$',views.editpost,name='editpost'),]
	
