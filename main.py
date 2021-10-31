def get_row():
    row = int(input("Enter the number of row >>> "))
    return row


def get_pcs(row):
    list_of_row = []
    
    for i in range(0, row, 1):
        list_of_row.append(int(input(f"Enter the number of sticks for the row number {i+1} >>> ")))
        
    print(list_of_row)



if __name__ == '__main__':
    row = get_row()
    get_pcs(row)