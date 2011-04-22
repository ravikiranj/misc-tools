<?php
    function getResultFromYQL($yql_query) {
        $session = curl_init($yql_query);
        curl_setopt($session, CURLOPT_RETURNTRANSFER, true);

        $json = curl_exec($session);
        curl_close($session);

        return json_decode($json, true);
    }

    if(!empty($_GET['ip'])){
        $ip = $_GET['ip']; 
        $key = '7fc7e88c3b4c0e83127bce07a721043839574567756c1a0b85a4518ce1fa8fbf';
        $yql_base_url = "http://query.yahooapis.com/v1/public/yql";
        $yql_query = "select * from ip.location where ip='{$ip}' and key='{$key}'"; 
        $yql_query_url = $yql_base_url . "?q=" . urlencode($yql_query) . "&format=json&env=store://datatables.org/alltableswithkeys";
        
        echo "<pre>"; var_dump(getResultFromYQL($yql_query_url));echo "</pre>";

        
    }else {
        $html = <<<MARKUP
<html>
<head><title>IP Locator</title></head>
<body>
    <form method="GET">
        <p>Enter IP Address: <input type="text" id="ip" name="ip" /></p>
        <p><input type="submit" value="Submit" />
    </form>
</body>
</html>
MARKUP;
        echo $html;
    }
?>
