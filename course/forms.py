from django import forms

class CourseAddMemberForm(forms.Form):
    data = forms.CharField(label='學生資料', widget=forms.Textarea)