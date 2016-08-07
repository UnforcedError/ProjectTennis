from django.conf.urls import url

from . import views

# namespace
app_name = 'TennisApp'

urlpatterns = [
    url(r'^$', views.add_match, name="add_match"),
    url(r'^test$', views.show_post, name="test"),
    url(r'^formsTest$', views.add_match, name="test_forms"),
    url(r'^table$', views.show_table, name="table_view")
]