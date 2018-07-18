from django.conf.urls import url
from aar.views import index,R_Conference,R_Guidence,R_journal,Book,Update_Conferance,Update_Journal,Update_Book,Update_Guidence

urlpatterns = [
    url(r'^books/$', index, name='index'),
    url(r'^insert/$',Book, name='Book'),
    url(r'^conferance/$',R_Conference, name='R_Conference'),
    url(r'^guidance/$',R_Guidence, name='R_Guidence'),
    url(r'^journal/$',R_journal, name='R_journal'),
    url(r'^update_conf/$',Update_Conferance),
    url(r'^update_journal/$',Update_Journal),
    url(r'^update_book/$',Update_Book),
    url(r'^update_guidance/$',Update_Guidence),

]