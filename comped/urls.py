from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'comped.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'comped.core.views.home', name='home'),
    url(r'^medico/', 'comped.core.views.home_medico', name='home_medico'),
    url(r'^secretaria/', 'comped.core.views.home_secretaria', name='home_secretaria'),
    url(r'^cadastrar-paciente/', 'comped.core.views.cadastrar_paciente', name='cadastrar-paciente'),
    url(r'^admin/', include(admin.site.urls)),
)