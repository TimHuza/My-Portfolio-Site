from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from django.http import JsonResponse


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects_list.html', {'projects': projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})


# ---- CART VIEWS ----
def add_to_cart(request, project_id):
    # simple session-based cart (GET used here)
    try:
        Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'not found'}, status=404)
    cart = request.session.get('cart', [])
    if project_id not in cart:
        cart.append(project_id)
        request.session['cart'] = cart
    return JsonResponse({'status': 'success', 'cart_count': len(cart)})


def cart_view(request):
    cart = request.session.get('cart', [])
    liked_projects = Project.objects.filter(id__in=cart)
    return render(request, 'projects/cart.html', {'projects': liked_projects})


def remove_from_cart(request, project_id):
    cart = request.session.get('cart', [])
    if project_id in cart:
        cart.remove(project_id)  # Remove the project ID from the cart
        request.session['cart'] = cart  # Update the session
    return JsonResponse({'status': 'success', 'cart_count': len(cart)})