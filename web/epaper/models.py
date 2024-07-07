from django.db import models

# Create your models here.

class EPaperEmail(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    #created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '電子報訂閱'
        verbose_name_plural = '電子報訂閱'
        #ordering = ['-created_on']

    def __str__(self):
        return f'{self.email}'
    
class GuestMessage(models.Model):
    name = models.CharField('姓名', max_length=50)
    email = models.EmailField('電子郵件', max_length=100)
    subject = models.CharField('主旨', max_length=100)
    message = models.TextField('訊息', max_length=500)

    class Meta:
        verbose_name = '訪客留言'
        verbose_name_plural = '訪客留言'
        ordering = ['-id']

    def __str__(self):
        return f'{self.name} - {self.subject}'