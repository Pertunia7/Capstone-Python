from django.db import models
# Create your models here .
class Topic(models.Mode):

 topic_name = models.CharField(max_length = 256)

def _str_(self):
   
   return self.topic_name
   
class Article(models.Model):

      title = models.CharField(max_length =256)
      topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='articles')
      article = models.TextField()
      created = models.DateTimeField(auto_now_add=True)

      def _str_(self):
       return self.title 