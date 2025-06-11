from django.shortcuts import render
from .models import Material, Category
from django.contrib.auth.decorators import login_required


@login_required(login_url='users:login')
def materials_home(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    materials = Material.objects.all()
    if category_id:
        materials = materials.filter(category_id=category_id)
    context = {
        'categories': categories,
        'materials': materials,
        'selected_category': int(category_id) if category_id else None,
    }
    return render(request, 'materials/materials_home.html', context)
