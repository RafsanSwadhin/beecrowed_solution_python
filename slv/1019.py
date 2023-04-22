input_sec = int(input())
hour = input_sec//3600

minutes = (input_sec%3600)//60

seconds = input_sec%60

print(f"{hour}:{minutes}:{seconds}")