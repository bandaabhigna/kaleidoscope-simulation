import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import Figure, subplot
from matplotlib import animation
import math


xa=50
ya=50
xb=100
yb=100
xc=150
yc=150
xd=200
yd=200
xe=250
ye=250
xf=300
yf=300
xg=350
yg=350
xh=400
yh=400
xi=450
yi=450
xj=500
yj=500


def dist1(a,b):
	return abs((math.sqrt(3)*a+b-1500-500*math.sqrt(3))/2.0)

def dist2(a,b):
	return abs((math.sqrt(3)*a-b+1500-500*math.sqrt(3))/2.0)

def dist3(a,b):
	return b

r1a=dist1(xa,ya)
r2a=dist2(xa,ya)
r3a=dist3(xa,ya)

r1b=dist1(xb,yb)
r2b=dist2(xb,yb)
r3b=dist3(xb,yb)

r1c=dist1(xc,yc)
r2c=dist2(xc,yc)
r3c=dist3(xc,yc)

r1d=dist1(xd,yd)
r2d=dist2(xd,yd)
r3d=dist3(xd,yd)

r1e=dist1(xe,ye)
r2e=dist2(xe,ye)
r3e=dist3(xe,ye)

r1f=dist1(xf,yf)
r2f=dist2(xf,yf)
r3f=dist3(xf,yf)

r1g=dist1(xg,yg)
r2g=dist2(xg,yg)
r3g=dist3(xg,yg)

r1h=dist1(xh,yh)
r2h=dist2(xh,yh)
r3h=dist3(xh,yh)

r1i=dist1(xi,yi)
r2i=dist2(xi,yi)
r3i=dist3(xi,yi)

r1j=dist1(xj,yj)
r2j=dist2(xj,yj)
r3j=dist3(xj,yj)

def angle_cos_60(xa,r1a):
	return(xa+r1a*np.cos(np.radians(60)))
def angle_sin_60(ya,r1a):
	return(ya+r1a*np.sin(np.radians(60)))

def angle_cos_120(xa,r1a):
	return(xa+r1a*np.cos(np.radians(120)))
def angle_sin_120(ya,r1a):
	return(ya+r1a*np.sin(np.radians(120)))

mx1a=angle_cos_60(xa,r1a)
my1a=angle_sin_60(ya,r1a)
ix1a=angle_cos_60(mx1a,r1a)
iy1a=angle_sin_60(my1a,r1a)

mx2a=angle_cos_120(xa,r2a)
my2a=angle_sin_120(ya,r2a)
ix2a=angle_cos_120(mx2a,r2a)
iy2a=angle_sin_120(my2a,r2a)

mx3a=xa
my3a=ya-r3a
ix3a=mx3a
iy3a=my3a-r3a


mx1b=angle_cos_60(xb,r1b)
my1b=angle_sin_60(yb,r1b)
ix1b=angle_cos_60(mx1b,r1b)
iy1b=angle_sin_60(my1b,r1b)

mx2b=angle_cos_120(xb,r2b)
my2b=angle_sin_120(yb,r2b)
ix2b=angle_cos_120(mx2b,r2b)
iy2b=angle_sin_120(my2b,r2b)

mx3b=xb
my3b=yb-r3b
ix3b=mx3b
iy3b=my3b-r3b


mx1c=angle_cos_60(xc,r1c)
my1c=angle_sin_60(yc,r1c)
ix1c=angle_cos_60(mx1c,r1c)
iy1c=angle_sin_60(my1c,r1c)

mx2c=angle_cos_120(xc,r2c)
my2c=angle_sin_120(yc,r2c)
ix2c=angle_cos_120(mx2c,r2c)
iy2c=angle_sin_120(my2c,r2c)

mx3c=xc
my3c=yc-r3c
ix3c=mx3c
iy3c=my3c-r3c

mx1d=angle_cos_60(xd,r1d)
my1d=angle_sin_60(yd,r1d)
ix1d=angle_cos_60(mx1d,r1d)
iy1d=angle_sin_60(my1d,r1d)

mx2d=angle_cos_120(xd,r2d)
my2d=angle_sin_120(yd,r2d)
ix2d=angle_cos_120(mx2d,r2d)
iy2d=angle_sin_120(my2d,r2d)

mx3d=xd
my3d=yd-r3d
ix3d=mx3d
iy3d=my3d-r3d

