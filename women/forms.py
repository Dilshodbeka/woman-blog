from django import forms
from .models import Category, Husband, Women


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Kategoriya')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label='Er')
    
    class Meta:
        model = Women
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
        labels = {'slug': 'url'}


class UploadFileForm(forms.Form):
    file=forms.ImageField(label='Fayl')