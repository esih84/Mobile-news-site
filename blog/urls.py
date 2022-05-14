from django.urls import path
from .models import *
from .views import *


app_name = "blog"

urlpatterns = [
    path('', index, name="index"),
    path('', index2, name="index2"),

    path('post_detail/<slug:slug>/<int:id>/', post_detail, name='post_details'),
    path('mobos_detail/<slug:slug>/<int:prcs_id>/<int:speaker_id>/<int:cameras_id>/<int:material_id>/<int:memory_id>/', mobile_detail, name='mobos'),
    path('lab/<slug:slug>/<int:lobtop_speaker_id>/<int:labtop_processor_id>/<int:connections_id>/', labtop_detail, name='labs'),
    path('ctegor/<slug:slug>/', category_post, name='ctegor'),
    path('cate_obshen/<slug:slug>/', category_obshens, name='cat_obshen'),
    path('search/', search, name='search'),
    path('comment/<int:id>/', comments, name='camments'),
    path('comment/<int:id>/<int:comment_id>/', reply, name='reply'),

]