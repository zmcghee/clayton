from clayton.movies.models import FilmLog
from django.shortcuts import render_to_response
from django.template import RequestContext

def filmlog_entry_detail(request, id):
    return render_to_response('log/expanded_entry.html',
        {'entry': FilmLog.objects.get(pk=id),}, context_instance=RequestContext(request))