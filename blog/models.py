from tabnanny import verbose

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
User = get_user_model()

class Profile(models.Model):
    firstname = models.CharField(_('User name'), max_length=100, null=True, blank=True)
    lastname = models.CharField(_('User lastname'), max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to="profile", null=True, blank=True)
    facebook = models.URLField(_('Facebook'), blank=True, null=True)
    instagram = models.URLField(_('Instagram'), blank=True, null=True )
    twitter = models.URLField(_('Twitter'), blank=True, null=True)
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profile')

class Media(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    file = models.FileField(_('File'), upload_to='files')

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media')

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(_('Title'),max_length=255)
    order = models.IntegerField(_('Order'),default=0)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name=_('Author'))
    created_at = models.DateTimeField(_('Created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated_at'), auto_now=True)
    body = models.TextField(_('Body'))
    image = models.ManyToManyField(to=Media, verbose_name=_('Image'))
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name=_('Category'),
                                 related_name='posts')
    tags = models.ManyToManyField(to=Tag, verbose_name=_('Tags'), through="TagPost")

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
            return self.title

class TagPost(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name=_('Tag'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('Post'))

    class Meta:
        verbose_name = _('Tag Post')
        verbose_name_plural = _('Tag Posts')

    def __str__(self):
        return 'ManyToManyTable'
