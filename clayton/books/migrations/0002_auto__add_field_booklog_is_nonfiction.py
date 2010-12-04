# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'BookLog.is_nonfiction'
        db.add_column('books_booklog', 'is_nonfiction', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'BookLog.is_nonfiction'
        db.delete_column('books_booklog', 'is_nonfiction')


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
            'date_finished': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 3, 22, 26, 45, 986074)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_nonfiction': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_repeat_reading': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn_10': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'isbn_13': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['books']
