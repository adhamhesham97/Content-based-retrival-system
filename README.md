# Content-based-retrival-system
Using multimedia techniques to analyze, design, and implement content-based multimedia retrieval system, where the two media that we are going to use are the images and the videos.  
**We are using 3 techniques:**
 * **Average RGB:** taking the average for each color pixels in every image.
 * **Histogram:** acts as a counter for each individual color in every image
 * **Several Histogram:** which is slicing the image into certain number of divisions and comparing these slices by their histograms using (compareHist) function.

## Detailed analysis   
Frames are extracted from videos using the “KeyFramesExtraction” where frames are treated just like images.  
**In the main/source code,** functions that have been written were:  
 * **KeyFramesExtraction:** as mentioned earlier, this function basically takes a video and extracts its frames by putting them in an array of frames called “KeyFrames” and returns that array.
 * **Keyframesfeatures:** this function extracts features from the frames retrieved from a video, where it takes the “KeyFrames” array and loops over it extracting the histograms and average RGB. It returns the variables: avgRGB, Histograms, layoutHistogram (an array of the several histograms of each frame).
 * **sliceImage:** it takes two attributes (an image and the desired factor of division). What this function does is that it divides the image into slices of size smaller than the given image by dividing the image’s width and height by the square root of the given factor. It then loops over the total number of divisions (vertically then horizontally), creates image slices with the new acquired dimensions and store these slices in an array that is later returned by the function.
 * **CompareHist:** it takes two histograms, divides the minimum histogram by the second one and returns the value in an attribute called “intersection”.
 * **RGB_mean:** it takes an image and returns the average value for each channel of that image.
 * **Compare_avg_RGB:** it takes two avg RGB values and compares values of the same channel by the other value of the same channel.
 * **Histogram:** it takes an image, returns the three histograms of that image red, green and blue histograms.
 * **SeveralHistograms:** it takes an image and number of divisions, slices the given image into the required number of slices/divisions then loops over these slices extracting the three histograms of each slice and storing them in an array called histogram.
 * **Compare_SeveralHistograms:** takes two histograms, compares them and returns the average number of similar histograms.
 * **Similarity_Video:** checks if the keyFrames have similar features.

## Requirements:
 * python 3.8.5
 * imageio-ffmpeg
 

## User Guide:
<div align="center"> 
   <br />
   <img src="https://user-images.githubusercontent.com/64116564/121778896-64697600-cb99-11eb-96e6-9a345131b467.jpeg" />  
</div> 

 * First the user chooses **the type of multimedia** that is going to be used from the combo box in the top left corner whether it is an Image or a Video, then chooses **the retrieval method (Average RGB, Histogram, or Several Histograms)** from the other combo box on the top right corner. 
 * After choosing both the multimedia type and the retrieval method, the user presses the **Browse Files** button and **chooses a video/image to be retrieved.** 
 * Finally, before submitting the user must press the Build DB button where two folders/sections (one for images and the other for videos) appear in the blank area below. These sections are initially empty until the Submit button is pressed. 
 * An Exit button was created for the user to clear everything and close the program.

## Testing Scenario
* Retrieve an image from the database **using average RGB method.**  
<div align="center"> 
   <br />
   <img src="https://user-images.githubusercontent.com/64116564/121778142-eeafdb00-cb95-11eb-8b9c-5b523dfaf389.png" />  
</div> 
  
* Retrieve an image from the database **using histogram method.**
<div align="center"> 
   <br />
   <img src="https://user-images.githubusercontent.com/64116564/121778181-19019880-cb96-11eb-8df5-0a949c040c5a.png" />  
</div> 
  
* Retrieve an image from the database **using Several Histograms method.** 
<div align="center"> 
   <br />
   <img src="https://user-images.githubusercontent.com/64116564/121778286-91685980-cb96-11eb-941e-e7d737b06354.png" />  
</div> 

* Retrieve a video from the database **using average RGB method.**  
<div align="center"> 
   <br />
   <img src="https://user-images.githubusercontent.com/64116564/121778579-c923d100-cb97-11eb-8b73-b9560f2bac5c.gif" />  
</div> 



## Team Members:
  * Adham Hesham Hamed 
  * Aya Tarek El-Ashry
  * Yara Mohamed Hussien Zaki 
  * Reem Mohamed Abd El-Raaouf Mady
  * Amr Yasser Mahmoud El-Gamal
  * Ahmed Abd El-Salam Helaly
