#Q1 Create and access list elements
my_list = [1,2,3,4,5,6,7,8,9]
print(type(my_list))
print(my_list)
print([my_list[1]]) #Indexing starts from 0 
my__list=['apple', 'banana', 'cherry', 'dragon fruit']
print(type(my__list))
print(my__list)
print([my__list[3]])

#Q2 Find max/min from list

marks=[55,65,76,78,66,88,46,78]
print(marks)
print(max(marks))


#Q3 Sum of list elements

num=[10,20,30,40,50,60,70,80,90]
total=sum(num)
print("Sum of Numbers is: ",total)

#Q4 List of even Numbers

numb=[1,2,3,4,5,6,7,8,9,10]
even_num=[]
for num in numb:
    if num%2 ==0:
        even_num.append(num)
print("Even Numbers are: ", even_num)

#Q5 Count frequency of element

num= [1,2,3,1,3,43,2,4,3,2,56,32,4,2,2,3]

frq={}
for i in num:
    if i in frq:
        frq[i] +=1
      
    else:
        frq[i] =1

print("Frequency",frq)
          
#Q6 Remove Duplicates
# Use for loop to keep Orginal Order

num=[1,21,2,23,3,2,3,2,1,4,56]

unique_num=[]
for numbers in num:
    if numbers not in unique_num:
        unique_num.append(numbers)
print(unique_num)

#Q7 Reverse list
lst=[1,2,3,4,5,6,7,8,9,0]
lst.reverse()
print(lst)

#Q8 Tuple Operations
tup=(1,2,3,4,5,6,7,8,9,0)

##indexing
print(tup[2])

##Slicing
print(tup[1:3])

##Length of tuple
print(len(tup))

##Membership test
print(2 in tup)
print(200 not in tup)

##Concatination
t1=(1,2,3)
t2=(4,5,6)
result=t1+t2
print(result)

##Repetation
t=(1,2,3)
print(t*3)

##tuple packing and Unpacking
id=("Samiksha", 22,"Nanded")
name,age,city=id
print(name)
print(age)
print(city)

## Count&Index method
num=(1,2,32,3,3)
print(num.count(2))
print(num.index(3))


##Q9 Convert list to tuple
lst=[1,2,3,4,5,6,7,8,9]
tup=tuple(lst)
print(tup)

##Q10 Nested list print

nested_lst=[[1,2],[2,3],[4,5]]
print(nested_lst)