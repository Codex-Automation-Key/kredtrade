from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Industry, Category, Intent
from django.views.generic import(ListView, 
                                DetailView, 
                                CreateView, 
                                UpdateView,
                                DeleteView
)
from django.contrib.auth.models import User
from item.models import Item
from users.models import Profile, RegistrationCertificate
from .forms import PostForm, CategorySearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django import template




def index(request):
    items = Item.objects.order_by('-created_at').all()
    industries = Industry.objects.all()
    categories = Category.objects.all()

    return render(request, 'market/index.html', {
        'industries': industries,
        'categories': categories,
        'items': items

    })

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'market\home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'market/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class UserPostListView(ListView):
    model = Post
    template_name = 'market/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

class UserStoreListView(ListView):
    model = Item
    template_name = 'market/user_store.html'
    context_object_name = 'items'

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Item.objects.filter(created_by = user).order_by('-created_at')

class UserCompanyDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'market/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username )
        return user.profile
    def get_context_data(self, **kwargs):
        context = super(UserCompanyDetailView, self).get_context_data(**kwargs)
        user = self.get_object().user
        context['posts'] = Post.objects.filter(author=user).order_by('-date_posted')[0:3]
        context['items'] = Item.objects.filter(created_by=user).order_by('-created_at')[0:3]
        context['reg_certificates'] = RegistrationCertificate.objects.filter(user=user)[0:3]
        return context
       




class PostDetailView(DetailView):
    model = Post
    
 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','image', 'content', 'intent', 'target_country', 'source_country','post_category_hsn']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    
    return render(request, 'market/about.html')

def industries(request):
    context = {
        'industries':Industry.objects.all()
    }
    return render(request, 'market/industries.html', context)

def medicine(request):
   
    return render(request, 'market/medicine.html')

def industrydetails(request, pk):
    industry = get_object_or_404(Industry, pk=pk)
    categories = industry.categories.all()
    context = {
        'industry': industry,
        'categories': categories
    }
    return render(request, 'market/industry-page.html', context)


def categorydetails(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    items = category.items.all()[0:3]
    posts = category.posts.all()[0:3]

    item_users = User.objects.filter(items__item_category=category).distinct()
    post_users = User.objects.filter(post__in=posts).distinct()

    users = (item_users | post_users).distinct()[0:3]

    context = {
        'category': category,
        'items': items,
        'posts': posts,
        'users': users 
    }
    return render(request, 'market/category-page.html', context)

@login_required
def userslist(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    items = category.items.all()[0:3]
    posts = category.posts.all()[0:3]

    item_users = User.objects.filter(items__item_category=category).distinct()
    post_users = User.objects.filter(post__in=posts).distinct()

    users = (item_users | post_users).distinct()

    context = {
        'category': category,
        'items': items,
        'posts': posts,
        'users': users 
    }
    return render(request, 'market/userslist.html', context)


def categories_by_industry(request, industry_id):
    categories = Category.objects.filter(industry_id=industry_id).values('id', 'category_name')
    return JsonResponse(list(categories), safe=False)


def search_categories(request):
    form = CategorySearchForm(request.GET)
    categories = Category.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            categories = categories.filter(Q(category_name__icontains=query) | Q(hsn_6_digit__icontains = query))
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'market/search_categories.html', context)

def posts_by_intent(request, intent_id=None):
    if intent_id is None:
        # Handle the case where no intent_id is provided
        # This could involve redirecting the user, showing a default set of posts, etc.
        raise Http404("Intent not specified.")
    else:
        intent = get_object_or_404(Intent, id=intent_id)
        posts = Post.objects.filter(intent=intent).order_by('-date_posted')
        context = {
            'posts': posts,
            'intent': intent,
        }
        return render(request, 'market/posts_by_intent.html', context)


def posts_by_country(request, country_name):
    posts = Post.objects.filter(target_country=country_name).order_by('-date_posted')
    context = {
        'posts': posts,
        'country_name': country_name,
        'country_choices': Post.COUNTRY_CHOICES,  # Pass COUNTRY_CHOICES to the template
    }
    return render(request, 'market/posts_by_country.html', context)

def posts_by_country_redirect(request):
    country_name = request.GET.get('country_name')
    if country_name:
        return redirect('posts_by_country', country_name=country_name)
    else:
        # Redirect to a default page if no country is selected
        return redirect('market-home')


def filter_posts(request):
    # Get filter values from request
    intent_id = request.GET.get('intent')
    industry_id = request.GET.get('industry')
    country_name = request.GET.get('country')
    search_query = request.GET.get('search', '')

    # Start with all posts
    posts = Post.objects.all()

    # Filter by intent if specified
    if intent_id:
        posts = posts.filter(intent_id=intent_id)

    # Filter by industry if specified
    if industry_id:
        posts = posts.filter(post_industry_id=industry_id)

    # Filter by country (either source or target) if specified
    if country_name:
        posts = posts.filter(Q(source_country=country_name) | Q(target_country=country_name))

    # Filter by search query (in title or content) if specified
    if search_query:
        posts = posts.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    # Additional context variables for the template
    intents = Intent.objects.all()
    industries = Industry.objects.all()
    countries = dict(Post.COUNTRY_CHOICES)

    context = {
        'posts': posts.order_by('-date_posted'),
        'intents': intents,
        'industries': industries,
        'countries': countries,
        'selected_intent': intent_id,
        'selected_industry': industry_id,
        'selected_country': country_name,
        'search_query': search_query,
    }

    return render(request, 'market/posts_filter.html', context)