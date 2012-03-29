<?php
//Get matched words
function getMatches($letters, $k){
    $success = array();
    if($k < 2){
        return $success;
    }

    // Connects to your Database     
    $link = mysql_connect("localhost", "username", "passwd") or die(mysql_error());     
    mysql_select_db("dbname", $link) or die(mysql_error()); 

    $query = "select * from ind_words where char_length(word)={$k}";
    $result = mysql_query($query);
    $letterArr = str_split($letters);
    while ($row = mysql_fetch_array($result, MYSQL_BOTH)) {
        $word = trim($row[0]);
        $tempArr = $letterArr;
        $flag = 1;
        for($i = 0; $i < strlen($word); $i++){
            $found = 0;
            for($j = 0; $j < count($tempArr); $j++){
                if($word[$i] == $tempArr[$j]){
                    //Set this entry as null
                    $tempArr[$j] = '';
                    $found = 1;
                    break;
                }
            }
            if(!$found){
                $flag = 0;
                break;
            }
        }
        if($flag){
            $success[] = $word;
        }
    }
    if(!$success){
        sort($success);
    }
    return $success;
}

function getHTML($first, $success = array()){
    $letters = '';
    $wordlen = '';
    if(!$first){
        $letters = $_POST['letters'];
        $wordlen = $_POST['wordlen'];
    }
    $html = <<<HTML
<html>
<head><title>Draw Something Solver</title>
<style type="text/css">
body{
    margin: auto; /* center in viewport */
    width: 760px;
}
li{
}
#bd{
    border: 1px solid #C0C0C0;
    -webkit-border-radius: 12px; /* Saf3-4, iOS 1-3.2, Android ≤1.6 */
    -moz-border-radius: 12px; /* FF1-3.6 */
    border-radius: 12px; /* Opera 10.5, IE9, Saf5, Chrome, FF4, iOS 4, Android 2.1+ */
    margin-top: 25px;
    margin-bottom: 25px;
}
#main{
    padding: 25px;
}
#hd{
    margin-bottom: 25px;
}    
#hd h2{
    margin-right: 10px;
    display:  inline;
}
.field{
    margin-bottom: 15px;
}
#letter-form{
    clear: both;
}
#result-list{
    padding-left: 30px;
}

</style>

<body>
    <div class="yui3-g" id='bd'>
        <div class="yui3-u" id="main">
            <div id="hd"><h2>Draw Something Solver</h2><span>by Ravikiran Janardhana</span></div>
            <form method="post" id="letter-form">
                <div class='field'>
                    <span style="margin-right: 25px;">Enter all the letters</span>
                    <input type="text" name="letters" id="letters" value="{$letters}"/>
                </div>
                <div class='field'>
                    <span style="margin-right: 7px;">Enter the word length</span>
                    <input type="text" name="wordlen" id="wordlen" value="{$wordlen}"/>
                </div>
                <input type="submit" value="Submit">
            </form>
HTML;
        if(!$first){
            if(count($success) > 0){
                $resCount = count($success);
                $html .= "<div id='results'><div style='padding-left:10px;margin-bottom:-10px;'>{$resCount} words found</div><ol id='result-list'>";
                for($i = 0; $i < $resCount; $i++){
                    $html .= "<li>{$success[$i]} </li>";
                }
            }else{
                $html .= "<div id='results'><ol id='result-list' style='padding-left:0px;'>";
                $html .= "<li style='list-style-type:none;'>No matching words found.</li>";
            }
            $html .= "</ol></div>";
        }
        $html .= <<<HTML
        </div>
    </div>
</body>
HTML;
        return $html;
}

function init(){
    if(empty($_POST['letters']) || empty($_POST['wordlen'])){
        $html = getHTML(1);
    }else{
        $letters = trim($_POST['letters']);
        //Remove spaces in between
        $letters = strtolower(str_replace(' ', '', $letters));
        $wordlen = intval($_POST['wordlen']);

        if($wordlen <= strlen($letters)){
            $success = getMatches($letters, $wordlen);
            $html = getHTML(0, $success);
        }else{
            $success = array();
            $html = getHTML(0, $success);
        }
    }
    echo $html;
}

//call init
init();
?>