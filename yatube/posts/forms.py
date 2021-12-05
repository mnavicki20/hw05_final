from django.forms import ModelForm

from .models import Comment, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text', 'image')
        labels = {
            'text': 'Текст публикации',
            'group': 'Группа публикации',
            'image': 'Картинка публикации',
        }
        help_texts = {
            'text': 'Введите текст публикации',
            'group': 'Укажите группу публикации',
            'image': 'Добавьте картинку к публикации',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Текст комментария',
        }
        help_texts = {
            'text': 'Введите текст комментария',
        }
