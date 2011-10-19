from django.db import models
from jaam.jaam.models import BaseModel

class BlogPost(BaseModel):
    blog
    headline
    description
    body
    author
    pass

class Blog(models.Model):
    project
    title
    subtitle
    description
    pass