mx1e=angle_cos_60(xe,r1e)
my1e=angle_sin_60(ye,r1e)
ix1e=angle_cos_60(mx1e,r1e)
iy1e=angle_sin_60(my1e,r1e)

mx2e=angle_cos_120(xe,r2e)
my2e=angle_sin_120(ye,r2e)
ix2e=angle_cos_120(mx2e,r2e)
iy2e=angle_sin_120(my2e,r2e)

mx3e=xe
my3e=ye-r3e
ix3e=mx3e
iy3e=my3e-r3e

mx1f=angle_cos_60(xf,r1f)
my1f=angle_sin_60(yf,r1f)
ix1f=angle_cos_60(mx1f,r1f)
iy1f=angle_sin_60(my1f,r1f)

mx2f=angle_cos_120(xf,r2f)
my2f=angle_sin_120(yf,r2f)
ix2f=angle_cos_120(mx2f,r2f)
iy2f=angle_sin_120(my2f,r2f)

mx3f=xf
my3f=yf-r3f
ix3f=mx3f
iy3f=my3f-r3f

mx1g=angle_cos_60(xg,r1g)
my1g=angle_sin_60(yg,r1g)
ix1g=angle_cos_60(mx1g,r1g)
iy1g=angle_sin_60(my1g,r1g)

mx2g=angle_cos_120(xg,r2g)
my2g=angle_sin_120(yg,r2g)
ix2g=angle_cos_120(mx2g,r2g)
iy2g=angle_sin_120(my2g,r2g)

mx3g=xg
my3g=yg-r3g
ix3g=mx3g
iy3g=my3g-r3g


mx1h=angle_cos_60(xh,r1h)
my1h=angle_sin_60(yh,r1h)
ix1h=angle_cos_60(mx1h,r1h)
iy1h=angle_sin_60(my1h,r1h)

mx2h=angle_cos_120(xh,r2h)
my2h=angle_sin_120(yh,r2h)
ix2h=angle_cos_120(mx2h,r2h)
iy2h=angle_sin_120(my2h,r2h)

mx3h=xh
my3h=yh-r3h
ix3h=mx3h
iy3h=my3h-r3h


mx1i=angle_cos_60(xi,r1i)
my1i=angle_sin_60(yi,r1i)
ix1i=angle_cos_60(mx1i,r1i)
iy1i=angle_sin_60(my1i,r1i)

mx2i=angle_cos_120(xi,r2i)
my2i=angle_sin_120(yi,r2i)
ix2i=angle_cos_120(mx2i,r2i)
iy2i=angle_sin_120(my2i,r2i)

mx3i=xi
my3i=yi-r3i
ix3i=mx3i
iy3i=my3i-r3i

mx1j=angle_cos_60(xj,r1j)
my1j=angle_sin_60(yj,r1j)
ix1j=angle_cos_60(mx1j,r1j)	
iy1j=angle_sin_60(my1j,r1j)

mx2j=angle_cos_120(xj,r2j)
my2j=angle_sin_120(yj,r2j)
ix2j=angle_cos_120(mx2j,r2j)
iy2j=angle_sin_120(my2j,r2j)

mx3j=xj
my3j=yj-r3j
ix3j=mx3j
iy3j=my3j-r3j



fig=plt.figure()
plt.axis([-1500,2500,-1500,2500])

line=plt.Line2D((500,500+500*math.sqrt(3)),(1500,0),lw=1)
plt.gca().add_line(line)

line=plt.Line2D((500-500*math.sqrt(3),500),(0,1500),lw=1)
plt.gca().add_line(line)

line=plt.Line2D((500-500*math.sqrt(3),500+500*math.sqrt(3)),(0,0),lw=1)
plt.gca().add_line(line)




fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch_a = plt.Circle((5, -5), 5, color='g')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch1_a = plt.Circle((5, -5), 5, color='g')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch2_a= plt.Circle((5, -5), 5, color='g')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch3_a= plt.Circle((5, -5), 5, color='g')


fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch_b = plt.Circle((5, -5), 10, color='r')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch1_b = plt.Circle((5, -5), 10, color='r')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch2_b = plt.Circle((5, -5), 10, color='r')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch3_b = plt.Circle((5, -5), 10, color='r')


fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch_c = plt.Circle((5, -5), 20, color='b')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch1_c = plt.Circle((5, -5), 20, color='b')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch2_c = plt.Circle((5, -5), 20, color='b')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch3_c = plt.Circle((5, -5), 20, color='b')



fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch_d = plt.Circle((5, -5), 30, color='y')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch1_d = plt.Circle((5, -5), 30, color='y')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch2_d = plt.Circle((5, -5), 30, color='y')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch3_d = plt.Circle((5, -5), 30, color='y')


fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch_e= plt.Circle((5, -5), 40, color='g')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch1_e = plt.Circle((5, -5), 40, color='g')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch2_e= plt.Circle((5, -5), 40, color='g')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch3_e= plt.Circle((5, -5), 40, color='g')


fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch_f = plt.Circle((5, -5), 50, color='r')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch1_f = plt.Circle((5, -5), 50, color='r')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch2_f = plt.Circle((5, -5), 50, color='r')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch3_f = plt.Circle((5, -5), 50, color='r')


fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch_g = plt.Circle((5, -5), 60, color='b')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch1_g = plt.Circle((5, -5), 60, color='b')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch2_g = plt.Circle((5, -5), 60, color='b')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch3_g = plt.Circle((5, -5), 60, color='b')



fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch_h = plt.Circle((5, -5), 70, color='y')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch1_h = plt.Circle((5, -5), 70, color='y')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch2_h= plt.Circle((5, -5), 70, color='y')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch3_h = plt.Circle((5, -5), 70, color='y')


fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch_i= plt.Circle((5, -5), 80, color='g')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch1_i= plt.Circle((5, -5), 80, color='g')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch2_i= plt.Circle((5, -5), 80, color='g')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch3_i= plt.Circle((5, -5), 80, color='g')


fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch_j = plt.Circle((5, -5), 90, color='r')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch1_j = plt.Circle((5, -5), 90, color='r')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch2_j = plt.Circle((5, -5), 90, color='r')

fig.set_dpi(100)
fig.set_size_inches(8,8)
ax=fig.add_subplot(1,1,1)
patch3_j = plt.Circle((5, -5), 90, color='r')

def init():
  

    patch_a.center = (xa,ya)
    ax.add_patch(patch_a)

    patch1_a.center = (ix1a,iy1a)
    ax.add_patch(patch1_a)

    patch2_a.center = (ix2a,iy2a)
    ax.add_patch(patch2_a)

    patch3_a.center = (ix3a,iy3a)
    ax.add_patch(patch3_a)


    patch_b.center = (xb,yb)
    ax.add_patch(patch_b)

    patch1_b.center = (ix1b,iy1b)
    ax.add_patch(patch1_b)

    patch2_b.center = (ix2b,iy2b)
    ax.add_patch(patch2_b)

    patch3_b.center = (ix3b,iy3b)
    ax.add_patch(patch3_b)


    patch_c.center = (xc,yc)
    ax.add_patch(patch_c)

    patch1_c.center = (ix1c,iy1c)
    ax.add_patch(patch1_c)

    patch2_c.center = (ix2c,iy2c)
    ax.add_patch(patch2_c)

    patch3_c.center = (ix3c,iy3c)
    ax.add_patch(patch3_c)


    patch_d.center = (xd,yd)
    ax.add_patch(patch_d)

    patch1_d.center = (ix1d,iy1d)
    ax.add_patch(patch1_d)

    patch2_d.center = (ix2d,iy2d)
    ax.add_patch(patch2_d)

    patch3_d.center = (ix3d,iy3d)
    ax.add_patch(patch3_d)

    patch_e.center = (xe,ye)
    ax.add_patch(patch_e)

    patch1_e.center = (ix1e,iy1e)
    ax.add_patch(patch1_e)

    patch2_e.center = (ix2e,iy2e)
    ax.add_patch(patch2_e)

    patch3_e.center = (ix3e,iy3e)
    ax.add_patch(patch3_e)

    patch_f.center = (xf,yf)
    ax.add_patch(patch_f)

    patch1_f.center = (ix1f,iy1f)
    ax.add_patch(patch1_f)

    patch2_f.center = (ix2f,iy2f)
    ax.add_patch(patch2_f)

    patch3_f.center = (ix3f,iy3f)
    ax.add_patch(patch3_f)

    patch_g.center = (xg,yg)
    ax.add_patch(patch_g)

    patch1_g.center = (ix1g,iy1g)
    ax.add_patch(patch1_g)

    patch2_g.center = (ix2g,iy2g)
    ax.add_patch(patch2_g)

    patch3_g.center = (ix3g,iy3g)
    ax.add_patch(patch3_g)


    patch_h.center = (xh,yh)
    ax.add_patch(patch_h)

    patch1_h.center = (ix1h,iy1h)
    ax.add_patch(patch1_h)

    patch2_h.center = (ix2h,iy2h)
    ax.add_patch(patch2_h)

    patch3_h.center = (ix3h,iy3h)
    ax.add_patch(patch3_h)


    patch_i.center = (xi,yi)
    ax.add_patch(patch_i)

    patch1_i.center = (ix1i,iy1i)
    ax.add_patch(patch1_i)

    patch2_i.center = (ix2i,iy2i)
    ax.add_patch(patch2_i)

    patch3_i.center = (ix3i,iy3i)
    ax.add_patch(patch3_i)


    patch_j.center = (xj,yj)
    ax.add_patch(patch_j)

    patch1_j.center = (ix1j,iy1j)
    ax.add_patch(patch1_j)

    patch2_j.center = (ix2j,iy2j)
    ax.add_patch(patch2_j)

    patch3_j.center = (ix3j,iy3j)
    ax.add_patch(patch3_j)


    return (patch_a,patch1_a,patch2_a,patch3_a,patch_b,patch1_b,patch2_b,patch3_b,patch_c,patch1_c,patch2_c,patch3_c,patch_d,patch1_d,patch2_d,patch3_d,patch_e,patch1_e,patch2_e,patch3_e,patch_f,patch1_f,patch2_f,patch3_f,patch_g,patch1_g,patch2_g,patch3_g,patch_h,patch1_h,patch2_h,patch3_h,patch_i,patch1_i,patch2_i,patch3_i,patch_j,patch1_j,patch2_j,patch3_j)


