from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import cProfile
import pstats
import trace


def exp_func(x, a, b, c):
    return a * np.exp(b * x) + c

def timeGraph(f,b,e,s):
    xlist = range(b,e,s)
    ylist = []
    for i in xlist:
        a = datetime.now()
        f(i)
        b = datetime.now()
        ylist.append((b-a).total_seconds()) 
    ylist = [e * 1000 for e in ylist]
    x = np.array(xlist, dtype = float)
    y = np.array(ylist, dtype = float)
    graphPlots(x,y)
    
def funCallGraph(f,b,e,s):
    xlist = range(b,e,s)
    ylist = []
    for i in xlist:
        pr = cProfile.Profile()
        pr.enable()
        pr.runctx('f(i)',{'f':f, 'i':i},{})
        p = pstats.Stats(pr)
        s = p.total_calls
        ylist.append(s)
    x = np.array(xlist, dtype = float)
    y = np.array(ylist, dtype = float)
    graphPlots(x,y)
    
def lineExecGraph(f,b,e,s):
    xlist = range(b,e,s)
    ylist = []
    for i in xlist:
        tracer = trace.Trace(count=True, trace=False)
        tracer.runfunc(f, i)
        results = tracer.results()
        ylist.append(sum(results.counts.values()))
    x = np.array(xlist, dtype = float)
    y = np.array(ylist, dtype = float)
    graphPlots(x,y)
    

def graphPlots(x,y):
    plt.figure()
    plt.subplot(2,3,1)
    plt.title("Linear")
    fit = np.polyfit(x,y,1)
    fit_fn = np.poly1d(fit)
    plt.plot(x,y, 'ro',x, fit_fn(x))
    
    plt.subplot(2,3,2)
    plt.title("Quadratic")
    fit = np.polyfit(x,y,2)
    fit_fn = np.poly1d(fit)
    plt.plot(x,y, 'ro',x, fit_fn(x))
    
    plt.subplot(2,3,3)
    plt.title("Cubic")
    fit = np.polyfit(x,y,3)
    fit_fn = np.poly1d(fit)
    plt.plot(x,y, 'ro',x, fit_fn(x))
    
    plt.subplot(2,3,4)
    plt.title("e^n")
    try:
        popt, pcov = curve_fit(exp_func, x, y)
        plt.plot(x,y, 'ro')
        plt.plot(x, exp_func(x, *popt))
    except:
        plt.plot(x,y, 'ro')
              
    plt.subplot(2,3,5)
    plt.title("nlog(n)")
    coefficients = np.polyfit(x*np.log(x),y,1)
    fit = np.poly1d(coefficients)
    plt.plot(x,y, 'ro')
    plt.plot(x,fit(x*np.log(x)))
    
    plt.subplot(2,3,6)
    plt.title("log(n)")
    coefficients = np.polyfit(np.log(x),y,1)
    fit = np.poly1d(coefficients)
    plt.plot(x,y, 'ro')
    plt.plot(x,fit(np.log(x)))
    plt.show()
    