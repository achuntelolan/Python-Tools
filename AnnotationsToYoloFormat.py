''' This Python script efficiently converts a single file containing annotations
 in the format "image_path,x_min,y_min,x_max,y_max,class" 
into both YOLO format and individual Induvigel files for each corresponding image.\
written by ANOOP JOSEPH JOHN
'''
import os
import cv2

ann_path = "annotations.txt" # update with path of your annotation file
img_path = "OTHER/" #update with your image folder path
dest = 'output/' #update with path for output folder
file_count = 0
success_count = 0
failure_count = 0

with open(ann_path, 'r') as f:
    data = f.readlines()
    total_files = len(data)
    for line in data:
        file_name = line.split(" ")[0]
        file_name = file_name.split('/')[-1]
        img = cv2.imread(img_path + file_name)
        img_height, img_width, layers = img.shape

        labels = line.strip().split(' ')[1:]
        out_file = os.path.join(dest, f"{file_name.split('.')[0]}.txt")
        with open(out_file, "w") as f2:
            file_count += 1
            for k in labels:
                k_split = k.split(",")
                width = int(k_split[2]) - int(k_split[0])
                height = int(k_split[3]) - int(k_split[1])
                xc = str((int(k_split[0]) + (width / 2)) / img_width)
                yc = str((int(k_split[1]) + (height / 2)) / img_height)
                width = str(width / img_width)
                height = str(height / img_height)
                category = str(k_split[4])

                f2.write(str(category + ' ' + xc + ' ' + yc + ' ' + width + ' ' + height + '\n'))

            success_count += 1
            print(f"\rProcessed {file_count}/{total_files}", end="")

        f2.close()

print("\nConversion finished.")
print("Successful conversions:", success_count)
print("Failed conversions:", total_files - success_count)
