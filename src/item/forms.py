from django import forms


TYPE_CHOICES = [("job", "job"), ("story", "story"), ("poll", "poll"), ("all", "all")]


class FilterForm(forms.Form):
    type = forms.ChoiceField(choices=TYPE_CHOICES, required=False, initial="all")
    search = forms.CharField(required=False)
