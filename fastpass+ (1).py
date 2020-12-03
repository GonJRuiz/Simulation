from heapq import heappush, heappop
import random
import math

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def rand_exp(mu):
	
	rand = random.uniform(0, 1)
	
	num = - math.log(rand)/mu
	
	return num
	
def create_event(event_type, mu, time):
	e = (rand_exp(mu) + time, event_type)
	return e

def priority(f):
	rand = random.uniform(0, 1)
	if rand < f:
		return True
	else:
		return False


def simulate(f, arr_rate, s_time, customer_num):
	
	fp_arr = []
	reg_arr = []
	
	fp_est = []
	reg_est = []
	
	fp_departures = []
	reg_departures = []
	
	num_fp = 0
	num_total = 0
	
	events = []
	
	time = 0
	
	heappush(events, create_event('a', arr_rate, time))
	
	while len(events) != 0:
		event = heappop(events)
		time = event[0]
		
		if event[1] == 'a':
			
			#Arrival has f probability of having fastpass
			if priority(f):
				num_fp = num_fp + 1
				fp_arr.append(time)
			else:
				reg_arr.append(time)
			num_total = num_total + 1
				
			#Nobody in line means this person is given service immediately and is also given a departure time
			if num_total == 1:
				heappush(events, create_event('d', s_time, time))
				if num_fp > 0:
					fp_est.append(time)
				else:
					reg_est.append(time)
					
			#If there is another person left in the simulation, give them an arrival time
			if customer_num > 0:
				heappush(events, create_event('a', arr_rate, time))
				
				customer_num = customer_num - 1
		
		elif event[1] == 'd':
			
			#Service departs element
			if num_fp > 0:
				fp_departures.append(time)
				num_fp = num_fp - 1
			else:
				reg_departures.append(time)
			num_total = num_total - 1
			
			#If there is a line, they enter service and are given a departure time
			if num_fp > 0:
				fp_est.append(time)
				heappush(events, create_event('d', s_time, time))
			elif num_total > 0:
				reg_est.append(time)
				heappush(events, create_event('d', s_time, time))
				
	total_res_time_fp = 0
	total_res_time_reg = 0

	for i in range(len(fp_arr) - 1):
		total_res_time_fp = total_res_time_fp + (fp_departures[i]-fp_arr[i])
		
	for i in range(len(reg_arr) - 1):
		total_res_time_reg = total_res_time_reg + (reg_departures[i]-reg_arr[i])
	
	if len(fp_arr) > 0:
		avg_r_time_fp = total_res_time_fp/len(fp_arr)
	else:
		avg_r_time_fp = 0;
	avg_r_time_reg = total_res_time_reg/len(reg_arr)
	
	avg_r_time = (total_res_time_reg + total_res_time_fp)/(len(fp_arr) + len(reg_arr))
	
	return (avg_r_time, avg_r_time_fp, avg_r_time_reg, avg_r_time_fp/avg_r_time_reg)

r_t_avg = []
r_t_avg_fp = []
r_t_avg_reg = []
res_time_ratio = []
x_axis = []

for i in range(0, 100):
	temp = simulate(.01 * i ,.95, 1, 50000)
	
	r_t_avg.append(temp[0])
	r_t_avg_fp.append(temp[1])
	r_t_avg_reg.append(temp[2])
	res_time_ratio.append(temp[3])
	
	x_axis.append(i * .01)

plt.plot(x_axis, r_t_avg)
plt.legend("O")
plt.plot(x_axis, r_t_avg_fp)
plt.legend("F")
plt.plot(x_axis, r_t_avg_reg)
plt.legend("OFR")

plt.title('Average Residence Time for Low Load FastPass Probabilities')
plt.ylabel('Residence Time')
plt.xlabel('Fastpass Probability')

plt.savefig('High_Load.pdf', bbox_inches= 'tight')

for i in range(0, 100):
	print(round(i * .01, 2),  "Fastpass average: ",  round(r_t_avg_fp[i], 4), "Regular average: ", round(r_t_avg_reg[i], 4))
	