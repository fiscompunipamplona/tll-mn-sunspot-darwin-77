from pylab import plot,show,xlim,ylim,xlabel
from numpy import linspace,sin,cos,loadtxt

x=linspace(0,10,100)
y=sin(x)
z=cos(x)
plot(z,y)
show()
a=open("test.dad", "w")
for i in range(len(x)):
    a.write("%.2f %.2f %.2f\n" % (x[i], y[y], z[i])
        a.close()

b=loadtxt("test.dad",float)
plot(b[:,0], b[:,1], "go")
plot(b[:,0], b[:,2], "r-")

ylim(-1.01, 1.1)
xlabel("radianes")
show()
