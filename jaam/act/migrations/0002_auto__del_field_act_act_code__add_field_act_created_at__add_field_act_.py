# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Act.act_code'
        db.delete_column('act_act', 'act_code')

        # Adding field 'Act.created_at'
        db.add_column('act_act', 'created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 2, 23, 16, 44, 56, 543394), blank=True), keep_default=False)

        # Adding field 'Act.modified_at'
        db.add_column('act_act', 'modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 2, 23, 16, 44, 56, 543394), blank=True), keep_default=False)

        # Adding field 'Act.published'
        db.add_column('act_act', 'published', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Act.slug'
        db.add_column('act_act', 'slug', self.gf('django.db.models.fields.SlugField')(default='a', unique=True, max_length=50, db_index=True), keep_default=False)

        # Adding field 'Act.project'
        db.add_column('act_act', 'project', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['projects.Project']), keep_default=False)

        # Adding field 'Act.text'
        db.add_column('act_act', 'text', self.gf('ckeditor.fields.RichTextField')(default=''), keep_default=False)

        # Adding field 'Act.image'
        db.add_column('act_act', 'image', self.gf('django.db.models.fields.files.ImageField')(default=1, max_length=200), keep_default=False)

        # Adding M2M table for field tags on 'Act'
        db.create_table('act_act_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('act', models.ForeignKey(orm['act.act'], null=False)),
            ('tag', models.ForeignKey(orm['journalism.tag'], null=False))
        ))
        db.create_unique('act_act_tags', ['act_id', 'tag_id'])


    def backwards(self, orm):
        
        # Adding field 'Act.act_code'
        db.add_column('act_act', 'act_code', self.gf('ckeditor.fields.RichTextField')(default=0), keep_default=False)

        # Deleting field 'Act.created_at'
        db.delete_column('act_act', 'created_at')

        # Deleting field 'Act.modified_at'
        db.delete_column('act_act', 'modified_at')

        # Deleting field 'Act.published'
        db.delete_column('act_act', 'published')

        # Deleting field 'Act.slug'
        db.delete_column('act_act', 'slug')

        # Deleting field 'Act.project'
        db.delete_column('act_act', 'project_id')

        # Deleting field 'Act.text'
        db.delete_column('act_act', 'text')

        # Deleting field 'Act.image'
        db.delete_column('act_act', 'image')

        # Removing M2M table for field tags on 'Act'
        db.delete_table('act_act_tags')


    models = {
        'act.act': {
            'Meta': {'object_name': 'Act'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['journalism.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'text': ('ckeditor.fields.RichTextField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'journalism.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exif_data': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['photos.PhotoExifData']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200'}),
            'journalist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['journalism.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'photos.photoexifdata': {
            'Meta': {'object_name': 'PhotoExifData'},
            'altitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'camera_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'camera_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'flash_used': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'fnumber': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'focal_length': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'gps_latitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'gps_longitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'height_dimension': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shutter_speed': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'width_dimension': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'})
        },
        'photos.photogallery': {
            'Meta': {'object_name': 'PhotoGallery'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['photos.Photo']", 'through': "orm['photos.PhotoGalleryItem']", 'symmetrical': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['journalism.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'photos.photogalleryitem': {
            'Meta': {'object_name': 'PhotoGalleryItem'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.PhotoGallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']"})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'accentColor': ('django.db.models.fields.CharField', [], {'default': "'FFFFFF'", 'max_length': '7'}),
            'coverGallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['photos.PhotoGallery']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.ProjectLocation']", 'symmetrical': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'primaryColor': ('django.db.models.fields.CharField', [], {'default': "'FF0000'", 'max_length': '7'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['journalism.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.projectlocation': {
            'Meta': {'object_name': 'ProjectLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['act']