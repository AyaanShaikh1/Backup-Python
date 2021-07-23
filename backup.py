import os
import shutil

# path
path = 'C:/Users/Imtiyaz shaikh/Desktop'

print("Before Moving File: ")
print(os.listdir(path))

# source
source = 'C:/Users/Imtiyaz shaikh/Desktop/Project/68'

# destination
destination = 'C:/Users/Imtiyaz shaikh/Desktop'

# move content from source to destination example: Mumbai to Goa
dest = shutil.move(source,destination)

print(dest)

print("After Moving File: ")
print(os.listdir(path))
