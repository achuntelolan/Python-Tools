
'''the following code will convert normalized yolo annotations into absolute coordinates and plot the annotations
in corresponing images and save the output '''

import os
import cv2

img_folder = 'input/images' # replace with your  image folder path
anno_folder = 'input/annotations' # replace with your annotations file folder path
out_folder = 'output/annotations' # replace with your output path

for anno_file in os.listdir(anno_folder):
    img_name = os.path.splitext(anno_file)[0]
    img_path = os.path.join(img_folder, img_name)
    anno_path = os.path.join(anno_folder, anno_file)
    jpg_image_path = os.path.join(img_folder, img_name + '.jpg')
    png_image_path = os.path.join(img_folder, img_name + '.png')

    if os.path.exists(jpg_image_path):
        image_path = jpg_image_path
    elif os.path.exists(png_image_path):
        image_path = png_image_path

    if os.path.exists(image_path):
        image = cv2.imread(image_path)
        file = open(anno_path, 'r')
        anno_data = file.readlines()
        img_height , img_width , layers = image.shape
        for anno in anno_data:
            parts = anno.strip().split()
            label = int(parts[0])
            xc, yc, width, height = map(float, parts[1:])
            
            # Convert normalized coordinates back to absolute coordinates
            x1 = int((xc - width / 2) * img_width)
            y1 = int((yc - height / 2) * img_height)
            x2 = int((xc + width / 2) * img_width)
            y2 = int((yc + height / 2) * img_height)

           #  Edit the following code with if function in case if you want different colours for differnet classes 
            
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, 'Filled', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)


        out_path = os.path.join(out_folder, img_name + "_annotated.jpg")
        cv2.imwrite(out_path, image)
    else:
        print(f"Image not found for annotation file: {anno_file}")
