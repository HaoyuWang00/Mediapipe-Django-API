# Mediapipe and Django
This project will mainly use Mediapipe and Django. In the following part we will include the setup/installation for the requirements, explain how the core part of the code works and some bugs left to deal with.

Note that this project can be run under both Windows OS and Ubuntu 20.04. Both versions have similar code, but the setup and performance (can-dos and cannot-dos) are slightly different.

## Mediapipe
1. Installation: <B>Ubuntu/Windows</B>  https://google.github.io/mediapipe/getting_started/install.html. One thing to note that for <B>Windows</B>, one will have to use the specified <B>OpenCV 3.4.10</B>, while for <B>Ubuntu</B> one can just use the newest version for it.

2. Python Solution Installation: This is the solution that we currently use for the running API. For both OS, go to https://google.github.io/mediapipe/getting_started/python.html and do the installation with ```pip``` accordingly. One can do this in a ```python virtual environment``` or not, this is optional.

3. Python ready-to-use Solution: https://google.github.io/mediapipe/solutions/hands.html shows an example script of the calling the hand detector. This will be used as part of the API at ```../script/hand_video_detector.py```.

4. C++ example: https://google.github.io/mediapipe/getting_started/cpp.html shows the example for buliding the target for detection with C++ and other stuff. This part shall be able to run once we have done part 1, the main installation.
<br/>However, I personally have done the ```hello world example``` but fails at the ```hand detection example```. Here are the links to the related issues when buliding the example C++targets under both <B>Windows OS and Ubuntu 20.04</B>.
<br/><B>Windows:</B> https://github.com/google/mediapipe/issues/2172
<br/><B>Ubuntu 20.04:</B> https://github.com/google/mediapipe/issues/2001#issuecomment-864755332
<br/>Developers can refer to the issues and specifications.

5. Further work: For this project, one can use ```Graph``` and ```Calculators``` of Mediapipe to add more features like hand gestures detection. For more information, one can refer to: https://gist.github.com/TheJLifeX/74958cc59db477a91837244ff598ef4a

## Django
1. Installation: Do installation following https://docs.djangoproject.com/en/3.2/intro/install/.

2. If the developer has no experience with Django, he/she is strongly encouraged to take the tutorial before looking into this project, from: https://docs.djangoproject.com/en/3.2/intro/tutorial01/

3. Once this is done, one can look into the Django code with implements ```Mediapipe``` and ```cv2```.

4. Quick Review: (for the html pages) under ```template```, ```home.html``` is the home page. ```image_upload``` and ```video_input``` are two other pages written in html format and are triggered by some buttons. These all are based on the ```base``` one.