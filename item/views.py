from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from django.db.models import Q
from market.models import Post, Industry, Category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import(ListView, 
                                DetailView, 
                                CreateView, 
                                UpdateView,
                                DeleteView
)
from django.contrib.auth.models import User


def items(request):
    query = request.GET.get('query', '')
    industries = Industry.objects.all()
    industry_id = request.GET.get('industry', 0)
    items = Item.objects.all()
    
    if industry_id:
        items = items.filter(item_industry_id = industry_id)


    if query:
        items = items.filter(Q(item_name__icontains =query) | Q(item_description__icontains = query) )

    return render(request, 'item/items.html', {
        'items':items,
        'query': query,
        'industries': industries,
        'industry_id': int(industry_id)
    })





def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(created_by = item.created_by).order_by('-created_at').exclude(pk=pk)[0:3]
    similar_items = Item.objects.filter(item_industry = item.item_industry).order_by('-created_at').exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        'similar_items': similar_items,
    })


@login_required
def newitem(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by =request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    form = NewItemForm()
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
 

    return render(request, 'item/item_form.html', {
        'form': form,
        'title': 'Edit Item',
    })    

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by = request.user)
    item.delete()

    return redirect('market-index')



@login_required
def edititem(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by = request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance = item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
 

    return render(request, 'item/item_form.html', {
        'form': form,
        'title': 'New Item',
    })  