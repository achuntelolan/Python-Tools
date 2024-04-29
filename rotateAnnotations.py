'''
 This tool efficiently converts your existing annotation file to account for image rotations. 
It reads annotations saved in a single file with the format "file_name x_min,y_min,x_max,y_max,class". 
You can choose to rotate annotations clockwise or counterclockwise by 90 degrees, 
which is particularly useful when you've rotated your images after generating annotations.
you can coustomise this code based on your requirments 
Written by  ANOOP JOSEPH JOHN'''

import cv2

def process_annotation(annotation_line):
    parts = annotation_line.split()
    image_path = parts[0]
    coordinates = parts[1:]
    img = cv2.imread(image_path) 
    img_height , img_width , layers = img.shape

    rotate_clockwise = True # enable it TRUE or FALSE Based on which angle you want to rotate annotations this for 90 degree
    rotate_antiClockwise = True # enable it TRUE or FALSE Based on which angle you want to rotate annotations this for - 90 degree

    if rotate_clockwise:
        new_coordinates = []
        for coord in coordinates:
            x_min, y_min, x_max, y_max, class_label = map(int, coord.split(','))
            x_min, y_min, x_max, y_max = y_min,x_min, y_max, x_max
            new_x_min, new_y_min, new_x_max, new_y_max = (img_width - x_max),y_min, (img_width - x_min), y_max
            class_label = 0
            new_coord = f"{new_x_min},{new_y_min},{new_x_max},{new_y_max},{class_label}"
            new_coordinates.append(new_coord)
        return f"{image_path} {' '.join(new_coordinates)}"
    elif rotate_antiClockwise :
        new_coordinates = []
        for coord in coordinates:
            x_min, y_min, x_max, y_max, class_label = map(int, coord.split(','))
            x_min, y_min, x_max, y_max = y_min, x_min, y_max, x_max
            new_x_min, new_y_min, new_x_max, new_y_max = x_min,(img_height - y_max), x_max, (img_height - y_min)
            class_label = 0
            new_coord = f"{new_x_min},{new_y_min},{new_x_max},{new_y_max},{class_label}"
            new_coordinates.append(new_coord)
        return f"{image_path} {' '.join(new_coordinates)}"
    else:
        new_coordinates = []
        for coord in coordinates:
            x_min, y_min, x_max, y_max, class_label = map(int, coord.split(','))
            new_x_min, new_y_min, new_x_max, new_y_max = x_min, y_min, x_max, y_max
            class_label = 0
            new_coord = f"{new_x_min},{new_y_min},{new_x_max},{new_y_max},{class_label}"
            new_coordinates.append(new_coord)
        return f"{image_path} {' '.join(new_coordinates)}"

def process_annotation_file(annotation_file, output_file):
    with open(annotation_file, 'r') as f:
        with open(output_file, 'w') as out_f:
            for line in f:
                updated_line = process_annotation(line.strip())
                out_f.write(updated_line+'\n')

if __name__ == "__main__":
    annotation_file = "annotations.txt" # Update with your current annotation path
    output_file = "updated_annotations.txt" # Update with your newly generating annotation file name 
    process_annotation_file(annotation_file, output_file)
