from datetime import datetime
from django.db import models

RATING_CHOICES = (
	('0', "Walked out / Didn't finish"),
	('1', "Hated it"),
	('2', "Didn't like it"),
	('3', "Liked it"),
	('4', "Really liked it"),
	('5', "Loved it"),
)

class Venue(models.Model):
	name = models.CharField(max_length=50)
	city = models.CharField(max_length=25, blank=True, null=True)
	state = models.CharField(max_length=2, blank=True, null=True)
	url = models.URLField(blank=True, null=True)

	def __unicode__(self):
		if self.city and self.state:
			return "%s (%s, %s)" % (self.name, self.city, self.state)
		return self.name

	class Meta:
		ordering = ('name',)

class FilmLog(models.Model):
	movie_title = models.CharField(max_length=100, db_index=True)
	venue = models.ForeignKey(Venue)
	date = models.DateField(default=datetime.today())
	showtime = models.TimeField(blank=True, null=True, help_text='If applicable')
	imdb_id = models.PositiveIntegerField("IMDb ID", blank=True, null=True)
	release_year = models.PositiveIntegerField(default=datetime.today().year)
	rating = models.CharField(max_length=1, choices=RATING_CHOICES, db_index=True)
	is_print = models.BooleanField("35mm screening")
	is_repeat_viewing = models.BooleanField("repeat viewing")
	is_nonfiction = models.BooleanField("Documentary", default=False)
	notes = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return "%s - %s" % (self.date, self.movie_title)

	class Meta:
		ordering = ('-id',)
		verbose_name_plural = "Film log"