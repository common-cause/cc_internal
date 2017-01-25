from django.db import models

# Create your models here.

class FB_Post(models.Model):
	geography = models.CharField(max_length = 63)
	issue_area = models.CharField(max_length = 63)
	subissue = models.CharField(max_length = 63)
	post_type = models.CharField(max_length=63)
	post_date = models.DateTimeField()
	alert_id = models.IntegerField()
	link_to_post = models.CharField(max_length=127)
	post_num_of_day = models.IntegerField()
	subsource = models.CharField(max_length=31)
	fb_link = models.CharField(max_length=63)
	fb_shortlink = models.CharField(max_length=31)
	
class Issue(models.Model):
	option_name = models.CharField(max_length=31)
	option_code = models.CharField(max_length=3)
	
	
class Subissue(models.Model):
	issue = models.ForeignKey(Issue,on_delete=models.CASCADE)
	option_name = models.CharField(max_length=31)
	option_code = models.CharField(max_length=3)
	                                                                                                                                                                                                                                                                                                                                                                                                    