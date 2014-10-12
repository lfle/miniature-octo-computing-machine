#!/usr/bin/python
# coding=UTF-8
# Filename : datatemp.py

from matplotlib.dates import strpdate2num
from matplotlib.ticker import MultipleLocator
import matplotlib.dates as mdates
import numpy as np
from pylab import *

datafile = ('Aa/Aa.csv')
print 'loading', datafile

times, Notas, Faltas  = np.loadtxt(
    datafile, delimiter=',',
    converters={0:strpdate2num('%d-%b-%y-%H:%M:%S') },
    skiprows=1, usecols=(0,1,2), unpack=True)

fig = figure()
ax1 = fig.add_subplot(211)
ax1.set_title('$\mathbf{Frequ\^{e}ncia}$ em %', color='r')
ax1.bar(times, Faltas, color='r')	
ax1.axvspan(*mdates.datestr2num(['12/20/12', '02/13/13']), facecolor='r', alpha=0.3)
ax1.autoscale_view(tight='True', scalex=True, scaley=False)
ax1.yaxis.set_label_coords(-0.065, 0.5)
ax1.set_ylim(0,100)
ax1.axhline(y=75, linewidth=1, color='black')
ax1.annotate('Atingiu 75%!', xy=(.75, .81),  xycoords='axes fraction',
                horizontalalignment='center', verticalalignment='center')

for tl in ax1.get_yticklabels():
    tl.set_color('red')
locator   = MultipleLocator(14)
ax1.xaxis.set_major_locator(locator)
setp(gca(), 'xticklabels', [])
datafile = ('Aa/Aa.csv')
print 'loading', datafile

times, Notas, Faltas  = np.loadtxt(
    datafile, delimiter=',',
    converters={0:strpdate2num('%d-%b-%y-%H:%M:%S') },
    skiprows=1, usecols=(0,1,2), unpack=True)

ax3 = fig.add_subplot(212)
ax3.set_title('$\mathbf{Nota\ Acumulada}$', color='b')
ax3.plot_date(times, Notas, 'b-',linewidth=2.0)
ax3.yaxis.set_label_coords(-0.065, 0.5)
ax3.set_ylim(0,10)
ax3.annotate('Vacation', xy=(.27, .49),  xycoords='axes fraction',
                horizontalalignment='center', verticalalignment='center')
for tl in ax3.get_yticklabels():
    tl.set_color('blue')

ax3.autoscale_view(tight='True', scalex=True, scaley=False)
ax3.grid(True)
ax3.axvspan(*mdates.datestr2num(['12/20/2012', '02/13/2013']), color='b', alpha=0.3)
#	
# Imprime as datas no eixo x
locator   = MultipleLocator(14)
formatter = mdates.DateFormatter('%d/%m')
ax3.xaxis.set_major_formatter(formatter)
ax3.xaxis.set_major_locator(locator)

#  Inclina as datas no eixo x para melhorar apresentacao
fig.autofmt_xdate()
show()

datafile = ('Bb/Bb.csv')
print 'loading', datafile

times, Notas, Faltas  = np.loadtxt(
    datafile, delimiter=',',
    converters={0:strpdate2num('%d-%b-%y-%H:%M:%S') },
    skiprows=1, usecols=(0,1,2), unpack=True)

fig = figure()
ax1 = fig.add_subplot(211)
ax1.set_title('$\mathbf{Frequ\^{e}ncia}$ em %', color='r')
ax1.bar(times, Faltas, color='r')
ax1.axvspan(*mdates.datestr2num(['12/20/12', '02/13/13']), facecolor='r', alpha=0.3)	
ax1.autoscale_view(tight='True', scalex=True, scaley=False)
ax1.yaxis.set_label_coords(-0.065, 0.5)
ax1.set_ylim(0,100)
ax1.axhline(y=75, linewidth=1, color='black')
ax1.annotate('Atingiu 75%!', xy=(.75, .81),  xycoords='axes fraction',
                horizontalalignment='center', verticalalignment='center')

for tl in ax1.get_yticklabels():
    tl.set_color('red')

