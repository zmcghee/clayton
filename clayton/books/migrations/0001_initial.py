# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Author'
        db.create_table('books_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('given_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('books', ['Author'])

        # Adding model 'BookLog'
        db.create_table('books_booklog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Author'], null=True, blank=True)),
            ('date_finished', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2010, 12, 3, 22, 20, 45, 464301))),
            ('isbn_10', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('isbn_13', self.gf('django.db.models.fields.CharField')(max_length=14, null=True, blank=True)),
            ('is_repeat_reading', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('books', ['BookLog'])


    def backwards(self, orm):
        
        # Deleting model 'Author'
        db.delete_table('books_author')

        # Deleting model 'BookLog'
        db.delete_table('books_booklog')


    models = {
        'books.author': {
            'Meta': {'ordering': "('surname', 'given_name')", 'object_name': 'Author'},
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'books.booklog': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'BookLog'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Author']", 'null': 'True', 'blank': 'True'}),
            'book_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'date_finished': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 3, 22, 20, 45, 464301)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_repeat_reading': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn_10': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'isbn_13': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['books']
