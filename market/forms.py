from django import forms
from .models import Post, Industry, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'intent', 'source_country', 'target_country', 'post_category_hsn']
        labels = {
            'title': 'Post Title',
            'image': 'Post Image',
            'content': 'Post Content',
            'intent': 'Post Intent',
            'source_country': 'Source Country',
            'target_country': 'Target Country',
            'post_category_hsn': 'HSN Code of Category',
        }
    def save(self, commit=True):
        instance = super(PostForm, self).save(commit=False)
        # Set item's industry based on the selected category's industry
        if instance.post_category_hsn:
            instance.post_industry = instance.post_category_hsn.industry
        if commit:
            instance.save()
            # Save many-to-many data for the form.
            self._save_m2m()
        return instance

class CategorySearchForm(forms.Form):
    query = forms.CharField(required=False, 
                            label='Search categories',
                            widget=forms.TextInput(attrs={
            'class': 'border-2 border-gray-300 rounded-lg p-2',  # Example classes for border
            'placeholder': 'Type here to search...'  # Optional placeholder text
        }))