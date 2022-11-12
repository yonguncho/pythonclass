#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World!!!")


# In[12]:


money = True

if money == True:
    print("택시를 타자")
else:
    print("걸어 가자")
    


# In[14]:


money = 500

if money >= 5000:
    print("택시를 타자")
elif money >= 1000:
    print("버스를 타자")
else:
    print("걸어가자")


# In[26]:


#학생의 설정을 입력 받아서 
#점수가 90 이상이면 'A'학점 입니다.
#점수가 80 이상이면 'B'학점 입니다.
#점수가 70 이상이면 'C'학점 입니다.
#점수가 60 이상이면 'D'학점 입니다.
#나머지는 모두 'F' 학점입니다.

score = int(input ())

if score >= 90: 
    print("A 학점 입니다")
    
elif score >= 80:
    print("B 학점 입니다")
    
elif score >= 70:
    print("C 학점 입니다")
    
elif score >= 60:
    print("D 학점 입니다")
    
else:
    print("F 학점 입니다")



# In[29]:


#while

num = 10

while num >= 0:
    print(num)
    num = num -1


# In[32]:


prompt = "1. 덧셈 / 2. 뺄셈 / 3. 곱셈 / 4. 나눗셈 / 5. 종료"
num = 0

while num <= 4:
    print(prompt)
    num = int(input())
    


# In[34]:


no = 0

while no <= 10:
    print(no)
    no = no +1


# In[35]:


#True는 반드시 대분자 T로 해야한다.

no = 0

while True:     
    print(no)
    no = no +1
    
    if no > 10:
        break
    


# In[219]:


no = 1
sum = 0

while no <= 100:

    no = no + 1  # 1) 번 방법: if 빠지고 다시 올라와서 while 밑에.. 1)번 또는 2)번 둘 중 편한대로 사용

    if no % 3 == 0:
        sum = sum + no
            
    #no = no + 1 #python: no+=1 , java: no++; 2)번 방법: if가 빠지고 나서
        
print(sum)


# In[170]:


#For 구문
for  변수명 in 리스트():
     구행 구문


# In[173]:


for i in [1,2,3,4,5,6,7,8,9]:
    print(i)


# In[184]:


math = [80, 90, 70, 70, 100]

j = 1

for i in math:

    if i >= 90:
        print(j, "번째 학생은 합격입니다.")
    else:
        print(j, "번째 학생은 불합격입니다.")

    j += 1


# In[185]:


for i in  [1,2,3,4,5,6,7,8,9,10]:
    print(i)
    


# In[187]:


#짝수만 찍을 때

for i in  [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 == 0:
        print(i)


# In[188]:


#홀수만 찍을 때

for i in  [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 != 0:
        print(i)


# In[190]:


#Continue 

for i in  [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 != 0:
        continue   #Continue를 만나면 아래로 안내려가고 위로 다시 올린다

    print(i)


# In[191]:


#range 함수

print(range(1,11))



# In[192]:


for i in range(1,11): #두 번째 수는 미만
    print(i)


# In[223]:


# for 문으로 구구단 출력하기

for i in range (2,10): #i는 단을 표현
    for j in range (1,10):
        print(i*j, end= "\t")
    print()  #그냥 print()는 줄바꿈을 의미한다


# In[217]:


for i in range (1, 10):
    for j in range (2, 10):
        print (i*j, end="\t")
    print()
        


# In[226]:


#range를 사용하여 100이하의 수 중 짝수들만의 합계를 구하세요

sum = 0

for i in range (1, 101):
    i += 1
    if i % 2 ==0:
        sum += i
print(sum)


# In[232]:


#range를 사용하여 100이하의 수 중 짝수들만의 합계를 구하세요
#range(start,stop,step)

#for i in range(10): #start를 생략하면 0에서 시작한다.
#    print(i)

for i in range(0,11,2): #stop을 생략하면 1씩 증가
    print(i)


# In[240]:


#리스트 축약/내포 List Comprehension
#리스트를 좀더 편리하고 직관적으로 만드는 방법이다.

list1 = [1,2,3,4]

print(list1)

list2 = [num for num in list1] #list1앞에 num을 받고, 이 num이 for 앞 num에 전달

print(list2)

list3 = [num*2 for num in list1] #앞 리스트에서 값을 꺼내 연산

print(list3)

list4 = [num for num in list1  if num % 2 == 0] 
#list1에서 num을 꺼내서 조건에 만족하면 맨 앞 num으로 리스트 가져옴

print(list4)


# In[249]:


no = 70

if no >= 70:
    print("합격")
else:
    print("불합격")
    

print("합격입니다." if no >= 80  else "불합격입니다.")
    


# In[ ]:




