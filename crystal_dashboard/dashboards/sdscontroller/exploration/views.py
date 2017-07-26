# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from horizon import views

from crystal_dashboard.dashboards.sdscontroller.exploration \
    import tabs as mydashboard_tabs
from urlparse import urlparse




class IndexView(views.APIView):
    # A very simple class-based view...
    template_name = 'sdscontroller/exploration/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        context["ip_host"] = request.META['HTTP_HOST'].split(':')[0]
        return context

#
# from horizon import tabs
#
# from openstack_dashboard.dashboards.sdscontroller.administration \
#     import tabs as mydashboard_tabs
#
#
# class IndexView(tabs.TabbedTableView):
#     tab_group_class = mydashboard_tabs.MypanelTabs
#     template_name = 'sdscontroller/administration/index.html'
#
#     def get_data(self, request, context, *args, **kwargs):
#         # Add data to the context here...
#         return context