s1=set(input("Enter elements with space in between: ").strip().split())
s2=set(input("Enter elements with space in between: ").strip().split())
sim_diff=s1.symmetric_difference(s2)
print(sim_diff)
