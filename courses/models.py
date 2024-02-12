from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    preview_image = models.ImageField(upload_to='course_images/', **NULLABLE, verbose_name='картинка')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='студенты', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
