from diagrams import Diagram
from diagrams.programming.language import Python

with Diagram("Face Blurring ML System", show=True, direction="LR"):
    
    video = Python("Video Input\n(MP4 file)")
    
    splitter = Python("Frame Splitter\n(ffmpeg)")
    
    workers = [
        Python("Worker 1\nFace Detection + Blur"),
        Python("Worker 2\nFace Detection + Blur"),
        Python("Worker 3\nFace Detection + Blur"),
    ]
    
    output = Python("Video Output\n(Blurred MP4)")
    
    # Стрелки
    video >> splitter
    
    for w in workers:
        splitter >> w
    
    workers >> output