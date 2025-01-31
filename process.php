<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculation Results</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 50px;
        }
        .result {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #f9f9f9;
        }
        h2 {
            color: #333;
        }
        p {
            margin: 10px 0;
        }
        strong {
            color: #4CAF50;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <div class="result">
        <?php
        // Retrieve user input from the form
        $a = $_POST['a'];
        $b = $_POST['b'];
        $c = $_POST['c'];

        // Call the Python script with the input values
        $command = escapeshellcmd("python3 /var/www/html/calculate.py $a $b $c");
        $output = shell_exec($command);

        // Display the results or error messages
        echo $output;
        ?>
    </div>
</body>
</html>