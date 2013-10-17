# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.body_html'
        db.delete_column(u'blog_post', 'body_html')

        # Adding field 'Post.display'
        db.add_column(u'blog_post', 'display',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'Post.description'
        db.alter_column(u'blog_post', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Adding field 'Post.body_html'
        db.add_column(u'blog_post', 'body_html',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Post.display'
        db.delete_column(u'blog_post', 'display')


        # Changing field 'Post.description'
        db.alter_column(u'blog_post', 'description', self.gf('django.db.models.fields.TextField')(default='Description'))

    models = {
        u'blog.post': {
            'Meta': {'ordering': "['pub_date']", 'object_name': 'Post'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'None'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'blank': 'True'}),
            'text': ('ckeditor.fields.RichTextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']