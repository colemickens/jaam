from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from jaam.projects.models import Project
from jaam.photos.models import Photo, PhotoGallery, PhotoGalleryItem
from jaam.videos.models import Video, VideoGallery
from jaam.stories.models import Story
from jaam.blog.models import Blog, BlogPost
from easy_thumbnails.files import get_thumbnailer
import ast

class ProjectResource(ModelResource):
    covergallery = fields.ForeignKey('jaam.api.resources.PhotoGalleryResource', 'coverGallery', null=True)
    class Meta:
        queryset = Project.published_objects.exclude(coverGallery__published=False);
        allowed_methods = ['get']
        filtering = {
            'pk': ALL,
            'id': ALL,
            'slug': ALL,
            'covergallery': ('isnull'),
        }

class PhotoGalleryResource(ModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = PhotoGallery.published_objects.all()
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            'project': ALL_WITH_RELATIONS,
        }

class PhotoResource(ModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = Photo.published_objects.all()
        allowed_methods = ['get']
        filtering = {
            'slug': ALL,
            'project': ALL_WITH_RELATIONS,
            'title': ALL,
        }
    def dehydrate_image(self, bundle):
        if 'size' in bundle.request.GET:
            # TODO:
            # use id to filter instead of slug? implement id filtering above
            try:
                size = ast.literal_eval(bundle.request.GET['size'])
            except SyntaxError:
                return bundle.data['image']
            thumbnailer = self.obj_get(slug=bundle.data['slug']).image
            thumbnail_options = {'size': size}
            if 'crop' in bundle.request.GET and bundle.request.GET['crop'].lower() == 'true':
                thumbnail_options.update({'crop': True})
            return thumbnailer.get_thumbnail(thumbnail_options).url
        else:
            return bundle.data['image']
    def get_object_list(self, request):
        if hasattr(request, 'GET') and 'gallery__id' in request.GET:
            return Photo.published_objects.filter(photogallery=request.GET['gallery__id']).order_by('photogalleryitem__order')
        else:
            return super(PhotoResource, self).get_object_list(request)

class VideoGalleryResource(ModelResource):
    class Meta:
        queryset = VideoGallery.published_objects.all()
        allowed_methods = ['get']

class VideoResource(ModelResource):
    class Meta:
        queryset = Video.published_objects.all()
        allowed_methods = ['get']

class StoryResource(ModelResource):
    class Meta:
        queryset = Story.published_objects.all()
        allowed_methods = ['get']

class BlogResource(ModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = Blog.published_objects.all()
        allowed_methods = ['get']

class BlogPostResource(ModelResource):
    class Meta:
        queryset = BlogPost.published_objects.all()
        allowed_methods = ['get']

class DocumentResource(ModelResource):
    # TODO:
    # this one could be interesting
    # check the TastyPie documentation on
    # non-ORM resources, which is what this would be.
    # 
    # It will need to build a QuerySet of documents
    # from DocumentCloud
    class Meta:
        pass
