"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path,include
from waterbottle import views
from django.contrib.auth.views import LogoutView,LoginView
from waterbottle.views import index, adminclick_view, admin_dashboard_view, admin_404,admin_contact_view,admin_delete_contact,admin_edit_contact,upload_picture, views_pictures
from . import settings
from django.conf.urls.static import static





urlpatterns = [
    path('', views.index , name='index'),
     # add these lines
    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='admin/login.html'),name='adminlogin'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(next_page='/adminlogin'), name='logout'),
    path('admin-dashboard', admin_dashboard_view, name='admin-dashboard'),
      path('portfolio/',views.portfolio,name='portfolio'),
    path('contact/',views.contact,name='contact'),
    path('admin/404', admin_404),
    path('admin-contact' ,admin_contact_view , name='admin-contact' ),
    path('admin-delete-contact/<int:contact_id>/', views.admin_delete_contact, name='admin-delete-contact'),
    path('admin-edit-contact/<int:contact_id>/', views.admin_edit_contact, name='admin-edit-contact'),
      path('upload-picture/', views.upload_picture, name='upload_picture'),
    path('views-pictures/', views.views_pictures, name='views_pictures'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




