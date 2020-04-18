from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Club

class ClubChartView(TemplateView):
	template_name = 'stocks/charts.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["qs"] = Club.objects.all()
		return context

def home(request):
	return render(request, 'stocks/home.html')

def bar(request):
	return render(request, 'stocks/index.html')

def doughnut(request):
	item_one = request.POST.get("item_one")
	price_one = request.POST.get("price_one")
	item_two = request.POST.get("item_two")
	price_two = request.POST.get("price_two")
	item_three = request.POST.get("item_three")
	price_three = request.POST.get("price_three")	
	item_four = request.POST.get("item_four")
	price_four = request.POST.get("price_four")

	context3 = {
		"items": [item_one, item_two, item_three, item_four],
		"prices": [price_one, price_two, price_three, price_four],
	}
	return render(request, 'stocks/doughnut.html', context3)

def line(request):
	item_one = request.POST.get("item_one")
	price_one = request.POST.get("price_one")
	item_two = request.POST.get("item_two")
	price_two = request.POST.get("price_two")
	item_three = request.POST.get("item_three")
	price_three = request.POST.get("price_three")	
	item_four = request.POST.get("item_four")
	price_four = request.POST.get("price_four")

	context4 = {
		"items": [item_one, item_two, item_three, item_four],
		"prices": [price_one, price_two, price_three, price_four],
	}
	return render(request, 'stocks/line.html', context4)

def get_data_bar(request):
	item_one = request.POST.get("item_one")
	price_one = request.POST.get("price_one")
	item_two = request.POST.get("item_two")
	price_two = request.POST.get("price_two")
	item_three = request.POST.get("item_three")
	price_three = request.POST.get("price_three")	
	item_four = request.POST.get("item_four")
	price_four = request.POST.get("price_four")

	two_item_one = request.POST.get("two_item_one")
	two_price_one = request.POST.get("two_price_one")
	two_item_two = request.POST.get("two_item_two")
	two_price_two = request.POST.get("two_price_two")
	two_item_three = request.POST.get("two_item_three")
	two_price_three = request.POST.get("two_price_three")	
	two_item_four = request.POST.get("two_item_four")
	two_price_four = request.POST.get("two_price_four")

	add_1 = int(price_one) + int(price_two)
	add_2 = int(price_three) + int(price_four)
	add_3 = int(two_price_one) + int(two_price_two) 
	add_4 = int(two_price_three) + int(two_price_four)
	# print(add)

	context2 = {
		"items": [item_one, item_two, item_three, item_four, two_item_one, two_item_two, two_item_three, two_item_four],
		"prices": [price_one, price_two, price_three, price_four,two_price_one, two_price_two, two_price_three, two_price_four],
	
		"addition":[add_1, add_2, add_3, add_4]
	}
	
	return render(request, 'stocks/charts.html', context2)

def get_data_doughnut(request):
	item_one = request.POST.get("item_one")
	price_one = request.POST.get("price_one")
	item_two = request.POST.get("item_two")
	price_two = request.POST.get("price_two")
	item_three = request.POST.get("item_three")
	price_three = request.POST.get("price_three")	
	item_four = request.POST.get("item_four")
	price_four = request.POST.get("price_four")

	context3 = {
		"items": [item_one, item_two, item_three, item_four],
		"prices": [price_one, price_two, price_three, price_four],
	}
	return render(request, 'stocks/chartsTwo.html', context3)

def get_data_line(request):
	day_one = request.POST.get("day_one")
	day_two = request.POST.get("day_two")
	day_three = request.POST.get("day_three")
	day_four = request.POST.get("day_four")
	day_five = request.POST.get("day_five")
	day_six = request.POST.get("day_six")	
	day_seven = request.POST.get("day_seven")
	day_eight = request.POST.get("day_eight")
	day_nine = request.POST.get("day_nine")
	day_ten = request.POST.get("day_ten")

	two_day_one = request.POST.get("two_day_one")
	two_day_two = request.POST.get("two_day_two")
	two_day_three = request.POST.get("two_day_three")
	two_day_four = request.POST.get("two_day_four")
	two_day_five = request.POST.get("two_day_five")
	two_day_six = request.POST.get("two_day_six")	
	two_day_seven = request.POST.get("two_day_seven")
	two_day_eight = request.POST.get("two_day_eight")
	two_day_nine = request.POST.get("two_day_nine")
	two_day_ten = request.POST.get("two_day_ten")

	print(two_day_one+two_day_two+two_day_three+two_day_four+two_day_five+two_day_six+two_day_seven+two_day_eight+two_day_nine+two_day_ten)

	context4 = {
		"items": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
		"prices": [day_one, day_two, day_three, day_four, day_five, day_six, day_seven, day_eight, day_nine, day_ten],
		"two_prices": [two_day_one, two_day_two, two_day_three, two_day_four, two_day_five, two_day_six, two_day_seven, two_day_eight, two_day_nine, two_day_ten],
	}
	return render(request, 'stocks/chartsThree.html', context4)