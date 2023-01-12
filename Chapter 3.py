# def print_grid():
#     print('+----+----+')
#     print('/    /    /')
#     print('/    /    /')
#     print('/    /    /')
#     print('/    /    /')
#     print('+----+----+')
#     print('/    /    /')
#     print('/    /    /')
#     print('/    /    /')
#     print('/    /    /')
#     print('+----+----+')

# def print_grid():
#     print(("+" + "-" * 4) * 2 + "+")
#     print(("|" + " "*4)*2 + "|")
#     print(("|" + " "*4)*2 + "|")
#     print(("|" + " "*4)*2 + "|")
#     print(("|" + " "*4)*2 + "|")
#     print(("+" + "-" * 4) * 2 + "+")
#     print(("|" + " "*4)*2 + "|")
#     print(("|" + " "*4)*2 + "|")
#     print(("|" + " "*4)*2 + "|")
#     print(("|" + " "*4)*2 + "|")
#     print(("+" + "-" * 4) * 2 + "+")

# def print_grid(num_columns, num_rows):
#     a = ("+" + "-" * 4) * num_columns + "+" + "\n"
#     b = ("|" + " "*4) * num_columns + "|" + "\n"
#     print(a + b*num_rows + b + a + b*num_rows + b + a)

def print_grid(num_columns, num_rows, x="+", y=" - ", z="|"):
    a = (f"{x}{y*4}")*num_columns + "+"
    b = (f"{z}{' '*4*len(y)}")*num_columns + "|"
    row = a + "\n" + (b + "\n")*4
    rows = row * num_rows + a
    print (rows)

# def print_grid(x, y, z, h):
    # x = "+"
    # y = "-"
    # z= "|"
    # h = " "
    # a = (f"{x}{y*4}")*num_columns + "+"


# default parameters là các giá trị mặc định mà nếu không define trong main thì sẽ không thay đổi. Khi define trong main bằng 1 giá trị mới, giá trị mới sẽ thay thế giá trị đã cho trước đó
# array/list có index bắt đầu bằng 0
# len(string) là độ dài của string đó
# VD string HELLO có string[0] là H

# def print_grid(num_columns, num_rows):
#     print(("+" + "-" * 4) * num_columns + "+")
#     print((("|" + " "*4) * num_columns + "|" + "\n") * num_rows)
#     print(("+" + "-" * 4) * num_columns + "+")
#     print((("|" + " "*4) * num_columns + "|" + "\n") * num_rows)
#     print(("+" + "-" * 4) * num_columns + "+")

def main():
    print_grid(10, 10, x="o")
    pass

if __name__ == "__main__":
    main()



