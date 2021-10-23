from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    format = None
    if 'product_format' in request.POST:
        format = request.POST['product_format']
    bag = request.session.get('bag', {})
    
    if format:
        if item_id in list(bag.keys()):
            if format in bag[item_id]['items_by_format'].keys():
                bag[item_id]['items_by_format'][format] += quantity
            else:
                bag[item_id]['items_by_format'][format] = quantity
        else:
            bag[item_id] = {'items_by_format': {format: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    format = None
    if 'product_format' in request.POST:
        format = request.POST['product_format']
    bag = request.session.get('bag', {})

    if format:
        if quantity > 0:
            bag[item_id]['items_by_format'][format] = quantity
        else:
            del bag[item_id]['items_by_format'][format]
            if not bag[item_id]['items_by_format']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        format = None
        if 'product_format' in request.POST:
            format = request.POST['product_format']
        bag = request.session.get('bag', {})

        if format:
            del bag[item_id]['items_by_format'][format]
            if not bag[item_id]['items_by_format']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)