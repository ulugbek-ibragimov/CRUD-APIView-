# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import AbstractUser
#
# from blog.models import Social
#
#
# class CustomUser(AbstractUser):
#     social = models.ManyToManyField(to=Social, verbose_name=_('Social'))
#
#
#     def __str__(self):
#         return self.username