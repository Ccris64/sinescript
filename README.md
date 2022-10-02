# Sinescript - Make music with plain text files

Library credits:
lib used: pysine
repo: https://www.github.com/lneuhaus/pysine

## Usage

### First step:
Make a file with any name and any extension (I normally use **.sines**).

![readme_image1](https://user-images.githubusercontent.com/93295652/193435426-b94358ba-f35c-4b03-a2de-74bad4212ce9.PNG)
### How to write a valid Sinescript file:
Write frequencies in the following format:
```
Frequency Duration
```
**Example:**
```
800 1
```
800 is for 800hz, and 1 is for 1 seconds. Floating numbers for duration are also supported, such as 0.1.
To add a break, just do this:
```0 1```

0 is for 0hz (no sound). 1 is for 1 second. A 1 second break.
See the example picture:
![readme_image2](https://user-images.githubusercontent.com/93295652/193435537-d35c92b8-0413-4f5a-b304-9608a011071a.PNG)
