
from . import views
from leads import views as leads_views
from aidialer import views as aidialer_views
from accounts import views as accounts_views
from django.urls import path

app_name = "dashboard"

urlpatterns = [
    path(
        '',
        views.DashboardView.as_view(),
        name='home'
    ),
    path(
        'profile/',
        accounts_views.UserProfileView.as_view(),
        name='profile'
    ),
    path(
        'leads/',
        leads_views.LeadView.as_view(),
        name='leads'
    ),
    path(
        'leads/search/',
        leads_views.LeadSearchView.as_view(),
        name='leads_search'
    ),
    path(
        'leads/export/',
        leads_views.LeadExportView.as_view(),
        name='leads_export'
    ),
    path(
        'leads/<int:pk>/update/',
        leads_views.LeadUpdateView.as_view(),
        name='leads_update'
    ),
    path(
        'leads/<int:pk>/delete/',
        leads_views.LeadDeleteView.as_view(),
        name='leads_delete'
    ),
    path(
        'leads/category/',
        leads_views.CategoryView.as_view(),
        name='leads_category'
    ),
    path(
        'leads/category/search/',
        leads_views.CategorySearchView.as_view(),
        name='leads_category_search'
    ),
    path(
        'leads/category/export/',
        leads_views.CategoryExportView.as_view(),
        name='leads_category_export'
    ),
    path(
        'leads/category/<int:pk>/update/',
        leads_views.CategoryUpdateView.as_view(),
        name='leads_category_update'
    ),
    path(
        'leads/category/<int:pk>/delete/',
        leads_views.CategoryDeleteView.as_view(),
        name='leads_category_delete'
    ),
    path(
        'leads/agent/',
        leads_views.AgentView.as_view(),
        name='leads_agent'
    ),
    path(
        'leads/agent/export/',
        leads_views.AgentExportView.as_view(),
        name='leads_agent_export'
    ),
    path(
        'leads/agent/search/',
        leads_views.AgentSearchView.as_view(),
        name='leads_agent_search'
    ),
    path(
        'leads/agent/<int:pk>/update/',
        leads_views.AgentUpdateView.as_view(),
        name='leads_agent_update'
    ),
    path(
        'leads/agent/<int:pk>/delete/',
        leads_views.AgentDeleteView.as_view(),
        name='leads_agent_delete'
    ),
    # adding ai dialer path here
    path(
        'aidialer',
        aidialer_views.ai_dialer_view,
        name='ai_dialer'
    )
]
