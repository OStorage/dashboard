from django.conf.urls import url
from crystal_dashboard.dashboards.crystal.controllers.controllers import views

urlpatterns = [
    url(r'^create_controller/$', views.CreateControllerView.as_view(), name='create_controller'),
]
