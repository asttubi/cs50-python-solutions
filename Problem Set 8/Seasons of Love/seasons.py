import sys
from datetime import date
import re
import inflect

p = inflect.engine()

def main():
    dtoday=date.today()
    print(get_date(sub_date(input("Date of Birth: ")), dtoday))


def sub_date(b_day):
    result=re.search(r"^(\d\d\d\d)-(\d\d)-(\d\d)$", b_day)
    if not result:
        sys.exit("Invalid date")
    else:
        year=int(result.group(1))
        month=int(result.group(2))
        day=int(result.group(3))
        return date(year, month, day)

def get_date(d1, dtoday):
    delta = dtoday - d1
    return (p.number_to_words(delta.days*24*60, andword="")).capitalize()+" minutes"


if __name__ == "__main__":
    main()
