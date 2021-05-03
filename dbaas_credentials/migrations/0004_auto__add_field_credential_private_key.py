# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Credential.private_key'
        db.add_column(u'dbaas_credentials_credential', 'private_key',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Credential.private_key'
        db.delete_column(u'dbaas_credentials_credential', 'private_key')


    models = {
        u'dbaas_credentials.credential': {
            'Meta': {'object_name': 'Credential'},
            'config': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'endpoint': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'environments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['physical.Environment']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'integration_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'integration_type'", 'on_delete': 'models.PROTECT', 'to': u"orm['dbaas_credentials.CredentialType']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '406', 'null': 'True', 'blank': 'True'}),
            'private_key': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '406', 'blank': 'True'}),
            'team': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'dbaas_credentials.credentialtype': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'CredentialType'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'dbaas_credentials.parameter': {
            'Meta': {'unique_together': "((u'credential', u'name'),)", 'object_name': 'Parameter'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'credential': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'credential_parameters'", 'to': u"orm['dbaas_credentials.Credential']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'physical.cloud': {
            'Meta': {'object_name': 'Cloud'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.environment': {
            'Meta': {'object_name': 'Environment'},
            'cloud': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'environment_cloud'", 'on_delete': 'models.PROTECT', 'to': u"orm['physical.Cloud']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'migrate_environment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'migrate_to'", 'null': 'True', 'to': u"orm['physical.Environment']"}),
            'min_of_zones': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'provisioner': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'stage': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dbaas_credentials']