from clayton.movies.models import FilmLog
from datetime import datetime, timedelta
from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse

urlpatterns = patterns('django.views.generic.date_based',
    url(r'^log/(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_month', {
    	'queryset': FilmLog.objects.all(),
    	'date_field': 'date',
    	'month_format': '%m',
    	'template_name': 'log/month.html',
    	'template_object_name': 'movie',
    	'allow_empty': True,
    }, name='filmlog_archive_month'),
    url(r'^log/(?P<year>\d{4})/$', 'archive_year', {
    	'queryset': FilmLog.objects.all(),
    	'date_field': 'date',
    	'template_name': 'log/year.html',
    	'allow_empty': True,
    	'extra_context': {
    		'current_year': "%s" % datetime.today().year,
    	},
    }, name='filmlog_archive_year'),
)

urlpatterns += patterns('django.views.generic.simple',
    ('^log/$', 'redirect_to', {
    	'url': reverse('filmlog_archive_month', args=[
    		datetime.today().year, datetime.today().month]),
    	'permanent': False
    }),
)

urlpatterns += patterns('clayton.movies.views',
    url(r'^log/entry/(?P<id>\d+)/$', 'filmlog_entry_detail', name='filmlog_entry'),
)