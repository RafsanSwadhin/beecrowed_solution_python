input_day = int(input())

year = input_day//365
month = (input_day%365)//30

day = (input_day%365)%30

print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{day} dia(s)")