locator   = MultipleLocator(14)
ax1.xaxis.set_major_locator(locator)
setp(gca(), 'xticklabels', [])

datafile = ('Bb/Bb.csv')
print 'loading', datafile

times, Notas, Faltas  = np.loadtxt(
    datafile, delimiter=',',
    converters={0:strpdate2num('%d-%b-%y-%H:%M:%S') },
    skiprows=1, usecols=(0,1,2), unpack=True)
ax3 = fig.add_subplot(212)
ax3.set_title('$\mathbf{Nota\ Acumulada}$', color='b')
ax3.plot_date(times, Notas, 'b-',linewidth=2.0)
ax3.yaxis.set_label_coords(-0.065, 0.5)
ax3.set_ylim(0,10)
ax3.annotate('Vacation', xy=(.27, .49),  xycoords='axes fraction',
                horizontalalignment='center', verticalalignment='center')
for tl in ax3.get_yticklabels():
    tl.set_color('blue')

ax3.autoscale_view(tight='True', scalex=True, scaley=False)
ax3.grid(True)
ax3.axvspan(*mdates.datestr2num(['12/20/2012', '02/13/2013']), color='b', alpha=0.3)
	
# Imprime as datas no eixo x
locator   = MultipleLocator(14)
formatter = mdates.DateFormatter('%d/%m')
ax3.xaxis.set_major_formatter(formatter)
ax3.xaxis.set_major_locator(locator)

#  Inclina as datas no eixo x para melhorar apresentacao
fig.autofmt_xdate()

show()

datafile = ('Cc/Cc.csv')
print 'loading', datafile

times, Notas, Faltas  = np.loadtxt(
    datafile, delimiter=',',
    converters={0:strpdate2num('%d-%b-%y-%H:%M:%S') },
    skiprows=1, usecols=(0,1,2), unpack=True)

fig = figure()
ax1 = fig.add_subplot(211)
ax1.set_title('$\mathbf{Frequ\^{e}ncia}$ em %', color='r')
ax1.bar(times, Faltas, color='r')
ax1.axvspan(*mdates.datestr2num(['12/20/12', '02/13/13']), facecolor='r', alpha=0.3)	
ax1.autoscale_view(tight='True', scalex=True, scaley=False)
ax1.yaxis.set_label_coords(-0.065, 0.5)
ax1.set_ylim(0,100)
ax1.axhline(y=75, linewidth=1, color='black')
ax1.annotate('Atingiu 75%!', xy=(.75, .81),  xycoords='axes fraction',
                horizontalalignment='center', verticalalignment='center')

for tl in ax1.get_yticklabels():
    tl.set_color('red')

locator   = MultipleLocator(14)
ax1.xaxis.set_major_locator(locator)
setp(gca(), 'xticklabels', [])

datafile = ('Cc/Cc.csv')
print 'loading', datafile

times, Notas, Faltas  = np.loadtxt(
    datafile, delimiter=',',
    converters={0:strpdate2num('%d-%b-%y-%H:%M:%S') },
    skiprows=1, usecols=(0,1,2), unpack=True)

ax3 = fig.add_subplot(212)
ax3.set_title('$\mathbf{Nota\ Acumulada}$', color='b')
ax3.plot_date(times, Notas, 'b-',linewidth=2.0)
ax3.yaxis.set_label_coords(-0.065, 0.5)
ax3.set_ylim(0,10)
ax3.annotate('Vacation', xy=(.27, .49),  xycoords='axes fraction',
                horizontalalignment='center', verticalalignment='center')
for tl in ax3.get_yticklabels():
    tl.set_color('blue')

ax3.autoscale_view(tight='True', scalex=True, scaley=False)
ax3.grid(True)
ax3.axvspan(*mdates.datestr2num(['12/20/2012', '02/13/2013']), color='b', alpha=0.3)	
# Imprime as datas no eixo x
locator   = MultipleLocator(14)
formatter = mdates.DateFormatter('%d/%m')
ax3.xaxis.set_major_formatter(formatter)
ax3.xaxis.set_major_locator(locator)

#  Inclina as datas no eixo x para melhorar apresentacao
fig.autofmt_xdate()
show()
