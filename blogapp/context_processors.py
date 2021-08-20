from .models import Category

def extras(request):
  category_menu = Category.objects.all()
  return {'category_menu': category_menu}