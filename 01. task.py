package_paper = int(input())
rolls = int(input())
glue_litters = float(input())
discount = int(input())

all = ((package_paper * 5.80) + (rolls * 7.20) + (glue_litters * 1.20)) * ((100-discount)/100)
print(format(all,".3f"))