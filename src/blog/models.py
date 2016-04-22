from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    # author = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        # return "/blog/%s" %(self.id)
        return reverse("detail", kwargs={"slug": self.slug})

    def create_slug(instance, new_slug=None):
        slug = slugify(instance.title)
        if new_slug is not None:
            slug = new_slug
        qs = Post.objects.filter(slug=slug).order_by("-id")
        exists = qs.exists()
        if exists:
            new_slug = "%s-%s" % (slug, qs.first().id)
            return create_slug(instance, new_slug=new_slug)
        return slug
