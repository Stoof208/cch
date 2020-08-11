k='''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()`~-=_+[]\{}|;':",./<>? '''
def o(a,b):
    c,_,f=lambda _:k.index(_),[0]*a,len(k);e=list(map(c,''.join(b)));d,g=len(e),(sum(e)**2+a**3)%f
    for(h)in range(max(d,a)):i=e[h%f];_[h%a]+=i+g;g+=(i**2)%f
    return''.join(map(lambda _:k[_%f],_))
