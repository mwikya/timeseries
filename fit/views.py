from django.shortcuts import render
from django.contrib import messages
import math

def home(request):
    return render(request, 'home.html',)

def fit_curve(request):
	if request.method == "POST":
		years = request.POST.get('years').split(',')
		values = request.POST.get('values').split(',')
		n = len(years)
		middle = int(request.POST.get('middle'))	
		t = [int(yr)-int(middle) for yr in years]	
		t2 = [v**2 for v in t]				
		X_t = [float(v) for v in values]
		fittype = request.POST.get('fittype')
		if len(years) != len(X_t):
			messages.add_message(request, messages.WARNING, 
				"Years and Values length don't match"
			)
			return render(request, 'straight.html')
		else: 
			if fittype == 'straight':
				t_X_t = []
				for i in range(len(t)):
					t_X_t.append(int(X_t[i])*t[i])	
				b_hat = round((n*sum(t_X_t) - sum(t)*sum(X_t))/(n*sum(t2)-sum(t)**2),4)
				a_hat = round((sum(X_t) - b_hat*sum(t))/n,4)
				x_bar_t = [round(a_hat+(v*b_hat),2) for v in t]
				variation = []
				for i in range(n):
					variation.append(round(X_t[i]-x_bar_t[i],2))
				context = {
					'fittype':fittype,'years':years,
					't':t,'xt':X_t,'t2':t2,'sum_X_t':round(sum(X_t),2),
					'middle':middle,'txt':t_X_t,'sum_t':round(sum(t),2),'sum_t2':round(sum(t2),2),
					'b_hat':b_hat,"a_hat":a_hat,'x_bar_t':x_bar_t,
					'variation':variation,'sum_t_X_t':round(sum(t_X_t),2)
				}
				return render(request, 'straight.html',context)
			elif fittype == 'exponential':
				V = [round(math.log(v),4) for v in X_t]
				t_V = []
				for i in range(n):
					t_V.append(round(t[i]*V[i],3))
				B_hat = round((n*sum(t_V) - sum(t)*sum(V))/(n*sum(t2)-sum(t)**2),4)
				A_hat = round((sum(V) - B_hat*sum(t))/n,4)

				b_hat =round(math.exp(B_hat),4)
				a_hat = round(math.exp(A_hat),4)
				y_hat = [round(a_hat*b_hat**v,4) for v in t]
				variation = []
				for i in range(n):
					variation.append(round(X_t[i]-y_hat[i],4))
				context = {
					'fittype':fittype,'years':years,
					't':t,'Y':X_t,'t2':t2,"sum_t":round(sum(t),4),'sum_t2':round(sum(t2),4),
					'middle':middle,'V':V, 'sum_V':round(sum(V),4),
					'B_hat':B_hat,"A_hat":A_hat,
					'b_hat':b_hat,"a_hat":a_hat,
					't_V':t_V,"sum_t_V":round(sum(t_V),4),
					'y_hat':y_hat,'variation':variation,
				}				
				return render(request, 'straight.html',context)
			elif fittype == '':
				pass
			elif fittype == '':
				pass								
	else:
		return render(request, 'straight.html')