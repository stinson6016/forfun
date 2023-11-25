# fizz buzz because why not
from datetime import datetime

time_start = datetime.now()
start_buzz = 1
end_buzz = 100
check_buzz = {
    3 : 'fizz',
    5 : 'buzz'
}

for number in range(start_buzz, end_buzz + 1):
    
    output = ""

    for check in check_buzz:
        if number % check == 0:
            output += check_buzz[check]
    output = output if output != "" else number
    print(output)

time_end = datetime.now()

print(f"\nfizzy buzzy between {start_buzz} to {end_buzz}")
print(f"run start time {time_start}")
print(f"run end time {time_end}")

print("\nBuzz checks:")
for buzz in check_buzz:
    print(f"{buzz} - {check_buzz[buzz]}")