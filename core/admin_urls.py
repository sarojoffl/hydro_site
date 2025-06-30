from django.urls import path
from . import admin_views

urlpatterns = [
    # Dashboard
    path('', admin_views.dashboard_home, name='dashboard_home'),
    path('logout/', admin_views.logout_view, name='logout'),

    # Homepage Section
    path('carousel/', admin_views.carouselitem_list, name='carouselitem_list'),
    path('carousel/add/', admin_views.add_carouselitem, name='add_carouselitem'),
    path('carousel/edit/<int:pk>/', admin_views.edit_carouselitem, name='edit_carouselitem'),
    path('carousel/delete/<int:pk>/', admin_views.delete_carouselitem, name='delete_carouselitem'),


    path('about-info/edit/', admin_views.aboutinfo_edit, name='aboutinfo_edit'),
    
    
    path('about-images/add/', admin_views.add_aboutimage, name='add_aboutimage'),
    path('about-images/', admin_views.aboutimage_list, name='aboutimage_list'),
    path('about-images/edit/<int:pk>/', admin_views.edit_aboutimage, name='edit_aboutimage'),
    path('about-images/delete/<int:pk>/', admin_views.delete_aboutimage, name='delete_aboutimage'),

    
    path('facts/', admin_views.fact_list, name='fact_list'),
    path('facts/add/', admin_views.add_fact, name='add_fact'),
    path('facts/edit/<int:pk>/', admin_views.edit_fact, name='edit_fact'),
    path('facts/delete/<int:pk>/', admin_views.delete_fact, name='delete_fact'),

    # FeatureImage URLs
    path('feature-images/', admin_views.featureimage_list, name='featureimage_list'),
    path('feature-images/add/', admin_views.add_featureimage, name='add_featureimage'),
    path('feature-images/edit/<int:pk>/', admin_views.edit_featureimage, name='edit_featureimage'),
    path('feature-images/delete/<int:pk>/', admin_views.delete_featureimage, name='delete_featureimage'),

    # Feature URLs
    path('features/', admin_views.feature_list, name='feature_list'),
    path('features/add/', admin_views.add_feature, name='add_feature'),
    path('features/edit/<int:pk>/', admin_views.edit_feature, name='edit_feature'),
    path('features/delete/<int:pk>/', admin_views.delete_feature, name='delete_feature'),


    path('services/', admin_views.service_list, name='service_list'),
    path('services/add/', admin_views.add_service, name='add_service'),
    path('services/edit/<int:pk>/', admin_views.edit_service, name='edit_service'),
    path('services/delete/<int:pk>/', admin_views.delete_service, name='delete_service'),

    
    path('projects/', admin_views.project_list, name='project_list'),
    path('projects/add/', admin_views.add_project, name='add_project'),
    path('projects/edit/<int:pk>/', admin_views.edit_project, name='edit_project'),
    path('projects/delete/<int:pk>/', admin_views.delete_project, name='delete_project'),


    path('team/', admin_views.team_list, name='team_list'),
    path('team/add/', admin_views.add_team_member, name='add_team_member'),
    path('team/edit/<int:pk>/', admin_views.edit_team_member, name='edit_team_member'),
    path('team/delete/<int:pk>/', admin_views.delete_team_member, name='delete_team_member'),


    path('testimonials/', admin_views.testimonial_list, name='testimonial_list'),
    path('testimonials/add/', admin_views.add_testimonial, name='add_testimonial'),
    path('testimonials/edit/<int:pk>/', admin_views.edit_testimonial, name='edit_testimonial'),
    path('testimonials/delete/<int:pk>/', admin_views.delete_testimonial, name='delete_testimonial'),

    # CONTACT INFO
    path('contact-info/', admin_views.contactinfo_list, name='contactinfo_list'),
    path('contact-info/add/', admin_views.add_contactinfo, name='add_contactinfo'),
    path('contact-info/edit/<int:pk>/', admin_views.edit_contactinfo, name='edit_contactinfo'),
    path('contact-info/delete/<int:pk>/', admin_views.delete_contactinfo, name='delete_contactinfo'),

    # CONTACT MESSAGES
    path('contact-messages/', admin_views.contactmessage_list, name='contactmessage_list'),
    path('contact-messages/delete/<int:pk>/', admin_views.delete_contactmessage, name='delete_contactmessage'),

    # Downloads
    path('downloads/', admin_views.download_list, name='download_list'),
    path('downloads/add/', admin_views.add_download, name='add_download'),
    path('downloads/edit/<int:pk>/', admin_views.edit_download, name='edit_download'),
    path('downloads/delete/<int:pk>/', admin_views.delete_download, name='delete_download'),

    # Reports
    path('reports/', admin_views.report_list, name='report_list'),
    path('reports/add/', admin_views.add_report, name='add_report'),
    path('reports/edit/<int:pk>/', admin_views.edit_report, name='edit_report'),
    path('reports/delete/<int:pk>/', admin_views.delete_report, name='delete_report'),

    # Notices
    path('notices/', admin_views.notice_list, name='notice_list'),
    path('notices/add/', admin_views.add_notice, name='add_notice'),
    path('notices/edit/<int:pk>/', admin_views.edit_notice, name='edit_notice'),
    path('notices/delete/<int:pk>/', admin_views.delete_notice, name='delete_notice'),

    # CLIENTS
    path('clients/', admin_views.client_list, name='client_list'),
    path('clients/add/', admin_views.add_client, name='add_client'),
    path('clients/edit/<int:pk>/', admin_views.edit_client, name='edit_client'),
    path('clients/delete/<int:pk>/', admin_views.delete_client, name='delete_client'),

    # NEWSLETTER
    path('newsletter/', admin_views.newsletter_list, name='newsletter_list'),
    path('newsletter/delete/<int:pk>/', admin_views.delete_newsletter_subscriber, name='delete_newsletter_subscriber'),
    path('newsletter-subscribers/export-csv/', admin_views.export_newsletter_subscribers_csv, name='export_newsletter_subscribers_csv'),

    # ORGANIZATION DETAILS
    path('organizationdetails/', admin_views.organizationdetail_list, name='organizationdetail_list'),
    path('organizationdetails/add/', admin_views.add_organizationdetail, name='add_organizationdetail'),
    path('organizationdetails/<int:pk>/edit/', admin_views.edit_organizationdetail, name='edit_organizationdetail'),
    path('organizationdetails/<int:pk>/delete/', admin_views.delete_organizationdetail, name='delete_organizationdetail'),
]
