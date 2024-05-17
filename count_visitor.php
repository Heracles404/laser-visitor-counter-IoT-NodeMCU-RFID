<?php
// Database configuration
$servername = "localhost";
$username = "root"; // Your database username
$password = ""; // Your database password
$dbname = "visitor"; // Database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if we need to insert a new visitor
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $visitor_id = $_POST['visitor_id']; // Get visitor ID from POST request
    $date = date("Y-m-d"); // Current date
    $time = date("H:i:s"); // Current time

    // SQL query to insert a new visitor with date and time
    $sql = "INSERT INTO counter (visitor_ID, date, time) VALUES ('$visitor_id', '$date', '$time')";

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
} else {
    // SQL query to select the latest visitor ID
    $sql = "SELECT visitor_ID, date, time FROM counter ORDER BY visitor_ID DESC LIMIT 1"; 

    $result = $conn->query($sql);

    $visitor_data = array("visitor_id" => "", "date" => "", "time" => "");
    if ($result->num_rows > 0) {
        // Output data of the latest row
        $row = $result->fetch_assoc();
        $visitor_data["visitor_id"] = $row["visitor_ID"];
        $visitor_data["date"] = $row["date"];
        $visitor_data["time"] = $row["time"];
    } else {
        echo "0 results";
    }

    // Return data in JSON format
    echo json_encode($visitor_data);
}

$conn->close();
?>