from django.shortcuts import render
from Paytm import Checksum
from .models import donation
import json
import requests
from django.views.decorators.csrf import csrf_exempt

id = 1
amount = 10


@csrf_exempt
def index(request):
	return render(request,'chillaid/index.html')
def donation(request):
	return render(request,'chillaid/donate.html')
def period(request):
    return render(request,'periodPositive.html')
def medical(request):
    return render(request,'medical.html')
def education(request):
    return render(request,'education.html')
def submit(request):
    form=forms.donate()
    if request.method=="GET":
        name=request.GET['name']
        email=request.GET['email']
        contact=request.GET['number']
        address=request.GET['address']
        amount=request.GET['amount']
        # massage=request.GET['message']
        # t_id=request.GET['pan']
        id=request.GET['orderid']
        donate=donation(Name=name,Email=email,orderid=id,Contact=contact,address=address,amount=amount)
        donate.save()
        print(id)
        param_dict = dict()
        param_dict["body"]={
            'requestType' : 'Payment',
          'mid':'igXLGH25243081243293',
          'websiteName' : 'tratr.org',
            'orderId' : id,
      'CALLBACK_URL':' http://127.0.0.1:8000/index.html',
            'txnAmount'     : {
        'value'     : amount,
        'currency'  : 'INR',
    },
    'userInfo'      : {
        'custId'    : id,
    },
        }
        MID='@d1PBU6uUPVOt_QY'
        # param_dict['CHECKSUMHASH']= Checksum.generate_checksum(param_dict,MID)
        param_dict["head"] = {
    "signature"    : Checksum.generateSignature(json.dumps(param_dict["body"]),MID)
}
        return render(request,'paytm.html',{'param_dict':param_dict})
    return render(request,'foundation/index.html')

def submit2(request):
    paytmParams = dict()
    context = dict()
    if request.method=="GET":
        name=request.GET['name']
        email=request.GET['email']
        contact=request.GET['number']
        address=request.GET['address']
        amount=request.GET['amount']
        # massage=request.GET['message']
        # t_id=request.GET['pan']
        id=request.GET['orderid']
        donate=donation(Name=name,Email=email,orderid=id,Contact=contact,address=address,amount=amount)
        donate.save()
        print(id)
    paytmParams["body"] = {
        "requestType"   : "Payment",
        "mid"           : "igXLGH25243081243293",
        "websiteName"   : "DEFAULT",
        "orderId"       : id,
        "callbackUrl"   : "https://http://127.0.0.1:8000/index.html",
        "txnAmount"     : {
            "value"     : amount,
            "currency"  : "INR",
        },
        "userInfo"      : {
            "custId"    : id,
        },
    }

    # Generate checksum by parameters we have in body
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
    checksum = Checksum.generateSignature(json.dumps(paytmParams["body"]), "@d1PBU6uUPVOt_QY")

    paytmParams["head"] = {
        "signature"    : checksum
    }

    post_data = json.dumps(paytmParams)

    # for Staging
    url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=igXLGH25243081243293&orderId="+str(id)
    print(url)

    # for Production
    # url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=ORDERID_98765"
    response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
    print(response["body"]["txnToken"])
    context = {
        "t_id" : str(response["body"]["txnToken"]),
        "orderId" : id,
        "amount" : amount
    }
    return render(request,'paytm.html',context)
    return render(request,'foundation/index.html')

@csrf_exempt
def handlerequest(request):
    form=request.POST
    print(form)