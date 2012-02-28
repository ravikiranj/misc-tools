<?php
    // Replace the secret key below in params array for the code to work
    function displayHTML($msg, $number, $start){
        $html = <<<HTML
<html>
<head><title>Send SMS to India</title>
<style>
#doc{
    margin: auto; /* center in viewport */
    width: 760px;
    border: 1px solid #C0C0C0;
    -webkit-border-radius: 8px; /* Saf3-4, iOS 1-3.2, Android =1.6 */
    -moz-border-radius: 8px; /* FF1-3.6 */
    border-radius: 8px; /* Opera 10.5, IE9, Saf5, Chrome, FF4, iOS 4, Android 2.1+ */
    padding: 25px;
    margin-top: 50px;
    margin-bottom: 25px;
}
#bd{
}
.small{
    font-size: 81%;
}
#smsform{
    font-size: 91%;
}
.error{
    color: red;
}
.success{
    color: green;
}
#ft{
    text-align: center;
    font-size: 91%;
}
</style>
</head>
<body>
    <div class="yui3-g" id="doc">
        <div class="yui3-u" id="hd"><h2>Send SMS to India Hack</h2></div>
        <div class="yui3-u" id="bd">        
            <form id="smsform" method="post" onsubmit="return validateForm(this)">
                <div>Mobile No. (10 digits)</div>
                <input type="text" id="num" name="num" maxlength="10" /></br></br>
                
                <div>Message</div>
                <textarea name="msg" rows=4 cols=40 id="msg" onKeyDown="limitText(this.form.msg,this.form.countdown,140);" onKeyUp="limitText(this.form.msg,this.form.countdown,140);"></textarea></br>
                <div class="small">(Maximum characters: 140)</div>
                <div class="small">You have <input readonly type="text" name="countdown" size="3" value="140" /> characters left.</div></br>
                <div><input type="submit" value="Submit"  /></div>
            </form>
HTML;
        if(!$start){
            $ch = curl_init();
            $url = "http://s2.freesmsapi.com/messages/send?";
            /* REPLACE YOUR SECRET KEY HERE */
            $params = array('response' => 'json',
                            'skey' => 'REPLACE YOUR SECRET KEY HERE',
                            'message' => $msg,
                            'recipient' => $number
                            );
            foreach($params as $key=>$value){
                $url .= $key . "=" . urlencode($value) . "&";
            } 
            //remove last &
            $url = substr($url, 0, -1); 
            curl_setopt($ch, CURLOPT_URL, $url);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);    
            $response = curl_exec($ch); // execute curl session
            $data = json_decode($response, true);
            curl_close($ch);
            if(!$data || (isset($data['response']) && isset($data['response']['errors']))){
                $html .= "<div class='error'>Message sending failed :(, please try again after sometime</div>"; 
            }else{
                $html .= "<div class='success'>Message sent successfully to $number :) ! Have a nice day !</div>";
            }
        }
        $html .= <<<HTML
</div>
</div>
<div id="ft">Hack by Ravikiran Janardhana</div>
<script type="text/javascript">
function limitText(limitField, limitCount, limitNum) {
	if (limitField.value.length > limitNum) {
		limitField.value = limitField.value.substring(0, limitNum);
	} else {
		limitCount.value = limitNum - limitField.value.length;
	}
}
function validateForm(dataform){
    var num = dataform.num.value;
    var pat = /[1-9][0-9]{9}/;
    var msg = dataform.msg.value;
    if(pat.test(num) && msg){
        return true;
    }else{
        if(!pat.test(num)){
            alert("Mobile no. should be 10 digits");
        }else{
            alert("Cannot send an empty message");
        }
        return false;
    }
}
</script>
</body>
</html>    
HTML;
        echo $html;
    }
    function init(){
    	if(!empty($_POST['msg']) && !empty($_POST['num'])){
    	    displayHTML($_POST['msg'], $_POST['num'], 0);
    	}else{
    	    displayHTML('', '', 1);
    	}
    }
    init();
?>
