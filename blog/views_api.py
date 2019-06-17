from django.http import JsonResponse
from blog.models import Category
from django.core.exceptions import ValidationError, ObjectDoesNotExist

def get_category_list(request):
    category_name = request.GET.get('name', '')
    if category_name == '':
        return JsonResponse({'status':10021, 'message':'parameter error : name of category is null'})
    else:
        category = {}
        try:
            result = Category.objects.get(name=category_name)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'query result is empty'})
        else:
            category['name'] = result.name
            return JsonResponse({'status':200, 'message':'success', 'data':category})

def add_category(request):
    category_name = request.POST.get('name', '')
    result = Category.objects.filter(name=category_name)
    if category_name == '':
        return JsonResponse({'status':10021, 'message':'parameter error : name of category is null'})
    else:
        if result:
            return JsonResponse({'status':10022, 'message':'category is already exits'})
        else:
            Category.objects.create(name=category_name)
            return JsonResponse({'status':200, 'message':'add event success'})