from django.db import models
import requests

# Create your models here.
	
class Issue(models.Model):
	option_name = models.CharField(max_length=31)
	option_code = models.CharField(max_length=3)
	
	def __str__(self):
		return self.option_name
	
	
class Subissue(models.Model):
	issue = models.ForeignKey(Issue,on_delete=models.CASCADE)
	option_name = models.CharField(max_length=63)
	option_code = models.CharField(max_length=3)
	
	def __str__(self):
		return self.option_name
		
class Geography(models.Model):
	option_code = models.CharField(max_length=2)
	
	def __str__(self):
		return self.option_code

class FB_Post(models.Model):
	geography = models.ForeignKey(Geography,on_delete=models.CASCADE)
	issue = models.ForeignKey(Issue,on_delete=models.CASCADE)
	subissue = models.ForeignKey(Subissue,on_delete=models.CASCADE)
	post_type = models.CharField(max_length=127)
	post_date = models.DateTimeField()
	alert_id = models.IntegerField()
	link_to_post = models.CharField(max_length=127)
	post_num_of_day = models.IntegerField(editable=False)
	subsource = models.CharField(max_length=31,editable=False)
	fb_link = models.CharField(max_length=127,editable=False)
	fb_shortlink = models.CharField(max_length=31,editable=False)
	
	def __str__(self):
		return self.subsource
	
	@classmethod
	def code_and_create(cls,geography,issue,subissue,post_type,post_date,alert_id):
		posts_on_day = len(cls.filter(post_date=post_date))
		post_num_of_day = posts_on_day + 1
		subsource = 'fb-' + post_date.isoformat() + '-' + '00'[0:2-len(str(post_num_of_day))] + (str(post_num_of_day)
		fb_link = 'https://secure2.convio.net/comcau/site/Advocacy?cmd=display&page=UserAction&id=%s&s_src=%s&s_subsrc=%s' % (str(alert_id), str(alert_id), subsource)
		fb_shortlink = requests.get('https://api-ssl.bit.ly/v3/shorten',params={'access_token' : '54af1938f5e34d66cfec2c1a734968389c00983d' 'format' : 'txt' 'longUrl' : fb_link}).text
		return cls(geography=geography,issue=issue,subissue=subissue,post_type=post_type,post_date=post_date,alert_id=alert_id,post_num_of_day = post_num_of_day,subsource=subsource,fb_link=fb_link,fb_shortlink=fb_shortlink)
		
		