# import os
# os.chdir("Photos")
# originals = os.listdir()

# def extract_place(originals):
#     places = []
#     for i in originals:
#         first = i.find("_")
#         partial = i[first+1:]
#         second = partial.find("_")
#         final = partial[:second]
#         places.append(final)
#     return places

# print(extract_place(originals))

# def make_place_directories(places): # Here's the function definition
#     for place in places:
#         os.mkdir(place)

# #Method 2
# places = []
# def extract_place(string):
#     if string not in places:
#         places.append(string.split("_")[1])

# for i in originals:
#     extract_place(i)
    
# print(places)

#Method 3
# def extract_place(string):
#     for i in string:
#         places.append(i.split("_")[1])
#     return places
  
# print(extract_place(originals))







#Correct Form
import os

def extract_place(filename):
    return filename.split('_')[1]

def make_place_directories(places): # Here's the function definition
    for place in places:
        os.mkdir(place)

os.chdir("Photos")
originals = os.listdir()
places = []
for filename in originals:
    place = extract_place(filename)
    if place not in places:
        places.append(place)

make_place_directories(places) # Don't forget to call the function!


for filename in originals:
    place = extract_place(filename)
    os.rename(filename, os.path.join(place, filename))

print(os.listdir()) # This is just a temporary line for testing!
print(places)