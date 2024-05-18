<?php
// Database connection
$DB_HOST = "localhost";
$DB_USER = "root"; 
$DB_PASS = ""; 
$DB_NAME = "visitor";

// Create connection
$conn = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get vID from GET parameters
if (isset($_GET['vID'])) {
    $vID = $_GET['vID'];
} else {
    die("vID parameter is missing");
}

// Insert data
$time = date("H:i:s"); // Current time
$date = date("Y-m-d"); // Current date

$sql = $conn->prepare("INSERT INTO counter (visitor_ID, time, date) VALUES (?, ?, ?)");
$sql->bind_param("sss", $vID, $time, $date);

if ($sql->execute() === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql->error;
}

// Close connection
$sql->close();
$conn->close();
?>
