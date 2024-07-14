# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    index = 0
    while index < len(my_list):
        if my_list[index] == 0:
            index += 1
            continue
        elif my_list[index] < 0:
            index += 1
            break
        print(my_list[index])
        index += 1





































