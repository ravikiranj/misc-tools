<?php
    function getResultFromYQL($yql_query) {
        $session = curl_init($yql_query);
        curl_setopt($session, CURLOPT_RETURNTRANSFER, true);

        $json = curl_exec($session);
        curl_close($session);

        return json_decode($json, true);
    }
    function getLocation($self = false){
        if($self){
            $ip = $_SERVER['REMOTE_ADDR'];
        }else{
            $ip = $_GET['ip'];
        }
        $key = '7fc7e88c3b4c0e83127bce07a721043839574567756c1a0b85a4518ce1fa8fbf';
        $yql_base_url = "http://query.yahooapis.com/v1/public/yql";
        $yql_query = "select * from ip.location where ip='{$ip}' and key='{$key}'"; 
        $yql_query_url = $yql_base_url . "?q=" . urlencode($yql_query) . "&format=json&env=store://datatables.org/alltableswithkeys";
        $locResult = getResultFromYQL($yql_query_url);
        $markup = 'Failed to convert IP to Location, please try again';
        if(isset($locResult['query']) && isset($locResult['query']['results']) && !empty($locResult['query']['results']['Response'])){
            $resp = $locResult['query']['results']['Response'];
            $markup = '';
            if($self){
                $markup .= "<h2>Your IP Address = {$_SERVER['REMOTE_ADDR']}</h2>"; 
            }else {
                $markup .= "<h2>Entered IP Address = {$_GET['ip']}</h2>"; 
            }
            $markup .= '<table id="resultarea" border="1" cellpadding="20" align="center">';
            foreach($resp as $key => $value){
                if(empty($value)){
                    $value = "-";
                }
                $markup .= <<<MARKUP
<tr><td>$key</td><td>{$value}</td></tr>
MARKUP;
            }
            $markup .= '</table>';
        }
        if($self){
            return $markup;
        }else {
            echo $markup;
        }
    }
    if(!empty($_GET['ip'])){
        getLocation(); 
    }else {
        $result = getLocation(true);
        $html = <<<MARKUP
<html>
<head><title>IP Locator</title>
<link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/combo?2.9.0/build/reset-fonts-grids/reset-fonts-grids.css"> 
<style type="text/css">
#bd{
    margin-top: 25px;
    border: 1px solid #C0C0C0;
    border-radius: 8px 8px 8px 8px;
    margin-top: 25px;
    padding: 25px; 
}
#submit_form{
    text-align: center;
}
#submit_form input{
    margin-left: 5px;
}
#ip_text{
    font-size: 105%;
    text-align: center;
}
#submit_form .gray{
    color: gray;
    text-align: center;
}
#result h2{
    text-align: center;
    margin-top: 15px;
    font-size: 150%
}
#resultarea{
    margin-top: 15px;
}
#resultarea td{
    padding: 5px;
    text-align: center;
}
#loading-icon{
    display: none;
    margin: auto;
    margin-top: 5px;
}
</style>
</head>
<body>
    <div id="doc">
        <div id="hd">
        <div id="bd">
            <form id="submit_form" method="GET">
                <p>
                    <input class="gray" id="ip_text" type="text" name="ip" value="Enter IP Address"/>
                    <input class="submit-btn" id="submit_button" type="submit" value="Submit" />
                    <img id="loading-icon" src="loading_icon.gif" />
                </p>
            </form>
            <div id="result">{$result}</div>
        <div id="ft">
    </div>
</body>
<script type="text/javascript" src="http://yui.yahooapis.com/combo?2.9.0/build/yahoo-dom-event/yahoo-dom-event.js&2.9.0/build/connection/connection-min.js"></script>
<script type="text/javascript" src="ip_locator.js"></script>
</html>
MARKUP;
        echo $html;
    }
?>
