#!/usr/bin/python

import math, random, string


def fill_seq():
	seq = {}
	seq['a']='A@'
	seq['b']='B8'
	seq['c']='C('
	seq['d']='Db'
	seq['e']='E&'
	seq['f']='F;'
	seq['g']='G9'
	seq['h']='H"'
	seq['i']='I!'
	seq['j']='J/'
	seq['k']='K#'
	seq['l']='L|'
	seq['m']='M3'
	seq['n']='Nu'
	seq['o']='O0'
	seq['p']='P?'
	seq['q']='Q,'
	seq['r']='R%'
	seq['s']='S$'
	seq['t']='T+'
	seq['u']='Un'
	seq['v']='V^'
	seq['w']='Wm'
	seq['x']='X*'
	seq['y']='Y"'
	seq['z']='Z]'
	return seq

def generate(w1, w2, b, g):
	myrg = random.SystemRandom()
	seq = fill_seq()
	pw = w1 + w2
	if test_mode:	
		print "DEBUG: pw=", pw
	l_pos = myrg.sample(xrange(len(pw)-1),b)
	for a in range(0,b): 
		pos = l_pos[a] 
		pw = pw[:pos] + myrg.choice(seq[pw[pos]]) + pw[pos+1:]
		if test_mode:
			print "DEBUG: words factor pos,pw=", pos, pw
	for a in range(0,g):
		pos = myrg.randint(0,len(pw))
		pw = pw[:pos] + myrg.choice(string.digits) + pw[pos:]
		if test_mode:	
			print "DEBUG: number factor pos,pw=", pos, pw
	return pw

def binomial(n, k):
	return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def calculate_complexity(w1, w2, b, g):
	c={'entropy':0, 'time':0}
	L = round((len(w1)+len(w2))/2,0)
	num = 30*binomial(L,b)*binomial(L+g,g)*binomial(6,2)*2
	if test_mode:	
		print "DEBUG: num=", num
		print "num2=", 30*binomial(2*L,b)*binomial(2*L+g,g)*binomial(6,2) 
	c['entropy']=math.log(num,2)
	c['time'] = num/3600
	return c


test_mode = False
another = 'y'
while another =='y':
	word1 = raw_input("Insert the first word:")
	word2 = raw_input("Insert the second word:")
	str_beta = raw_input("Insert the number of letters alterations:")
	beta = int(str_beta)
	str_gamma = raw_input("Insert the number of numbers alterations:")
	gamma = int(str_gamma)
	password = generate(word1, word2, beta, gamma)
	complexity = calculate_complexity(word1, word2, beta, gamma)
	print "The password generated is ", password
	print "The additional entropy is %i bit" % (complexity['entropy']) 
	another = raw_input("Try another word combination?[y/N]:")
print "Bye!"

