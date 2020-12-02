from django.db import models

class Blogpost(models.Model):
    post_title = models.CharField(max_length=60)
    pub_date = models.DateField(auto_now=False)
    post_text = models.TextField()