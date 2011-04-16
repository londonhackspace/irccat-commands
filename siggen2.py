#!/usr/bin/python
#changes  = [(period, colour)]
#documentation
#type signatures
#Make seperate module
import time as T
import urllib2
import math as M
import pyparsing as P
red = [255,0,0]
green = [0, 255, 0]
blue = [0,0,255]
black = [0,0,0]


#Colour -> Colour -> Colour
def addcol (c1, c2):
   return [min(max(a + b, 0), 255) for a, b in zip( c1, c2)]

#Colour -> Colour -> Colour
def meancol(c1, c2):
   return [int((a+b)/2) for a,b in zip(c1, c2)]



#Colour -> Float -> Colour
def scalecol(c1, sf):
   #print c1
   #printsig 
   return [int(a*sf) for a in c1 ]

sigred = [(1,red)]
sigblack = [(1,black)]


sig1 = [(1, red), (5,  green)]
sig2 = [(2,4), (3, 3)]


#This finds out whether the first (0) or the second signal (1) is the smallest
#Flint -> Flint -> Maybe Int
def findmin (perioda, periodb):
  if perioda == float("infinity"):
    if periodb == float("infinity"):
      return None
    else:
      return 1
  else:
    if periodb == float("infinity"):
      return 0
    else:
      if perioda< periodb:
	return 0
      else:
        return 1

#None in colour signifys a pause
#None in time signifies the end ofa a signal

#List a -> Signal a
def listtogen (xs):
 for x in xs:
   #print x
   yield x


#a -> Signal a
def forever(x):
   return listtogen([(float("infinity"),x)])

#No well defined type signature. Kinda like Signal a -> Maybe a
def attemptNextSignal (gen):
  try:
    return gen.next()
  except StopIteration:
    return float("infinity"), None

#Maybe b -> Maybe b -> (b->b->b) -> b
#Well strictly all the bs can be different classes in which case it is undefined
def maybefunc(a, b, func):
 if a ==None:
   return b
 elif b == None:
   return a
 else:
   return func (a,b)

#Maybe Int -> Maybe Int -> Maybe Int
def infadd (a,b):
 if a ==None:
   return None
 elif b == None:
   return None
 else:
   return a + b

#Signal a -> Int -> Signal a
def cutoff (sig, end):
  time = 0
  while True: 
    try: 
      t,c = sig.next()
      if t == None:
        raise StopIteration
      oldtime = time
      time = t +time
      if time > end:
        yield (end-oldtime),c
	raise StopIteration
      else:
        yield t,c
    except StopIteration:
      raise
#Signal a -> Signal a -> Signal a
def concat (siga, sigb):
  firstsignal = True
  while firstsignal: 
    try:
      yield siga.next()
    except StopIteration:
      firstsignal = False
  while True:
    try: 
      yield sigb.next()
    except StopIteration:
      raise



def repeat (sig):
  ls = []
  for x in sig:
    yield x
    ls.append(x)
  while True: 
    for x in ls:
      yield x

def sanitise (sig):
  while True:
    try:
      t1, c1 = sig.next()
      try: 
        t2, c2 = sig.next()
        if t2 == 0.0:
          yield (t1, c2)
        else:
          yield (t1, c1)
	  yield (t2, c2)
      except StopIteration:
        yield (t1,c1)
    except StopIteration:
      raise

#Signal a -> Signal b -> (a->b->c) -> Signal c   
def combine(siga, sigb, func):
  return sanitise (combine1 (siga,sigb,func))

#Signal a -> Signal b -> (a->b->c) -> Signal c   
def combine1 (siga, sigb, func):
  fina = False
  finb = False
  
  perioda = None
  periodb = None
  perioda, cola = attemptNextSignal (siga)
  periodb, colb = attemptNextSignal (sigb)
  timea = perioda
  timeb = periodb
  time0 = 0
  while True:
    #print timea
    #print timeb
    nxt = findmin (timea, timeb)
    if (nxt == None): 
      raise StopIteration
    nextstep =maybefunc(timea - time0,timeb-time0,min)
    yield  (nextstep, func (cola , colb))
    time0 = time0+ nextstep
    if (nxt == 0):
      perioda, cola = attemptNextSignal (siga) 
      timea = timea + perioda
    else:
      periodb, colb = attemptNextSignal (sigb)
      timeb = timeb + periodb
 
def add (siga, sigb):
  return combine (siga, sigb, lambda a, b: maybefunc(a,b, addcol))

def printsig (sig):
  tm = 0
  for t, c in sig:
    tm  = maybefunc (tm,  t, lambda a, b: a+b)
    print "at time " + str (tm) + "change to" +  str(c)

#printsig (concat (listtogen(sigred), listtogen(sigblack)) ) 

def timemap (signal, func):
  for t,c in signal:
    yield (func(t), c)

def colourmap (signal, func):
  for t,c in signal:
    yield (t, func(c))



def sample (func, res=0.1):
  x = 0
  while  True:
     yield (res, func(x) )
     #print "Sampling"
     x += res

def makegradient (beginning, end, length):
   return (lambda t:  addcol ( scalecol (beginning, min(1,max(0,(length-t)/length))) ,  scalecol(end,  min(1,max(0,(t/length))) )))


#print x (0.5)

def executechanges( signal , func):
  count = 0
  for (t,c) in signal:
    func (c)
    count = count+ 1
    #print count
    #print "waiting"+ str(t) 
    T.sleep(t)

def squarewave( hi,low, hilength, lowlength):
  while True:
    yield (hilength, hi)
    yield (lowlength, low)

#printsig( cutoff (squarewave (10,0,1,20), 100))

def times2(integer):
  return integer*2

#add (sig1, sig2)
def changecolour (col):
  
  colstr = map (str, col)  
  #print ','.join(colstr)
  #print "http://localhost:8000/_/%s" % ','.join(colstr)
  urllib2.urlopen("http://localhost:8000/_/%s" % ','.join(colstr))

def fadein(col, time=1.0):
   return sample (makegradient (black, col, time), 0.1)

def fadeout(col, time=1.0):
  return sample (makegradient (col, black,time), 0.1)

def scaledsine(t, val):
   return (M.sin(t/val) +1)/2 

def scale(colsig, scalesig):
    return combine (colsig, scalesig, lambda a,b: maybefunc(a,b,scalecol))


def mix (siga, sigb, sigscale):
   add (scale (siga, sigscale), scale(sigb, colourmap(sigscale, lambda a: 1-a)) )


def sine (col, freq):
   return scale( forever( col ), sample (lambda t: scaledsine(t, freq)))
def runcolours(sig):
  executechanges(sig, changecolour)

#printsig (sample (scaledsine, 0.1))

#executechanges (add (sample (makegradient(red,green,1), 0.1 , 1), listtogen(sig1)), changecolour)

#runcolours (cutoff(add( add(sine(green,1),sine(red, 4)), squarewave(black,blue,4,0.3)) , 30))



#runcolours (cutoff(repeat (cutoff (fadein(red,10), 10)), 30))


#changecolour(black)


#mix signal signal val
#overwrite signal signal
#fade ivalue ivalue time
#change value time
