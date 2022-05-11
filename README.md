# Auto TAMU class-enrollment tool

## Problem Statement:
This was created for fun while I was reloading the TAMU class enrollment page (https://cas.tamu.edu/cas/login?service=https://howdy.tamu.edu/uPortal/Login&renew=true) constantly at 1 AM and hoping to find a seat for CSCE 411 Section 504 (which I later Q-dropped anyways).

## Purpose: 
It automatically searches for an empty seat in a provided section from a class, and will refresh forever untill he/she is enrolled in that section.

## Implementation:
This porject simulates a user's behavior of constantly refreshing the page and putting the class and section number everytime it reloads. 
It utilizes the **Selenium** brower automation library for Python, which grabs the content such as number of seats left and section number by Xpath, given the username, password, class number and section number, with a while loop which will only stop when the class is enrolled.

## Impact:
This project makes class enrollment easier and faster, and I don't believe the software gives anyone an advantage. It's designed to catch an empty seat for a student in need whenever another student drops out of the class. Since the timing is unknown, a desperate student would reload the page constantly and wish for that empty seat. Because this tool only automates browser behaviors, requests are being sent in a human pace to the server, and thus creating no overwhelming traffic. Hopefully this projects inspires the school to make the enrollment process better for **underclassmen**, **transfer students** and **international students**, who historically have a hardtime figuring out the system and registering for a class they need to graduate in time.

## Note:
Only Chrome brower was tested. The latest chromedriver must be downloaded and put in the same folder as the code: https://chromedriver.chromium.org/, the one included the the repo has depreciated.
