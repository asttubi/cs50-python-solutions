import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches:=re.search(r"^(.+)\.(.+)\.(.+)\.(.+)$", ip):
        return find_range(matches.groups())
    else:
        return False

def find_range(t):
    response=[]
    for i in t:
        if 0<=int(i)<=255:
            response.append(True)
        else:
            response.append(False)

    if all(response):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
