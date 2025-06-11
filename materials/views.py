from django.shortcuts import render
from .models import Material, Category
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from users.decorators import role_required
from django.utils.decorators import method_decorator


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


@method_decorator(role_required(['teacher']), name='dispatch')
class CreateMaterialView(CreateView):
    model = Material
    fields = ['title', 'category', 'file']
    template_name = 'materials/material_form.html'
    success_url = reverse_lazy('materials:materials_home')


@method_decorator(role_required(['teacher']), name='dispatch')
class UpdateMaterialView(UpdateView):
    model = Material
    fields = ['title', 'category', 'file']
    template_name = 'materials/material_form.html'
    success_url = reverse_lazy('materials:materials_home')


@method_decorator(role_required(['teacher']), name='dispatch')
class DeleteMaterialView(DeleteView):
    model = Material
    template_name = 'materials/material_confirm_delete.html'
    success_url = reverse_lazy('materials:materials_home')
