from statistics import stdev
from math import log 
from math import sqrt
from random import random 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def rand_exp(mu):
    return -log(random()) / mu

#--- Simulate the M/M/1 queue
#
# Inputs:
#    arrival_rate
#    avg_service_time
#    n: number of simulated customers
#
# Output: the average residence time of customer in the queue

def simulate(arrival_rate, avg_service_time, n):

    # Generate interarrival times
    interarr_times = []
    for i in range(n):
        interarr_times.append(rand_exp(arrival_rate))

    # Generate service times
    serv_times = []
    for i in range(n):
        serv_times.append(rand_exp(1/avg_service_time))

    # Calculate arrival times
    arrival_times = []
    arrival_times.append(interarr_times[0])
    for i in range(1, n):
        arrival_times.append(interarr_times[i] + arrival_times[i - 1])


    # Initialize other lists
    enter_service_times = [0] * n
    dep_times = [0] * n

    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    dep_times[0] = enter_service_times[0] + serv_times[0]

    # Loop over all other arrivals
    for i in range(1, n):
        enter_service_times[i] = max(arrival_times[i], dep_times[i - 1])
        dep_times[i] = enter_service_times[i] + serv_times[i]

    residence_times = [0] * n
    
    # Calculate residence times
    for i in range(n):
        residence_times[i] = dep_times[i] - arrival_times[i]

    return sum(residence_times)/ n

#Utilization & Average Residence Times Plot
def plot(util, sim_res_times):
    plt.figure()
    plt.title("M/M/1 Queue Util & Avg. Res. Times")
    plt.xlabel("Utilization")
    plt.ylabel("Avg. Residence Time")
    plt.plot(util, sim_res_times)
    plt.savefig("MM1_Queue_Plot.pdf", bbox_inches='tight')

#Confidence Intervals Plot
def plot2(ucl, lcl, art):
    plt.figure()
    a_times = []
    start = .05
    for i in range(0, 19):
        a_times.append(start)
        start+= .05
        
    plt.title("M/M/1 Confidence Intervals")
    plt.xlabel("Utilization")
    plt.ylabel("Avg. Residence Times")
    plt.plot(a_times, ucl, label= "UCL", color = "blue")
    plt.plot(a_times, lcl, label = "LCL", color = "green")
    plt.plot(a_times, art, label = "AVG", color = "yellow")
    plt.savefig("MM1_Conf_Int.pdf", bbox_inches='tight')
    

def main():
    arrival_rate = .05
    util = []
    sim_res_times = []

    while arrival_rate <= .95:
        sim_res_times.append(simulate(arrival_rate,1,5000))
        util.append(arrival_rate * 1)
        arrival_rate += .05

    plot(util,sim_res_times)

    arrival_rate = .05
    conf_int_Val = 0

    total_res = 0
    vals = [0] * 5
    ucl = [0] * 19
    lcl = [0] * 19
    art = [0] * 19
    level = 0;

    while arrival_rate <=1.0:

        res = simulate(arrival_rate,1,1000)
        if conf_int_Val % 5 == 0 and conf_int_Val != 0:

            vals[conf_int_Val % 5] = res
            y_bar = total_res/5 
            art[level] = y_bar
            UCL = y_bar + 2.776 * stdev(vals, y_bar)/sqrt(5)
            ucl[level] = UCL
            LCL = y_bar - 2.776 * stdev(vals, y_bar)/sqrt(5)
            lcl[level] = LCL
            print(round(arrival_rate, 3), " UCL is", round(UCL, 3), "LCL is", round(LCL,3))
            arrival_rate += .05
            total_res = 0
            level += 1
        else:
            vals[conf_int_Val % 5] = res
            total_res += res
        conf_int_Val+=1

    plot2(ucl,lcl, art)


if __name__ == '__main__':
    main()
    

