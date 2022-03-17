from django import template

register = template.Library()

censored_words = ['новость','title']

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Нельзя цензурировать не строку')
    for word in censored_words:
        value = value.replace(word[1:],'*'*(len(word)-1))
    return value