#Counting the number of enteries
file_path = 'logfile.txt'
def log_enteries_count(file_path):
    with open(file_path, 'r') as my_file:
        log_enteries = my_file.readlines()
    return len(log_enteries)

# print(log_enteries_count(file_path))



#Retrieving the date in each entrie
file_path = 'logfile.txt'
date = []
time = []
complete_date = []
def log_enteries_date(file_path):
    with open(file_path, 'r') as file:
        log_enteries = file.readlines()
        for i in log_enteries:
            # date.append(i[:10])
            # time.append(i[11:19])
            complete_date.append(i[:19])
        max_time = max(complete_date)
        min_time = min(complete_date)
        return min_time, max_time

print(log_enteries_date(file_path))


# Counting Error Entry
file_path = 'logfile.txt'
def log_enteries_error(file_path):
    count = 0
    with open(file_path, 'r') as file:
        log_enteries = file.readlines()
        i_count =[i for i in log_enteries if 'ERROR' in i]
        # for i in log_enteries:
        #     if 'ERROR' in i:
        #         count += 1
        # return count
        return len(i_count)

print(log_enteries_error(file_path))


#Scripting for the most frequent user accessing the website
# from collections import Counter

# def log_enteries_mfuser(file_path):
    # count = 0
    # final = []
    # names = []
    # word = []
    # word_final = []
    # with open(file_path, 'r') as file:
    #     user_entries = [line.split(' - ')[2].split('"')[1] for line in file if "User" in line]
        # log_enteries = file.readlines()
        # for i in log_enteries:
        #     word.append(i.split(' - ')[2].split('"')[1])
        # return word
        # for i in word:
        #     word_final.append(i.split('"')[1])
        # # return word_final
        # for i in word_final:
        #     if i in names:
        #         count +=1
        #     else:
        #         count = 0   
        # return names, count
        
# print(log_enteries_mfuser(file_path))


#Print the most frequent user
# from collections import Counter
# file_path = 'logfile.txt'
# def most_frequent_user(file_path):
#     with open(file_path, "r") as file:
#         user_entries = [line.split(' - ')[2].split('"')[1] for line in file if "User" in line]
#         user_counts = Counter(user_entries)
#         most_common_user = user_counts.most_common(1)
#         return most_common_user

# most_common_user = most_frequent_user(file_path)
# print("Most frequent user:", most_common_user[0][0])

# print(Counter('abracadabra').most_common(1))


#Print the Unique User that accessed the web
# from collections import Counter
# file_path = 'logfile.txt'
# def most_frequent_user(file_path):
#     with open(file_path, "r") as file:
#         user_entries = [line.split(' - ')[2].split('"')[1] for line in file if "User" in line]
#         unique_users = set(user_entries)
#         return unique_users


# print("Unique user(s):", most_frequent_user(file_path))

# print(Counter('abracadabra').most_common(1))



# from datetime import datetime
# def extract_time_range(file_path):
#     with open(file_path, "r") as file:
#         timestamps = [line.split(' - ')[0] for line in file]
#         timestamps = [datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") for timestamp in timestamps]
#         min_time = min(timestamps)
#         max_time = max(timestamps)
#         return min_time, max_time
#         # return timestamps

# min_timestamp, max_timestamp = extract_time_range(file_path)
# print("Time range of log entries:", min_timestamp, "to", max_timestamp)
# print(extract_time_range(file_path))


#Find the timestamp of the first log entries
file_path = 'logfile.txt'
def first_log_entry(filepath):
    with open(file_path, 'r') as file:
        first = file.readline()
        return first.split(' - ')[0]

print(first_log_entry(file_path))


#Find the timestamp of the last log entries
file_path = 'logfile.txt'
def first_log_entry(filepath):
    with open(file_path, 'r') as file:
        last = file.readlines()
        return last[-1].split(' - ')[0]

print(first_log_entry(file_path))



#Calculate the average characters
def calculate_average_characters(file_path):
    with open(file_path, "r") as file:
        total_characters = sum(len(line) for line in file)
        total_entries = log_enteries_count(file_path)
        average_characters = round(total_characters / total_entries)
        return total_characters, average_characters, total_entries

total_characters, average_characters, total_entries = calculate_average_characters(file_path)
print("Average characters per log entry:", average_characters)
print("Total characters of log entry:", total_characters)
print("Total entries:", total_entries)



#Most common log message type.
from collections import Counter
file_path = 'logfile.txt'
def most_frequent_user(file_path):
    with open(file_path, "r") as file:
        log_messages = [line.split(' - ')[1] for line in file]
        log_status = Counter(log_messages)
        return log_status.most_common(1)

print("Most Common Log Message Type:", most_frequent_user(file_path)[0][0])



#Calculating the percentage of info message type
file_path = 'logfile.txt'
def info_type_percentage(file_path):
    with open(file_path, 'r') as info:
        info_type = [line for line in info if 'INFO' in line]
        len_info_type = len(info_type)
        total_entries = log_enteries_count(file_path)
        info_percentage = (len_info_type / total_entries) * 100
        return round(info_percentage, 2)
print("Percentage of Info Log Message Type:", info_type_percentage(file_path))

a = 15
b = 10
print("A") if a > b else print("=") if a == b else print("B")

#Removing Text files using python
# import os
# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
# else:
#     print('File doesnot exist. Check the name again!')


