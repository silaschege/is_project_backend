from importlib.machinery import PathFinder
from importlib.metadata import PathDistribution
from typing import OrderedDict
from django.shortcuts import render

# Create your views here.

# record payment with installment 
# check if order if blance is zero and make balance into zero
# balanc is difference of total sum of installments minus the total amount paid 
# toatal amout paid is total amount paid plus previous total amount paid 
# change installment stattus ro paid if balance is zero
# balance is zero then it is moved to shipping
