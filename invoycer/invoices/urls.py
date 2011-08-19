from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'invoices.views.index', name='index'),
)