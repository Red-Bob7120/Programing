import matplotlib.pyplot as plt


y1 =[350,410,520,695]
y2 =[200,250,385,350]
x = range(len(y1))
plt.bar(x,y1,width = 0.25 ,color = "green")
plt.bar(x,y2,width= 0.3, color="red", bottom = y1)

plt.title('Quarterly sales')
plt.xlabel('Quarters')
plt.ylabel('sales')
xLabel = ['first','second','third','fourth']

plt.xticks(x,xLabel,fontsize = 10)

plt.legend(['chairs','desks'])

plt.show()