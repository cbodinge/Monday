"""
URL configuration for Monday project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webhooks.views import sample_testing, tests, ticketing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hooks/', sample_testing.rename_new_order, name='rename_new_order'),
    path('rename-pending-orders/', sample_testing.rename_all_pending_orders, name='rename_all_pending_orders'),
    path('create-request-link/', ticketing.create_request_link, name='create_request_link'),
    path('update-all-request-links/', ticketing.update_all_request_links, name='update_all_request_links'),
    path('get-board-ids/', tests.get_board_list),
    path('test/', tests.test),

]
