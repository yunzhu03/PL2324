import re
from sys import argv

on = r'[Oo][Nn]'
on_re = re.compile(on)

off = r'[Oo][Ff]{2}'
off_re = re.compile(off)

switch = r'(?=[Oo][Nn]|[Oo][Ff]{2})'
switch_re = re.compile(switch)

digit_or_sum = r'\d+|='
digit_or_sum_re = re.compile(digit_or_sum)

end_of_line = r'\n$'
end_of_line_re = re.compile(end_of_line)

def is_end_of_line(str):
    return end_of_line_re.match(str)

def soma(str,accumulator):
    res = 0
    list = digit_or_sum_re.findall(str)
    for element in list:
        if element.isdigit():
            res += int(element)
        else:
            print(res+accumulator)
    return res

def not_soma(str,accumulator):
    res = 0
    list = digit_or_sum_re.findall(str)
    for element in list:
        if not element.isdigit():
            print(res+accumulator)
            

def separate(file):
    res = []
    lines = file.readlines()
    for line in lines:
        res += switch_re.split(line)
    return res
    
def switch_handler(list):
    last_is_on = False
    res = 0
    for str in list:
        if on_re.match(str):
            res += soma(str,res)
            if end_of_line_re.match(str) == None:
                last_is_on = True
            else:
                last_is_on = False
        elif off_re.match(str):
            not_soma(str,res)
            last_is_on = False 
        else: 
            if last_is_on:
                res += soma(str,res)
    return res    

if __name__ == "__main__":
    try:
        file = argv.pop(1)
        with open(file,'r') as f:
            list = separate(f)
            res = switch_handler(list)
            print(res)           
        f.close()
    except Exception as e:
        print(e)