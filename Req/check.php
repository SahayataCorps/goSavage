<!DOCTYPE html>
<html>
<head>
	<title>Checking</title>
	<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<?php $url =  $_GET['url'];
$command = escapeshellcmd(' ');
$output = exec("python find.py ".$url);
echo $output;
?>

<div>
	<?php
	if($output > 0) {?>
	<div class="container" style="padding-top: 100px;">
	<div class="alert alert-warning">
    <strong>Warning!</strong> This alert box could indicate a warning that might need attention.
  	</div>
	<a href="<?php echo $_GET['url']; ?>">Advance</a>
	</div>
	<?php } 
	else {?>
	<div class="container" style="padding-top: 100px;">
	<div class="alert alert-success">
    <strong>Success!</strong> This alert box could indicate a successful or positive action.
  	<a href="<?php echo $url; ?>">Advance</a>
  	</div>
    </div>
	<?php } ?>
</div>

</body>
</html>