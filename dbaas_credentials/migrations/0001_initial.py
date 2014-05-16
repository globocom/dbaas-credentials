# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CredentialType'
        db.create_table(u'dbaas_credentials_credentialtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'dbaas_credentials', ['CredentialType'])

        # Adding model 'Credential'
        db.create_table(u'dbaas_credentials_credential', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=406, null=True, blank=True)),
            ('integration_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'integration_type', on_delete=models.PROTECT, to=orm['dbaas_credentials.CredentialType'])),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=406, blank=True)),
            ('endpoint', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'dbaas_credentials', ['Credential'])

        # Adding M2M table for field environments on 'Credential'
        m2m_table_name = db.shorten_name(u'dbaas_credentials_credential_environments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('credential', models.ForeignKey(orm[u'dbaas_credentials.credential'], null=False)),
            ('environment', models.ForeignKey(orm[u'physical.environment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['credential_id', 'environment_id'])


    def backwards(self, orm):
        # Deleting model 'CredentialType'
        db.delete_table(u'dbaas_credentials_credentialtype')

        # Deleting model 'Credential'
        db.delete_table(u'dbaas_credentials_credential')

        # Removing M2M table for field environments on 'Credential'
        db.delete_table(db.shorten_name(u'dbaas_credentials_credential_environments'))


    models = {
        u'dbaas_credentials.credential': {
            'Meta': {'object_name': 'Credential'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'endpoint': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'environments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['physical.Environment']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'integration_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'integration_type'", 'on_delete': 'models.PROTECT', 'to': u"orm['dbaas_credentials.CredentialType']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '406', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '406', 'blank': 'True'}),
            'team': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'dbaas_credentials.credentialtype': {
            'Meta': {'object_name': 'CredentialType'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.environment': {
            'Meta': {'object_name': 'Environment'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dbaas_credentials']