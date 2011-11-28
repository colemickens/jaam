from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from jaam.shortcuts import render_to_response, RequestContext

from jaam.projects.models import Project
from jaam.photos.models import Photo, PhotoGallery
# Create your views here.
def gallery_details(request, project_slug, gallery_slug):
    project = get_object_or_404(Project, slug=project_slug)
    gallery = get_object_or_404(PhotoGallery, slug=gallery_slug)
    return render_to_response('photo_gallery.html', { 'gallery': gallery }, context_instance=RequestContext(request))

def details(request, project_slug, photo_id):
    project = get_object_or_404(Project, slug=project_slug)
    photo = get_object_or_404(Photo, pk=photo_id)
    return render_to_response('photo_details.html', { 'photo': photo }, context_instance=RequestContext(request))
