# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Race.race_type'
        db.add_column('race_race', 'race_type', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Changing field 'Race.contact_email'
        db.alter_column('race_race', 'contact_email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Race.contact_phone'
        db.alter_column('race_race', 'contact_phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Deleting field 'Race.race_type'
        db.delete_column('race_race', 'race_type')

        # Changing field 'Race.contact_email'
        db.alter_column('race_race', 'contact_email', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Race.contact_phone'
        db.alter_column('race_race', 'contact_phone', self.gf('django.db.models.fields.CharField')(max_length=100))


    models = {
        'race.distance': {
            'Meta': {'object_name': 'Distance'},
            'distance': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '1'}),
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
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'race_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['race']
