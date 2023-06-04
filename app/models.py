from django.db import models
from django.contrib.auth.models import User



class Video (models.Model) : 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos',null=True,blank=True)
    genre = models.TextField(max_length=1000,default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'Post by : {self.user}'
    

class Recommend_Video (models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_recommend = models.TextField(max_length=1000,default='')

    def __str__(self) :
        return f'{self.user} recommended data'
    