
no_of_chars=123
#str1=input()
def max_distinct_char(str,n):
    count = [0] * no_of_chars
    for i in range(n):
        count[ord(str[i])]+=1
    max_distinct=0
    for i in range(no_of_chars):
        if(count[i]!=0):
            max_distinct+=1    
    return max_distinct 
  
def smallesteSubstr_maxDistictChar(str): 
  
    n=len(str)
    max_distinct=max_distinct_char(str, n) 
    minl=n
    for i in range(n):
        for j in range(n):
            substr=str[i:j] 
            substr_lenghth = len(substr) 
            sub_distinct_char=max_distinct_char(substr,  
                                                  substr_lenghth)
            if (substr_lenghth < minl and max_distinct == sub_distinct_char):
                minl=substr_lenghth 
  
    return minl 

str1=input()
l=smallesteSubstr_maxDistictChar(str1); 
print( "The length of the smallest substring", 
           "consisting of maximum distinct", 
           "characters :", l)
