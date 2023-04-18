<!DOCTYPE html>
<html>
<head>
	<title>PHP Pagina met database records</title>
</head>
<body>
    <h1>PHP Pagina met database records</h1>
    <?php
        // Verbinding maken met de database
    $servername = "192.168.1.199";
    $username = "webserver";
    $password = "wachtwoord";
    $dbname = "voorbeelddatabase";

    $conn = mysqli_connect($servername, $username, $password, $dbname);
    $hostname = gethostname();
    echo "De hostname van deze server is: " . $hostname . "<br>";
    // Controleer of de verbinding is gelukt
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    // Voer een SQL-query uit
    $sql = "SELECT * FROM tabel1";
    $result = mysqli_query($conn, $sql);

    // Verwerk de resultaten
    if (mysqli_num_rows($result) > 0) {
        while($row = mysqli_fetch_assoc($result)) {
            echo "ID: " . $row["id"]. " - Naam: " . $row["naam"]. " - Leeftijd: " . $row["leeftijd"]. "<br>";
        }
    } else {
        echo "Geen resultaten gevonden.";
    }

    // Sluit de verbinding met de database
    mysqli_close($conn);
    ?>
</body>
</html>