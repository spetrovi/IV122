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

def variations(lis, k):
	result = []
	if k == 0:
		return [[]]
	else:
		for i in range(len(lis)):
			tmp_list = lis[:]
			tmp_list.remove(lis[i])
			some_result = combinations_repeat(tmp_list, k-1)
			for item in some_result:
				result.append([lis[i]]+item)
	return result

def variations_repeat(lis, k):
	result = []
	if k == 0:
		return [[]]
	else:
		for i in range(len(lis)):
			some_result = combinations_repeat(lis[:], k-1)
			for item in some_result:
				result.append([lis[i]]+item)
	return result

def combinations(lis, k):
	result = []
	if k == 0:
		return [[]]
	else:
		for i in range(len(lis)):
			some_result = combinations(lis[i+1:], k-1)
			for item in some_result:
				result.append([lis[i]]+item)
	return result

def combinations_repeat(lis, k):
	result = []
	if k == 0:
		return [[]]
	else:
		for i in range(len(lis)):
			some_result = combinations(lis[i:], k-1)
			for item in some_result:
				result.append([lis[i]]+item)
	return result

#implementacia z minuleho roka
#kombinacie
def comb(lis,k):
  if k == 0:
	return [[]]
  if k == 1:
    return make_list_from_list(lis)
  if k == 2: #rekurzivna zarazka
    tmp_list = lis[:]
    for i in range(0,len(tmp_list)):
      remnant = tmp_list.pop(0)
      for j in tmp_list:
  	element = [remnant]+[j]
  	result.append(element)
    return result 
  result = []
  tmp_list = lis[:]
  for item in tmp_list:
    tmp_list.remove(item)
    new_list = []
    for j in comb(tmp_list,k-1):
      new_list.append([item]+j)

    print new_list
    result.append(new_list)
  print result
  return result

#kombinacie s opakovanim
def comb_repeat(lis,k):
  result = []
  if k == 1:
    return make_list_from_list(lis)
  if k == 2: #rekurzivna zarazka
    tmp_list = lis[:]
    for i in lis:
      remnant = tmp_list[0]
      for j in tmp_list:
	element = [remnant]+[j]
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
    tmp_list = lis[:]
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
    tmp_list = lis[:]
    for i in range(0,len(tmp_list)):
      remnant = tmp_list[i]
      for j in tmp_list:
	element = [remnant]+[j]
	result.append(element)
    return result 
  
  for i in range(0,len(lis)):
    remnant = lis[i]
    new_list = var_repeat(lis,k-1)
    for j in range(0,len(new_list)):
      new_list[j] = [remnant]+new_list[j]
    result += new_list
  return result  

#print combinations(['A','B','C','D'],2)
##print combinations_repeat(['A','B','C','D'],2)
#print variations(['A','B','C','D'],2)
#print variations_repeat(['A','B','C'],2)
