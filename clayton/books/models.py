from datetime import datetime
from django.db import models

class Author(models.Model):
	given_name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)

	def __unicode__(self):
		return "%s %s" % (self.given_name, self.surname)

	class Meta:
		ordering = ('surname', 'given_name',)

class BookLog(models.Model):
	book_title = models.CharField(max_length=100, db_index=True)
	author = models.ForeignKey(Author, blank=True, null=True)
	date_finished = models.DateField(default=datetime.today())
	isbn_10 = models.CharField("ISBN-10", max_length=10, blank=True, null=True)
	isbn_13 = models.CharField("ISBN-13", max_length=14, blank=True, null=True)
	is_nonfiction = models.BooleanField("Nonfiction", default=True)
	is_repeat_reading = models.BooleanField("repeat reading")
	notes = models.TextField(blank=True, null=True)

	def __unicode__(self):
		if self.author:
			return "%s - %s (%s)" % (self.date_finished, self.book_title, self.author)
		return "%s - %s" % (self.date_finished, self.book_title)

	class Meta:
		ordering = ('-id',)
		verbose_name_plural = "Book log"