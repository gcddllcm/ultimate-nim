import random

def get_pcs():
    pile1 = int(input("Matches in the 1st pile >>> "))
    pile2 = int(input("Matches in the 2nd pile >>> "))
    pile3 = int(input("Matches in the 3rd pile >>> "))
    
    pcs = [pile1, pile2, pile3]
    
    return pcs


def get_random_pcs():
    pile1 = random.randint(1, 1000)
    pile2 = random.randint(1, 1000)
    pile3 = random.randint(1, 1000)
    
    pcs = [pile1, pile2, pile3]
    
    print(pcs)
    
    return pcs



def nim_sum(a, b):
    a_binary_2 = int(bin(a)[2 : ])
    # print(a_binary_2)
    b_binary_2 = int(bin(b)[2 : ])
    # print(b_binary_2)

    sum_binary_2 = str(a_binary_2 + b_binary_2)
    nim_sum = sum_binary_2.replace("2", "0")
    convert_to_int = int(f"{nim_sum}", 2)

    return convert_to_int
    


def calculation(pcs):
    pile1, pile2, pile3 = pcs[0], pcs[1], pcs[2]
    #list of nim sum
    lons = [
        nim_sum(pile1, pile2),
        nim_sum(pile1, pile3),
        nim_sum(pile2, pile3)
    ]
    
    
    if lons[0] == pile3 or lons[1] == pile2 or lons[2] == pile1:
        print("The second player always win this nim.")
    else:
        if pile3 > nim_sum(pile1, pile2):
            print(f"The first player always win by picking {pile3 - nim_sum(pile1, pile2)} pieces from the 3rd pile.")
        elif pile2 > nim_sum(pile1, pile3):
            print(f"The first player always win by picking {pile2 - nim_sum(pile1, pile3)} pieces from the 2nd pile.")
        elif pile1 > nim_sum(pile2, pile3):
            print(f"The first player always win by picking {pile1 - nim_sum(pile2, pile3)} pieces from the 1st pile.")



if __name__ == '__main__':
    pcs = get_pcs()
    calculation(pcs)