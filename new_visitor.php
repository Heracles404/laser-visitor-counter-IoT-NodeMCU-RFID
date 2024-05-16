<?php
// Database connection
$DB_HOST = "localhost";
$DB_USER = "root"; 
$DB_PASS = ""; 
$DB_NAME = "visitor";

$conn = mysqli_connect($DB_HOST,$DB_USER,$DB_PASS,$DB_NAME);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Insert data
// You can modify this to get the actual visitor ID
$time = date("H:i:s"); // Current time
$date = date("Y-F-d"); // Current date

$sql = "INSERT INTO counter (time, date) VALUES ('$time', '$date')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
