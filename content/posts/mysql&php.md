title: Retrieving information from a MySQL database using php
date: 2016-04-05
image: phpsql.jpg

PHP is a server-side scripting language that is used to make web pages dynamic and interactive. As opposed to a raw html page, PHP allows your users to post and retrieve information to and from a database. If you use PHP with a database, your users can create content that will remain there for later viewing.

In this guide, I will walk you through how to use PHP to connect and manipulate a database. For the sake of brevity, we will only be retrieving the contents of our database. This guide assumes three things:
* Basic knowledge of HTM
* Basic knowledge SQL
* Access to an online database (either through a hosting provider such as Fatcow, or through an online text editor such as cloud 9)

Throughout this guide, I will be giving general steps that I will demonstrate through specific examples. You may either follow along using my examples, or apply the steps to your own setup.

### Step 1: Create a database

This step largely depends on the database provider you are using. If you are using a hosting provider (I am using Fatcow), you can navigate to your control panel and find the option for creating a new database. You want to name your database appropriately so that you can find it later, and give it a strong password so that others cannot access it.

### Step 2: Create and populate your desired tables
I am using phpmyadmin so I have the option of either doing this using the GUI (clicking and typing) options, or using SQL queries. I’m lazy so I’m going to use the GUI. I created a users table with three attributes: ‘username’, ‘password’, and ‘email’.

### Step 3: Create your PHP file.
I will name my file index.php. You may also use an html page and add the markings ‘’ around any PHP code you are adding.

### Step 4: Connect to the database
Inside your file, enter the following code. Be sure to get the information in asterisks from your hosting provider. (Of course I’m not going to show you my own credentials)

    <!--?php $link = mysqli_connect('*database_url*', '*username*', '*password*’, '*database_name*');

      if (!$link) {
      die('Could not connect: ' . mysql_error());
      }

      echo 'Connected successfully';

    ?-->

If the page is able to connect to your database, it should say “Connected successfully”. If it instead prints out “Could not connect,” you should double check the credentials you have provided to your database.

### Step 5: Retrieve records from your database
Underneath all the code we have written thus far, paste/write the following:

    <table >
      <thead>
        <tr>
            <th>Username</th>
            <th>Email</th>
            <th >Password</th>
        </tr>
      </thead>

      <tbody>
      <?php
       $query = "SELECT * FROM users";

          if( $result= mysqli_query($link, $query)) {

              while ($row = mysqli_fetch_array($result)) {
               echo '<tr>';
                  echo '<td>' . $row[username] .  '</td>';
                  echo '<td>' . $row[email] . '</td>';
                  echo '<td>' . $row[password] . '</td>';
                echo '</tr>';
             }


          } else {

              echo "it failed";

          }
      ?>

      </tbody>
    </table>

What I have done here is created a simple html table which I populated using the values of my users table. I used the query ‘SELECT * FROM users’ to pull all the records from the users table. We are then looping through the columns in each record and adding them to a row in our html table.
You may adjust this sample code as need be to fit the format of your tables.

