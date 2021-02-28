# Problem solving
Write a program that solves the most suitable (with most power) link station for a device at given
point [x,y].
# Project
Please make this project as complete as you think it should be to be maintainable in the long
term by more than one maintainer. Provide instructions how to run the solution or if applicable
how to access a deployed running version.
This problem can be solved in 2-dimensional space. Link stations have reach and power.
A link station’s power can be calculated:
```
power = (reach - device's distance from linkstation)^2
if distance > reach, power = 0
```
Program should output following line:
```
“Best link station for point x,y is x,y with power z”
or:
“No link station within reach for point x,y”
```
Link stations​ are located at points (x, y) and have reach (r) ([x, y, r]):
```
[[0, 0, 10],
[20, 20, 5],
[10, 0, 12]]
```
Print out function output from points​ (x, y):
```
(0,0), (100, 100), (15,10) and (18, 18).

```


# My journey to the solution

I have found this problem rather challening but getting the solution right felt very rewarding. 
Most diffucult part was getting started. I took me a while to understand the logic completely. I had to break the problem down into to smaller sub problems and tackle them one by one.
First, I wanted to make sure that my results would be correct, so I manually worked out the math calculations, which I would later on use to compare my programs' results.  

Then, I decided on working out the distance between link stations and the device. For that I decided to build a function which uses the formuler specifiied in the question which returned the result. 

Then I moved onto calculating the most suitable link station (with most power). This is where I spent most of my time as at first I struggled with getting the correct results. Not only that, the program was returning results for all stations, instead of 4 best ones. 
![Screenshot 2021-02-28 at 14 03 35](https://user-images.githubusercontent.com/79025366/109417851-02ac4400-79ce-11eb-831d-745141c30baa.png)

Once I got past the problem of getting the result for the best 4 stations, with the use of for loops which would assign the best station for the given device to new variables best_station, I was still not happy with the numbers I was getting. 
I couldnt see how the second device located at point (100, 100) was getting any power when the problem specifies that if distance > reach then power is 0. 

Then I finally realised my mistake on line 44 which read: 
```
if distance > station_reach or power == 0:

```
and changed it to:
```
if distance <= station_reach:
````
Which yielded the correct result which matched my caluculations. 

# Conclusion

In conclusion I found this be diffuclt but definitely enojoyable (once I got the correct result anyway). I felt a sense of accoplishment for my hard work and dedication to see the assignment till the successful end. 

Thanks
Rad
