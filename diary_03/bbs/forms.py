from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):

    #admin.pyで使うcommentのフォームをtextareaタグにする
    #https://stackoverflow.com/questions/430592/django-admin-charfield-as-textarea
    comment     = forms.CharField(widget=forms.Textarea)

    class Meta:
        model   = Topic
        fields  = [ "title","comment" ] #←このフィールドの順番がadminに関わってくるので注意

#モデルを継承しないフォームクラス
class YearMonthForm(forms.Form):
    year    = forms.IntegerField()
    month   = forms.IntegerField()
