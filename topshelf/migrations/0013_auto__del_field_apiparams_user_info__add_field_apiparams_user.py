# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ApiParams.user_info'
        db.delete_column(u'topshelf_apiparams', 'user_info_id')

        # Adding field 'ApiParams.user'
        db.add_column(u'topshelf_apiparams', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ApiParams.user_info'
        raise RuntimeError("Cannot reverse this migration. 'ApiParams.user_info' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ApiParams.user_info'
        db.add_column(u'topshelf_apiparams', 'user_info',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'ApiParams.user'
        db.delete_column(u'topshelf_apiparams', 'user_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'topshelf.apiparams': {
            'Meta': {'object_name': 'ApiParams'},
            'choice1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'choice2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'choice3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'diet': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'topshelf.ingredmaster': {
            'Meta': {'object_name': 'IngredMaster'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ing': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'topshelf.ingredmaster_test': {
            'Meta': {'object_name': 'IngredMaster_test'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ing_test': ('django.db.models.fields.CharField', [], {'max_length': '10000'})
        },
        u'topshelf.useringred': {
            'Meta': {'object_name': 'UserIngred'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ing_master': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['topshelf.IngredMaster_test']"}),
            'purch_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'topshelf.userrecipe': {
            'Meta': {'object_name': 'UserRecipe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['topshelf']