from django import template


register = template.Library()


cens_words = [
   'должно', 'факт', 'шоу', 'если', 'что',
   'если', 'американском', 'встретится', 1]
a = 1

@register.filter()
def censor(text):
   c_text = text.lower().split()
   for word in c_text:
      if word in cens_words:
         text = text.replace(word, f'{word[0] + len(word) * "*"}')
   return text