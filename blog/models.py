from django.conf import settings        #????
from django.db import models            #моделька как и в монго
from django.utils import timezone       #импорт модуля для времени

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #Название
    text = models.TextField() #обычный текст
    created_date = models.DateTimeField(default=timezone.now) #дату берёт с сегодня
    published_date = models.DateTimeField(blank=True, null=True) #берёт дату хз откуда

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title