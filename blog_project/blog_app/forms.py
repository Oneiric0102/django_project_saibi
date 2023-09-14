from django import forms
from .models import Board
from ckeditor.widgets import CKEditorWidget


class TempPostForm(forms.ModelForm):
    is_draft = forms.BooleanField(
        required=False, initial=True, widget=forms.CheckboxInput(attrs={"class": "checkbox"})
    )

    class Meta:
        model = Board
        fields = ["title", "content", "is_draft"]


class PostForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                "style": "border: 1px solid #dbdbdb; width: 735px; height:30px;",
                "placeholder": " 제목",
            }
        ),
    )
    content = forms.CharField(widget=CKEditorWidget(config_name="default"), label="")

    class Meta:
        model = Board
        fields = ["title", "content"]
