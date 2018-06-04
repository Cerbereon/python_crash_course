from django.db import models

# Create your models here.


class Post(models.Model):
    '''Post which user post.'''
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return a string representation of the model.'''
        return self.text