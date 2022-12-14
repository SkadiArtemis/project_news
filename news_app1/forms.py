from django import forms
from django.core. exceptions import ValidationError
from .models import Post, Subscribers


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get("name")
            description = cleaned_data.get("description")

            if name == description:
                raise ValidationError(
                    "Описание не должно быть идентично названию."
                )

            return cleaned_data


class Group(forms.ModelForm):
    pass


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ('category', )
