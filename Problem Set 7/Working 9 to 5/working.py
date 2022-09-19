import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):

    matches=re.search(r"^([0-9][0-9]?(:\d\d)?) (AM|PM) to ([0-9][0-9]?(:\d\d)?) (AM|PM)$", s)
    if matches:
        first=split_hour(matches.group(1),matches.group(3))
        second=split_hour(matches.group(4),matches.group(6))
        return f"{first} to {second}"
    else:
        raise ValueError

def split_hour(x,b):
    if ":" in x:

        a= x.split(":")
        if int(a[1])<60:
            if b == "AM" and a[0] == "12":
               return "00" + ":"+ a[1]
            elif b == "AM":
               return f"{int(a[0]):02}:{a[1]}"
            elif b == "PM" and a[0] == "12":
               return a[0] +":"+a[1]
            else:
               return str(int(a[0]) + 12) + ":"+ a[1]
        else:
            raise ValueError
    else:
        if b == "AM" and x == "12":
            return "00" + ":"+ "00"
        elif b == "AM":
            return f"{int(x):02}:00"
        elif b == "PM" and x == "12":
            return x+":"+"00"
        else:
            return str(int(x) + 12) + ":"+ "00"


if __name__ == "__main__":
    main()
