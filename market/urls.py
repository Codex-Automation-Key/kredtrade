from django.urls import path
from . import views
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    UserStoreListView,
                    index,
                    industrydetails,
                    UserCompanyDetailView,
                    )

urlpatterns = [
    path('', PostListView.as_view(), name='market-home'),
    path('about/', views.about, name='market-about'),
    path('industries/', views.industries, name='market-industries'),
    path('medicine/', views.medicine, name='industry-medicine'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), 
    path('company/<str:username>', UserCompanyDetailView.as_view(), name = 'user-company'),   
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('store/<str:username>', UserStoreListView.as_view(), name='user-store'),
    path('index/', index, name='market-index' ),
    path('industry/<int:pk>/', views.industrydetails, name = 'industry-detail' ),
    path('category/<int:pk>/', views.categorydetails, name = 'category-detail'),
    path('category-users/<int:pk>', views.userslist, name = 'category-users'),
    path('ajax/categories_by_industry/<int:industry_id>/', views.categories_by_industry, name='ajax_categories_by_industry'),
    path('search/', views.search_categories, name='search_categories'),
    path('intents/<int:intent_id>/', views.posts_by_intent, name='posts_by_intent'),
    path('country/<str:country_name>/', views.posts_by_country, name='posts_by_country'),
    path('posts_by_country/redirect/', views.posts_by_country_redirect, name='posts_by_country_redirect'),
    path('advance_search', views.filter_posts, name = 'filter_posts'),

]
