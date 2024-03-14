from django import forms
from .models import Item


INPUT_CLASSES = 'mt-6 w-auto py-3 px-3 rounded-xl border '


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_name', 'item_description', 'image', 
                    'preferred_unit', 'quantity', 'quality_description', 'price_per_unit',
                    'available','item_category')

        labels = {
            'quantity': 'M.O.Q.'
        }

        widgets = {
            'item_category':forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'item_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'item_description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),


        }

    def save(self, commit=True):
        instance = super(NewItemForm, self).save(commit=False)
        # Set item's industry based on the selected category's industry
        if instance.item_category:
            instance.item_industry = instance.item_category.industry
        if commit:
            instance.save()
            # Save many-to-many data for the form.
            self._save_m2m()
        return instance

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_category', 'item_name', 'item_description', 'image', 'preferred_unit', 'quantity', 'quality_description', 'price_per_unit',
                    'available',)

        labels = {
            'quantity' : 'M.O.Q'
        }
        
        widgets = {
            
            'item_category':forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'item_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'item_description': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'quantity': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })


        }




#'created_by'