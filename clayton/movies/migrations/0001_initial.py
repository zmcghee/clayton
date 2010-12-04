# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Venue'
        db.create_table('movies_venue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('movies', ['Venue'])

        # Adding model 'FilmLog'
        db.create_table('movies_filmlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie_title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movies.Venue'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2010, 12, 3, 21, 24, 25, 553245))),
            ('showtime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('imdb_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=1, db_index=True)),
            ('is_print', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_repeat_viewing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('movies', ['FilmLog'])


    def backwards(self, orm):
        
        # Deleting model 'Venue'
        db.delete_table('movies_venue')

        # Deleting model 'FilmLog'
        db.delete_table('movies_filmlog')


    models = {
        'movies.filmlog': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'FilmLog'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 3, 21, 24, 25, 559115)'}),
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
            'city': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['movies']
