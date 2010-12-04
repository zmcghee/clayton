# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Venue.city'
        db.alter_column('movies_venue', 'city', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'Venue.state'
        db.alter_column('movies_venue', 'state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))


    def backwards(self, orm):
        
        # Changing field 'Venue.city'
        db.alter_column('movies_venue', 'city', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'Venue.state'
        db.alter_column('movies_venue', 'state', self.gf('django.db.models.fields.CharField')(max_length=2))


    models = {
        'movies.filmlog': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'FilmLog'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 3, 21, 26, 48, 418330)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_print': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_repeat_viewing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'movie_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_index': 'True'}),
            'showtime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movies.Venue']"})
        },
        'movies.venue': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Venue'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['movies']
