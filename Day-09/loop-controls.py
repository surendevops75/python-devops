# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     if number == 3:
#         break
#     print(number)

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     if number == 3:
#         continue
#     print(number)

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)