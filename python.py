length=10
width=5
 #area of rectancle
def calculate_area(length,width):
    return length*width

print(calculate_area(length,width))
  #area of perimeter
def calculate_perimeter(length,width):
    return length+width

print(calculate_perimeter(length,width))
 

 #Money saving


def calculate_interest(months ,rate, saved):
    deposit=0
    for _ in range(months):
        deposit += saved
        deposit *= 1 + rate
    return deposit

print(calculate_interest(12, 0.02, 250))




#eligible for discount (age,is student)that retur true if 
#-age is 18 or above
#-or a person

def is_eligible_for_discount(age, is_student):
    x=False
    if age<18 or age >60:
        x=True
    elif is_student == True:
        x=True
    else: 
        x=False
    return x

print(is_eligible_for_discount(20, False))

  




