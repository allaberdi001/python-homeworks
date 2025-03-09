universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    enrollment_values=[]
    tuition_fees=[]
    for i in range(len(universities)):
        enrollment_values.append(universities[i][1])
        tuition_fees.append(universities[i][2])
    return enrollment_values,tuition_fees

def mean(l):
    return sum(l)/len(l)
def median(l):
    l.sort()
    if len(l)%2==1:
        return l[(len(l)+1)//2-1]
    else:
        return (l[len(l)//2-1]+l[len(l)//2])/2
enrollment_values,tuition_fees=enrollment_stats(universities)
print("******************************")
print(f"Total students: {sum(enrollment_values):,}")
print(f"Total tuition: $ {sum(tuition_fees):,}")
print()
print(f"Student mean: {mean(enrollment_values):,.2f}")
print(f"Student median: {median(enrollment_values):,}")
print()
print(f"Tuition mean: $ {mean(tuition_fees):,.2f}")
print(f"Tuition median: $ {median(tuition_fees):,}")
print("******************************")
