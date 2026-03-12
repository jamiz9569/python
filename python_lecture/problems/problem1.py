
# question no. 1
print ('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.
''')


#question no. 2
import math
print ("5*1 =", 5*1)
print ("5*2 =", 5*2)
print ("5*3 =", 5*3)
print ("5*4 =", 5*4)
print ("5*5 =", 5*5)
print ("5*6 =", 5*6)
print ("5*7 =", 5*7)
print ("5*8 =", 5*8)
print ("5*9 =", 5*9)
print ("5*10 =", 5*10)


#question no. 3
import pyttsx3
engine = pyttsx3.init()
engine.say("jamiz qamar , how are you ?")
engine.runAndWait()


#question no. 4
import os

# Specify the directory you want to list
directory = "D:\\python\\python_lecture"  # Change this to your desired path

# Get the list of all files and directories
contents = os.listdir(directory)

# Print each item
print(f"Contents of '{directory}':")
for item in contents:
    print(item)


