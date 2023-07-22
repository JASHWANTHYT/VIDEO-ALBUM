import os 
import cv2

path= "Images/"

Images =[]

for file in os.listdir(path):
    name, extension = os .path.splitext(file)

    if extension in ['.gif','.png','.jpg','.jpeg,','.jfif']:
        file_name = path+"/"+file

        print(file_name)

        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])

height , width, channels = frame.shape

size = (width, height)

print(size)

video_name = "Project.avi"
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps= 0.8
out = cv2.VideoWriter(video_name, fourcc,fps,size)

for i in range(count):
    image = cv2.imread(Images[i])

    out.write(image)

out.release()
print("Completed")