from sympy import *
def find_points_over_equation(n,x,y,m,c ):
    linepointsx=[]
    linepointsy=[]
    X = Symbol('X', real=True)
    Y = Symbol('Y', real=True)
    #takinig the initial coordinates 
    for dataiterator in range(0,n):
        #through applying calculus
        newx=x[dataiterator]
        newy=y[dataiterator]
        distance=(X-newx)**2+((m*X+c)-newy)**2
        derivative_distance=diff(distance)
        dataiterator_roots=solve(derivative_distance)
        #more than one rooty
        if len(dataiterator_roots)>1:
            find_minima_root=[]
            for root in dataiterator_roots:
                minvalue=dataiterator_roots[root]*m+c
                find_minima_root.append(minvalue)
            minima=min(find_minima_root)
            minima_index=(find_minima_root.index(minima))
            final_x=dataiterator_roots[minima_index]

        
        else:
            final_x=dataiterator_roots[0]
        
        Y= final_x *m +c

        linepointsx.append(final_x)
        linepointsy.append(Y)
    return(linepointsx),(linepointsy)





    

