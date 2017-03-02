from django.forms import ModelForm
from .models import FB_Post

class FbCreateForm(ModelForm):
	class Meta:
		model = FB_Post
		fields = ['geography','issue','subissue','post_type','post_date','alert_id']
		
class FbLinkForm(ModelForm):
	class Meta:
		model = FB_Post
		fields =['link_to_post']
		
		
		