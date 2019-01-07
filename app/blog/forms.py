import re

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

    def clean_message(self):
        # CommentForm 에서 작성한 cleaned_data 로 받아 message 변수에 할당
        message = self.cleaned_data.get('message', None)
        if message:
            # CommentForm 에 한글이 단 한자라도 없으면 ValidationError 을 발생
            if not re.search(r'[ㄱ-힣]', message):
                raise forms.ValidationError('메세지에 한글이 필요합니다.')
        # Validation 을 통과한 message 는 return 하여 해당 댓글 저장
        return message
