'''
 This python script converts a single file containing annotations 
in the format "image_path,x_min,y_min,x_max,y_max,class" 
into individual Induvigel files for each corresponding image. 
written by ANOOP JOSEPH JOHN '''


import os

def create_annotation_files(annotations_file,output_path):
    # Create the output folder if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    with open(annotations_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # Split the line by whitespace
            parts = line.strip().split()
            if len(parts) > 1:
                image_path = parts[0] 
                file_name=image_path.split('/')[-1] # First part is the image path spliting and taking only image name 
                annotations = ' '.join(parts[1:])  # Remaining parts are annotations
                print(annotations)
                # Extract the image filename without extension
                image_filename = os.path.splitext(os.path.basename(file_name))[0]
                print(image_filename)

                # Create the path for the annotation file in the output folder
                annotation_filename = os.path.join(output_path, f"{image_filename}.txt")

                # Write the annotations to the annotation file
                with open(annotation_filename, 'w') as out_f:
                    out_f.write(annotations)
            else:
                # If no annotations, create an empty annotation file
                image_filename = os.path.splitext(os.path.basename(parts[0]))[0]
                print(image_filename)
                annotation_filename = os.path.join(output_path, f"{image_filename}.txt")
                open(annotation_filename, 'a').close()

if __name__ == "__main__":
    annotations_file = "updated_annotations.txt"
    output_path = "output"
    create_annotation_files(annotations_file,output_path)
