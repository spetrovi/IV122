import sys, copy

def make_list_from_list(lis):
  result = []
  for i in lis:
    result.append([i])
  return result
#permutacie
"""
def perm(lis):
  if len(lis) == 2: #rekurzivna zarazka
    return [[lis[0],lis[1]],[lis[1],lis[0]]]
  new_list = []
  result = []
  for i in range(0,len(lis)):
    new_list = copy.deepcopy(lis)
    remnant = new_list.pop(i)
    new_list = perm(new_list)
    for j in range(0,len(new_list)):
      new_list[j] = [remnant]+new_list[j]
    result += new_list  
  return result
"""

#permutacie su variacie bez opakovania, kde n==k
def perm(lis):
  return var(lis,len(lis))

#kombinacie
def comb(lis,k):
  result = []
  if k == 1:
    return make_list_from_list(lis)
  if k == 2: #rekurzivna zarazka
    tmp_list = copy.deepcopy(lis)
    for i in range(0,len(tmp_list)):
      remnant = tmp_list.pop(0)
      for j in range(0,len(tmp_list)):
	element = [remnant]+[tmp_list[j]]
	result.append(element)
    return result 
  
  for i in range(0,len(lis)-2):
    remnant = lis.pop(0)
    new_list = comb(lis,k-1)
    for j in range(0,len(new_list)):
      new_list[j] = [remnant]+new_list[j]
    result += new_list  
  return result

#kombinacie s opakovanim
def comb_repeat(lis,k):
  result = []
  if k == 1:
    return make_list_from_list(lis)
  if k == 2: #rekurzivna zarazka
    tmp_list = copy.deepcopy(lis)
    for i in range(0,len(lis)):
      remnant = tmp_list[0]
      for j in range(0, len(tmp_list)):
	element = [remnant]+[tmp_list[j]]
	result.append(element)
      tmp_list.pop(0)
    return result
  
  for i in range(0,len(lis)):
    remnant = lis[i]
    new_list = comb_repeat(lis,k-1)
    for j in range(0,len(new_list)):
      new_list[j] = [remnant]+new_list[j]
    result += new_list
  return result
  
def var(lis,k):
  result = []
  if k == 1:
    return make_list_from_list(lis)
  if k == 2: #rekurzivna zarazka
    tmp_list = copy.deepcopy(lis)
    for i in range(0,len(tmp_list)):
      remnant = tmp_list.pop(0)
      for j in range(0,len(tmp_list)):
	element = [remnant]+[tmp_list[j]]
	result.append(element)
      tmp_list.append(remnant)
    return result 
  
  for i in range(0,len(lis)):
    remnant = lis.pop(0)
    new_list = var(lis,k-1)
    for j in range(0,len(new_list)):
      new_list[j] = [remnant]+new_list[j]
    result += new_list
    lis.append(remnant)
  return result
  
def var_repeat(lis,k):
  result = []
  if k == 1:
    return make_list_from_list(lis)
  if k == 2: #rekurzivna zarazka
    tmp_list = copy.deepcopy(lis)
    for i in range(0,len(tmp_list)):
      remnant = tmp_list[i]
      for j in range(0,len(tmp_list)):
	element = [remnant]+[tmp_list[j]]
	result.append(element)
    return result 
  
  for i in range(0,len(lis)):
    remnant = lis[i]
    new_list = var_repeat(lis,k-1)
    for j in range(0,len(new_list)):
      new_list[j] = [remnant]+new_list[j]
    result += new_list
  return result  
  
lis = ['A','B','C','D']
#print perm(lis)
#print comb(lis,3)
#print comb_repeat(lis,3)
#print var(lis,3)
#print var_repeat(lis,3)