def animate(i):
    def ani_cos(xa):
    	return (xa+100*np.sin(np.radians(i)))
    def ani_sin(xa):
    	return (xa+100*np.cos(np.radians(i)))
    
    x, y = patch_a.center
    x = ani_sin(xa)
    y = ani_cos(ya)
    patch_a.center = (x, y)

    x, y = patch1_a.center
    x = ani_sin(ix1a)
    y = ani_cos(iy1a)
    patch1_a.center = (x, y)

    x, y = patch2_a.center
    x =ani_sin(ix2a)
    y =ani_cos(iy2a)
    patch2_a.center = (x, y)

    x, y = patch3_a.center
    x =ani_sin(ix3a)
    y =ani_cos(iy3a)
    patch3_a.center = (x, y)


    x, y = patch_b.center
    x =ani_sin(xb)
    y =ani_cos(yb)
    patch_b.center = (x, y)

    x, y = patch1_b.center
    x =ani_sin(ix1b)
    y =ani_cos(iy1b)
    patch1_b.center = (x, y)

    x, y = patch2_b.center
    x =ani_sin(ix2b)
    y =ani_cos(iy2b)
    patch2_b.center = (x, y)

    x, y = patch3_b.center
    x =  ani_sin(ix3b)
    y =  ani_cos(iy3b)
    patch3_b.center = (x, y)


    x, y = patch_c.center
    x =ani_sin(xc)
    y =ani_cos(yc)
    patch_c.center = (x, y)

    x, y = patch1_c.center
    x = ani_sin(ix1c)
    y = ani_cos(iy1c)
    patch1_c.center = (x, y)

    x, y = patch2_c.center
    x =ani_sin(ix2c)
    y =ani_cos(iy2c)
    patch2_c.center = (x, y)

    x, y = patch3_c.center
    x = ani_sin(ix3c)
    y =ani_cos(iy3c)
    patch3_c.center = (x, y)


    x, y = patch_d.center
    x = ani_sin(xd)
    y = ani_cos(yd)
    patch_d.center = (x, y)

    x, y = patch1_d.center
    x =ani_sin(ix1d)
    y =ani_cos(iy1d)
    patch1_d.center = (x, y)

    x, y = patch2_d.center
    x =ani_sin(ix2d)
    y =ani_cos(iy2d)
    patch2_d.center = (x, y)

    x, y = patch3_d.center
    x =ani_sin(ix3d)
    y =ani_cos(iy3d)
    patch3_d.center = (x, y)

    x, y = patch_e.center
    x =ani_sin(xe)
    y =ani_cos(ye)
    patch_e.center = (x, y)

    x, y = patch1_e.center
    x =ani_sin(ix1e)
    y =ani_cos(iy1e)
    patch1_e.center = (x, y)

    x, y = patch2_e.center
    x =ani_sin(ix2e)
    y =ani_cos(iy2e)
    patch2_e.center = (x, y)

    x, y = patch3_e.center
    x =ani_sin(ix3e)
    y =ani_cos(iy3e)
    patch3_e.center = (x, y)

    x, y = patch_f.center
    x =ani_sin(xf)
    y = ani_cos(yf)
    patch_f.center = (x, y)

    x, y = patch1_a.center
    x =ani_sin(ix1f)
    y =ani_cos(iy1f)
    patch1_f.center = (x, y)

    x, y = patch2_f.center
    x =ani_sin(ix2f)
    y =ani_cos(iy2f)
    patch2_f.center = (x, y)

    x, y = patch3_f.center
    x =ani_sin(ix3f)
    y =ani_cos(iy3f)
    patch3_f.center = (x, y)

    x, y = patch_g.center
    x = ani_sin(xg)
    y = ani_cos(yg)
    patch_g.center = (x, y)

    x, y = patch1_g.center
    x = ani_sin(ix1g)
    y = ani_cos(iy1g)
    patch1_g.center = (x, y)

    x, y = patch2_g.center
    x =ani_sin(ix2g)
    y =ani_cos(iy2g)
    patch2_g.center = (x, y)

    x, y = patch3_g.center
    x =ani_sin(ix3g)
    y =ani_cos(iy3g)
    patch3_g.center = (x, y)


    x, y = patch_h.center
    x =ani_sin(xh)
    y =ani_cos(yh)
    patch_h.center = (x, y)

    x, y = patch1_h.center
    x =ani_sin(ix1h)
    y =ani_cos(iy1h)
    patch1_h.center = (x, y)

    x, y = patch2_h.center
    x =ani_sin(ix2h)
    y =ani_cos(iy2h)
    patch2_h.center = (x, y)

    x, y = patch3_h.center
    x =  ani_sin(ix3h)
    y =  ani_cos(iy3h)
    patch3_h.center = (x, y)


    x, y = patch_i.center
    x =ani_sin(xi)
    y =ani_cos(yi)
    patch_i.center = (x, y)

    x, y = patch1_i.center
    x = ani_sin(ix1i)
    y = ani_cos(iy1i)
    patch1_i.center = (x, y)

    x, y = patch2_i.center
    x =ani_sin(ix2i)
    y =ani_cos(iy2i)
    patch2_i.center = (x, y)

    x, y = patch3_i.center
    x = ani_sin(ix3i)
    y =ani_cos(iy3i)
    patch3_i.center = (x, y)


    x, y = patch_j.center
    x = ani_sin(xj)
    y = ani_cos(yj)
    patch_j.center = (x, y)

    x, y = patch1_j.center
    x =ani_sin(ix1j)
    y =ani_cos(iy1j)
    patch1_j.center = (x, y)

    x, y = patch2_j.center
    x =ani_sin(ix2j)
    y =ani_cos(iy2j)
    patch2_j.center = (x, y)

    x, y = patch3_j.center
    x =ani_sin(ix3j)
    y =ani_cos(iy3j)
    patch3_j.center = (x, y)



    return (patch_a,patch1_a,patch2_a,patch3_a,patch_b,patch1_b,patch2_b,patch3_b,patch_c,patch1_c,patch2_c,patch3_c,patch_d,patch1_d,patch2_d,patch3_d,patch_e,patch1_e,patch2_e,patch3_e,patch_f,patch1_f,patch2_f,patch3_f,patch_g,patch1_g,patch2_g,patch3_g,patch_h,patch1_h,patch2_h,patch3_h,patch_i,patch1_i,patch2_i,patch3_i,patch_j,patch1_j,patch2_j,patch3_j)



anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)

fig.suptitle('kaleidoscope simulation',fontsize=14,fontweight='bold')

plt.show()

