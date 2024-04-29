import os
import cv2

logo = ''' 

 ___      ___ ___  ________  _______   ________      ________  ___    ___ 
|\  \    /  /|\  \|\   ___ \|\  ___ \ |\   __  \    |\   __  \|\  \  /  /|
\ \  \  /  / | \  \ \  \_|\ \ \   __/|\ \  \|\  \   \ \  \|\  \ \  \/  / /
 \ \  \/  / / \ \  \ \  \ \\ \ \  \_|/_\ \  \\\  \   \ \   ____\ \    / / 
  \ \    / /   \ \  \ \  \_\\ \ \  \_|\ \ \  \\\  \ __\ \  \___|\/  /  /  
   \ \__/ /     \ \__\ \_______\ \_______\ \_______\\__\ \__\ __/  / /    
    \|__|/       \|__|\|_______|\|_______|\|_______\|__|\|__||\___/ /     
                                                             \|___|/      
                                                                          
                                                                          
'''
def checkInput(input):
    if input.strip() == "":
        input = None
        return input
    else:
        return int(input)

def trim_video(input_file, output_file, start_time=None, end_time=None, duration=None):
    cap = cv2.VideoCapture(input_file)
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    start_frame = 0 if start_time is None else int(start_time * fps)
    end_frame = total_frames if end_time is None else int(end_time * fps)
    
    if duration is not None:
        end_frame = start_frame + int(duration * fps)
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, fps, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                                     int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    
    while cap.isOpened() and cap.get(cv2.CAP_PROP_POS_FRAMES) <= end_frame:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def rotate_video(input_video, output_video, angle):
    cap = cv2.VideoCapture(input_video)
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID') 
    out = cv2.VideoWriter(output_video, fourcc, fps, (height, width))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if angle == 90:
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        elif angle == -90:
            frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        else :
            print("wrong angle you given ")
            break
            
        out.write(frame)
    
    cap.release()
    out.release()
    

if __name__ == "__main__":
    t_out = 't3.avi'
    duration = None
    is_trim = False
    is_rotate = False
    print(logo)
    print("curently we support only avi format")
    Trim = input("Do you want trim the video ? (y/n) : ")
    rotate = input("Do you want rotate your video ? (y/n) : ")
    input_file = input("Enter our video full path : ")
    r_out = input("Enter the output full path you want to save with file name : ")
    if Trim == "y" or Trim == "Y":
        print("Enter the times in seconds")
        start_time = input("From where you want start trim(leave it empty if you want to start from begining ) : ")
        end_time = input("Upto where you want to trim(leave it empty if you want to trim for end of video or upto a perticular duration): ")
        start_time = checkInput(start_time)
        end_time = checkInput(end_time)
        if end_time == None:
            duration = int(input("Enter Upto how much seconds you want to trim: "))
        is_trim = True
    if rotate == "y" or rotate == "Y":
        angle = input("Enter the angle to rotate 90 degree for CLOCKWISE or -90 degree for COUNTERCLOCKWISE rotation : ")
        angle = checkInput(angle)
        is_rotate = True
    
    if is_trim and not is_rotate :
        trim_video(input_file, r_out,start_time, end_time,duration)
        print(f"your Video is Success Fully Trimed and Saved as {r_out}")
    elif is_rotate and not is_trim :
        rotate_video(input_file, r_out, angle)
        print(f"your Video is Success Fully Rotated and Saved as {r_out}")
    elif is_trim and is_rotate :
        trim_video(input_file, t_out,start_time, end_time,duration)
        rotate_video(t_out, r_out, angle)
        os.remove(t_out)
        print(f"your Video is Success Fully Trimmed, Rotated and Saved as {r_out} ")
    else : 
        print("Please check your value or select atleast one option")