# file_path="exam.log"
# def first_line(file_path):
#     with open(file_path) as file:
#         return file.readline()

# print(first_line(file_path))


# Counting Error Entry
file_path = 'exam.log'
def log_enteries_error(file_path):
    with open(file_path, 'r') as file:
        log_enteries = file.readlines()
        i_count =[i for i in log_enteries if 'ERROR' in i]
        return len(i_count)

print(log_enteries_error(file_path))

file_path = 'exam.log'
def log_enteries_info(file_path):
    with open(file_path, 'r') as file:
        log_enteries = file.readlines()
        i_count_info =[i for i in log_enteries if 'INFO' in i]
        return len(i_count_info)

print(log_enteries_info(file_path))


#Counting the number of enteries
file_path = 'exam.log'
def log_enteries_count(file_path):
    with open(file_path, 'r') as my_file:
        log_enteries = my_file.readlines()
    return len(log_enteries)

print(log_enteries_count(file_path))



# Print the most frequent user
from collections import Counter
file_path = 'exam.log'
def error_level_number(file_path):
    with open(file_path, "r") as file:
        user_entries = [line.split('\t')[1]for line in file]
        user_counts = Counter(user_entries)
        # return user_counts['ERROR']
        return user_counts

print(error_level_number(file_path))


#Calculating the least time
file_path= 'exam.log'
def log_enteries_date(file_path):
    complete_date = []
    with open(file_path, 'r') as file:
        log_enteries = file.readlines()
        for i in log_enteries:
            complete_date.append(i[10:22])
        max_time = max(complete_date)
        min_time = min(complete_date)
        return min_time, max_time

print(log_enteries_date(file_path))

from collections import Counter
file_path = 'exam.log'
def log_enteries_transactions(file_path):
    with open(file_path, 'r') as file:
        lists = {}
        log_enteries = file.readlines()
        i_count_info =[i.split('\t')for i in log_enteries if 'transaction' in i]
        count = 0
        for i in range(17018,17315,3):
            while count < len(i_count_info):
                if i in i_count_info:
                    lists.append(i_count_info[count])
                count+=1

        # user_counts = Counter(i_count_info)
        return lists

print(log_enteries_transactions(file_path))



# file_path = 'exam.log'
# def error_level_number(file_path):
#     with open(file_path, "r") as file:
#         user_entries_transactions = [line.split('\t')[4]for line in file if 'transaction' in line]
#         ids = []
#         for i in user_entries_transactions:
#             same = i.split(' ')[1]
#             if len (same) == 6:
#                 ids.append(same)
#         return ids
        # user_entries_transactions_date = [line.split('\t')[0]for line in file if 'transaction' in line]
        # user_counts = Counter(user_entries)
#         # return user_counts['ERROR']
#         print(user_entries_transactions)
#         # print(user_entries_transactions_date)

# print(error_level_number(file_path))
# # error_level_number(file_path)
