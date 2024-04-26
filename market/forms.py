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
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['post_category_hsn'].queryset = Category.objects.all()
        self.fields['post_category_hsn'].label_from_instance = self.label_from_instance

    @staticmethod
    def label_from_instance(obj):
        # Return the first 20 characters of the category name along with the HSN code
        return "%s - %s" % (obj.hsn_6_digit, obj.category_name[:20])

    def save(self, commit=True):
        instance = super(PostForm, self).save(commit=False)
        # Set item's industry based on the selected category's industry
        if instance.post_category_hsn:
            instance.post_industry = instance.post_category_hsn.industry
        if commit:
            instance.save()
            self._save_m2m()
        return instance


class CategorySearchForm(forms.Form):
    query = forms.CharField(required=False, 
                            label='Search categories',
                            widget=forms.TextInput(attrs={
            'class': 'border-2 border-gray-300 rounded-lg p-2',  # Example classes for border
            'placeholder': 'Type here to search...'  # Optional placeholder text
        }))