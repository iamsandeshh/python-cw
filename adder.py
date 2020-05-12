from binary import insert_val

def half_adder(a,b):
    sum = a^b
    carry = a and b
    return carry,sum

def full_adder(carry_in,a,b):
    carry1,sum1 = half_adder(a,b)
    carry2,sum = half_adder(sum1,carry_in)
    carry = carry1 or carry2
    return carry,sum

def adder():
    first_value,second_value = insert_val()
    c_in = 0
    fin = []

    for i in range(len(first_value)-1,-1,-1):
        add, c_in = full_adder(first_value[i], second_value[i], c_in)
        fin.insert(0,add)
    fin.insert(0,c_in)

    fin = int("".join(str(i) for i in fin))
    print("Result is : ", fin )
