from django import forms
from .models import Item
from market.models import Industry, Category


INPUT_CLASSES = 'mt-6 w-auto py-3 px-3 rounded-xl border '


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'item_name', 'item_description', 'image', 'preferred_unit', 
            'quantity', 'quality_description', 'price_per_unit', 
            'available', 'expiration_date', 'item_category'
        ]
        labels = {
            'quantity': 'Minimum Order Quantity (MOQ)',
            'item_category': 'Category'
        }
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'input-class'}),
            'item_description': forms.Textarea(attrs={'class': 'input-class'}),
            'image': forms.FileInput(attrs={'class': 'input-class'}),
            'preferred_unit': forms.Select(attrs={'class': 'input-class'}),
            'quantity': forms.NumberInput(attrs={'class': 'input-class'}),
            'quality_description': forms.Textarea(attrs={'class': 'input-class'}),
            'price_per_unit': forms.NumberInput(attrs={'class': 'input-class'}),
            'available': forms.CheckboxInput(attrs={'class': 'input-class'}),
            'expiration_date': forms.DateInput(attrs={'class': 'input-class', 'type': 'date'}),
            'item_category': forms.Select(attrs={'class': 'input-class'})
        }

    def __init__(self, *args, **kwargs):
        super(NewItemForm, self).__init__(*args, **kwargs)
        self.fields['item_category'].queryset = Category.objects.all()
        self.fields['item_category'].label_from_instance = lambda obj: f"{obj.hsn_6_digit} - {obj.category_name[:20]}"

    def save(self, commit=True):
        instance = super(NewItemForm, self).save(commit=False)
        if instance.item_category:
            instance.item_industry = instance.item_category.industry
        if commit:
            instance.save()
            self._save_m2m()
        return instance


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'item_name', 'item_description', 'image', 
            'preferred_unit', 'quantity', 'quality_description', 'price_per_unit',
            'available', 'item_category'
        ]
        labels = {
            'quantity': 'Minimum Order Quantity (MOQ)'
        }
        widgets = {
            'item_category': forms.Select(attrs={'class': 'input-class'}),
            'item_name': forms.TextInput(attrs={'class': 'input-class'}),
            'item_description': forms.Textarea(attrs={'class': 'input-class'}),
            'image': forms.FileInput(attrs={'class': 'input-class'}),
            'preferred_unit': forms.Select(attrs={'class': 'input-class'}),
            'quantity': forms.NumberInput(attrs={'class': 'input-class'}),
            'quality_description': forms.Textarea(attrs={'class': 'input-class'}),
            'price_per_unit': forms.NumberInput(attrs={'class': 'input-class'}),
            'available': forms.CheckboxInput(attrs={'class': 'input-class'}),
            
        }

    def __init__(self, *args, **kwargs):
        super(EditItemForm, self).__init__(*args, **kwargs)
        self.fields['item_category'].queryset = Category.objects.all()
        self.fields['item_category'].label_from_instance = lambda obj: f"{obj.hsn_6_digit} - {obj.category_name[:20]}"

    def save(self, commit=True):
        instance = super(EditItemForm, self).save(commit=False)
        if instance.item_category:
            instance.item_industry = instance.item_category.industry
        if commit:
            instance.save()
            self._save_m2m()
        return instance



#'created_by'