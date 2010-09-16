# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Race'
        db.create_table('race_race', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_email', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('race', ['Race'])

        # Adding model 'Distance'
        db.create_table('race_distance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('distance', self.gf('django.db.models.fields.IntegerField')()),
            ('unit', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('race', ['Distance'])

        # Adding model 'Event'
        db.create_table('race_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['race.Race'])),
            ('distance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['race.Distance'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('race', ['Event'])


    def backwards(self, orm):
        
        # Deleting model 'Race'
        db.delete_table('race_race')

        # Deleting model 'Distance'
        db.delete_table('race_distance')

        # Deleting model 'Event'
        db.delete_table('race_event')


    models = {
        'race.distance': {
            'Meta': {'object_name': 'Distance'},
            'distance': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'unit': ('django.db.models.fields.IntegerField', [], {})
        },
        'race.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'distance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['race.Distance']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['race.Race']"})
        },
        'race.race': {
            'Meta': {'object_name': 'Race'},
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['race']
