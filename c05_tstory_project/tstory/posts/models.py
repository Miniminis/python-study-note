from django.db import models
from helpers.models import BaseModel
from users.models import User

# Create your models here.
class TPost(BaseModel):
    # from helpers : created_at, modifed_at 
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=255, blank=False)
    content = models.TextField(verbose_name='content')
    image = models.ImageField(verbose_name='image', blank=True, null=True)      # pillow lib required

    def __str__(self):
        return "%s written by %s" % (self.title, self.writer)