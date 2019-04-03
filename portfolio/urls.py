from django.urls import include, path
from portfolio import views
from rest_framework.urlpatterns import format_suffix_patterns

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('items/', views.list_item),
]
urlpatterns = format_suffix_patterns(urlpatterns)
