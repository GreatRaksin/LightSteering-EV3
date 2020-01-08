## Steer with light. 

In this exercise, we'll use a bright flashlight to steer the robot, perhaps around an obstacle course.

But how can we indicate, with the brightness of the flashlight, which way we want the robot to turn?

One way would be to have the robot turn left when there is minimal light, go straight when there is medium light and turn right when the light is bright, because you're pointing the flashlight straight at the color sensor.

The sensor's <code>.ambient()</code> property (it measures the ambient light intensity) can have values 0 to 100, so if we want to use the full range of steering from **-100** to **+100** then we need to come up with a formula to convert the light intensity to that range.

How about **(ambientLightIntensity * 2)-100**? Put a light intensity value of **0** into that formula and it will give us **-100**, as wanted and putting a value of **100** in will give a result of **+100**, with is also correct.

We'll keep the speed set to a constant, say, **50**. 

The code can be:

<code>while True:</code><br>
    <code>Robot.drive(50, cl.ambient() * 2 -100)</code>

Fix the color sensor so that it's facing vertically upwards, grab your flashlight, then run the script.

You're probably going to be disappointed with the result, but at least you should be able to see that you can influence the motion of the robot with your flashlight. 

The problem is that the light intensity is only ever going to be zero if the room is rather dark, which is unlikely, and probably also the brightness detected when you shine your flashlight directly at the sensor will not be anywhere close to **100**, so we can't get the steering range of **-100** to **+100** that we were hoping for.

In the next exercise we'll modify the code to get better results.
This adaptation to real world conditions is part of what makes programming robots so interesting.

## Steer with calibrated light. 

The last script was really short and you probably had some trouble adjusting the formula to get good results, so let's do a bit more work on it.

It'll be nice to be able to calibrate the light intensity in some way, so that the robot knows what is the dimmest and brightest light that it should expect. I propose this calibration procedure:

1. The Robot tells us to press the Enter button when the color sensor is in dim light.
2. We press the Enter button as instructed. 
3. The robot records that dim light intensity in a variable called 'dim'.
4. The robot beeps and then instructs us to press the Enter button again when the color sensor is in the bright light of the flashlight.
5. We point the flashlight at the color sensor and press the button as instructed.
6. The robot records that bright light intensity in a variable called 'bright'.
7. The robot beeps, says '3, 2, 1, go!', and then begins its motion. 

What would that look like in code?
The trickiest part is the calculation of the steering value based on the values of 'dim', 'bright' and the light intensity.
This is not a math course, and I don't have time to explain this formula properly to you, but check this out.

<code>steer = (200 * (intensity - dim)/(bright - dim)) - 100</code>

Ask yourself what would happen if the sensor, as it trundles along, is exposed to light with an intensity equal to 'dim'.

If intensity = dim then we get:

<code>steer = (200 * (dim - dim) / (bright - dim)) - 100 = 200 * (0) / (bright-dim)) - 100 = 0 - 100 = -100</code>

Then, in the formula above, intensity - dim will equal 0, so we will have that steer now is **-100**, as we want.

If intensity = bright then we get:

<code>steer = (200 * (bright - dim) / (bright - dim)) - 100 = 200 * 1 - 100 = 200 - 100 = +100</code>

When the sensor gives an intensity value equal to 'bright', then the part of the formula (intensity-dim)/(bright-dim) becomes (bright-dim)/(bright-dim which is just 1.
The whole formula then gives **(200*1) - 100** which is **+100**, as we want. Recall that multiplication is done before subtraction unless parentheses indicate otherwise.

That's not a proper mathematical justification of the formula, but it's all we need for right now.

At least it should convince you that the formula should work... or should it? What if we fix the bright value with a flashlight 40 centimeters from the sensor and then, while the robot is moving, we bring the flashlight 30 cm from the sensor. Then the intensity will exceed the bright value we recorded and that clever formula we looked at will give a value greater than **100**, which will generate an error if we try to use it as a steering value for the motor command.

You have to make sure that the motor command is never fed a steering value less than **-100** or greater than **+100**, and we can do that with the functions <code>max()</code> and <code>min()</code> which are standard built-in functions in Python. 
The function <code>max()</code> returns the largest value among the supplied arguments and the function <code>min()</code> gives the smallest value so we can make sure that the steering values 'steer' never exceeds **100** with <code>min(steer, 100)</code>, and we can make sure that steer is never less than -100 with <code>max(steer,-100)</code>.
Combining these into one line of code, we get <code>steer = min(max(steer, -100), 100)</code>

In file main.py you can find source code. Try it! That should work well enough, and it's kind of fun to be able to control the motion of the robot like this.

By all means set up a little obstacle course if you want to test your skills in controlling the robot in this novel way.
That <code>min(max())</code> function in 35 line is rather neat and our code is starting to get a bit long and complex: two good reasons to consider making a user-defined function.

Making a user-defined function has multiple advantages:
- The code can be easily recycled in other scripts.
- It allows us to make the structure of the main part of the program simpler and easier to understand, with fewer distractions. 

Let's see how that function could be made into a user-defined function called. Open file user-defined.py and try to run it on tour robot.



