from django.shortcuts import render
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
import razorpay
from .models import Donations


def home(request):
    return render(request, 'index.html')


def donations(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = int(request.POST.get('amount')) * 100

        client = razorpay.Client(auth=("rzp_test_FeSKspFKrmILOE", "eXqKpXcTpiIkJX9QK2d0wC7k"))
        payment = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        donation = Donations(name=name,email=email, amount=amount, razorpay_payment_id=payment['id'])
        donation.save()
    return render(request, 'donations.html')


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = (request.POST)
        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break

        user = Donations.objects.filter(order_id = order_id).first()
        #user.paid = True
        #user.save()

    return render(request, "success.html")



