from django.db import models
from django.contrib.auth.models import User
from jaam.journalism.models import BaseModel
from jaam.projects.models import Project
from ckeditor.fields import RichTextField

class Blog(BaseModel):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('jaam.blog.views.blog_details', (), {
            'project_slug': self.project.slug,
            'blog_title_slug': self.slug,
        })

class BlogPost(BaseModel):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    body = RichTextField()
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.headline

    @models.permalink
    def get_absolute_url(self):
        return ('jaam.blog.views.post_details', (), {
            'project_slug': self.blog.project.slug,
            'blog_title_slug': self.blog.slug,
            'blog_post_slug': self.slug,
        })
