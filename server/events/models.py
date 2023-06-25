from django.db import models

from django.contrib.auth import get_user_model

class Event(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    body   = models.TextField(blank=True,null=True)
    image  = models.ImageField(upload_to='events/',blank=True,null=True)
    line_up = models.CharField(max_length=255)
    entrance_fee = models.CharField(max_length=20)
    likes  = models.ManyToManyField(get_user_model(),blank=True,related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        if self.body:
            return self.body
        return str(self.pk)

class Comment(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    body = models.TextField()

    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.body