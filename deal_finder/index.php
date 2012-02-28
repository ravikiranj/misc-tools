<?php
    global $debug;
    $debug = 0;
    function getData($keyword){
        $result = "";
        $yql_url = "http://query.yahooapis.com/v1/public/yql?";
        $url_list = array(  'http://feeds.feedburner.com/SlickdealsnetFP',
                            'http://feeds.feedburner.com/bargainist',
                            'http://www.deals2buy.com/rssgen/alldeals.xml',
                            'http://www.dealsofamerica.com/arss.xml',
                            'http://feeds.dealtaker.com/feed_engine/feed-deals.xml',
                            'http://rss.dealcatcher.com/rss.xml',
                            'http://www.techbargains.com/rss.xml');

        //Add quotes to start and end of url
        for($i = 0; $i < sizeof($url_list); $i++){
            $url_list[$i] = "'" . $url_list[$i] . "'";
        }
        //Combine it to a string
        $url_string = implode(",", $url_list);
        $yql_query = "select * from feed where url in ($url_string) and title like '%{$keyword}%'  | unique(field='link') | sort(field='pubDate', descending='true')";
        $query_url = $yql_url . "format=json&q=" . urlencode($yql_query);

        $ch = curl_init(); // open curl session
        // set curl options
        curl_setopt($ch, CURLOPT_URL, $query_url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);    
        $response = curl_exec($ch); // execute curl session
        $data = json_decode($response, true);
        if(!$data){
            return -1;
        }
        if($GLOBALS['debug']){
            echo "<pre>"; print_r($data); echo "</pre>";
            exit;
        }
        return $data;
    }

    function getArticleAgeString($article_time) {
         $current_time = time();
         $time_diff = $current_time - $article_time;
 
         if ($time_diff < 0) {
             return '';
         } elseif ($time_diff < (60 * 60)) {
             $minutes = floor($time_diff / 60);
             return ($minutes == 1) ? '1 minute ago' : sprintf('%d minutes ago', $minutes);
         } elseif ($time_diff < (60 * 60 * 24)) {
             $hours = floor($time_diff / (60 * 60));
             return ($hours == 1) ? '1 hour ago' : sprintf('%d hours ago', $hours);
         } elseif ($time_diff < (60 * 60 * 24 * 7)) {
             $days = floor($time_diff / (60 * 60 * 24));
             return ($days == 1) ? '1 day ago' : sprintf('%d days ago', $days);
         } elseif ($time_diff <= (60 * 60 * 24 * 30)) {
             $weeks = floor($time_diff / (60 * 60 * 24 * 7));
             return ($weeks == 1) ? '1 week ago' : sprintf('%d weeks ago', $weeks);
         } elseif ($time_diff < (60 * 60 * 24 * 365)) {
             // just take a rough estimation. No need to put complicated algorithm here
             $months = floor($time_diff / (60 * 60 * 24 * 30));
             return ($months == 1) ? 'one month ago' : sprintf('%d months ago', $months);
         } elseif ($article_time == 0) {
             return '';
         } else {
             return 'one year ago';
         }
     }     
    function getHTML($data, $keyword){
        $html = <<<HTML
<html>
<head><title>Deal Finder</title>
<link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/3.4.1/build/cssgrids/grids-min.css" />
<link rel="stylesheet" type="text/css" href="styles.css" />
</head>
<body>
    <div class="yui3-g" id="doc">
        <div class="yui3-u" id="hd">
            <h2> Deal Finder </h2>
        </div>
        <div class="yui3-u" id="bd">
            <form id="key-form" method="post" action="/">
                <p><input type="text" value="" name="keyword" id="keyword"/><input type="submit" value="Submit" id="sub"/></p>
            </form>
HTML;
        if(!empty($data['query']) && !empty($data['query']['count']) && !empty($data['query']['results']) && !empty($data['query']['results']['item'])){
            $count = $data['query']['count'];
            $results = $data['query']['results']['item'];
            $html .= "<ul class='result-list'>";
            $descMaxLen = 300;
            $titleMaxLen = 80;
            for($i = 0; $i < $count; $i++){
                $link = ''; 
                if(isset($results[$i]['link'])){
                    $link = $results[$i]['link'];
                }
                if(isset($results[$i]['link']) && isset($results[$i]['link']['content']) && preg_match('/^http/', $results[$i]['link']['content'])){
                    $link = $results[$i]['link']['content'];
                }
                $full_title = isset($results[$i]['title']) ? $results[$i]['title'] : "No title found";
                //Encode special characters
                $full_title = htmlspecialchars($full_title);
                $title = $full_title;
                if(strlen($title) > $titleMaxLen){
                    $title = substr($full_title, 0, $titleMaxLen-4) . "...";
                }
                $desc = isset($results[$i]['description']) ? $results[$i]['description'] : "";
                //Remove links in description
                $desc = preg_replace('/<a[^>]*>(.*)<\/a>/iU','', $desc);
                if(strlen($desc) > $descMaxLen){
                    $desc = substr($desc, 0, $descMaxLen-4) . "...";
                }
                $rawPubDate = isset($results[$i]['pubDate']) ? $results[$i]['pubDate'] : "";
                $articleAgeString = '';
                if($rawPubDate){
                    //$pubDate = strftime("%Y-%m-%d %H:%M:%S", strtotime($rawPubDate));
                    $article_time = strtotime($rawPubDate);
                    $articleAgeString = getArticleAgeString($article_time); 
                }
                $html .= <<<HTML
<li class="result">
    <div class="title"><a href="{$link}" title="{$full_title}" target="_blank">$title</a><span class="timestamp"> $articleAgeString</span></div>
    <div class="description"><p>$desc</p></div>
</li>    
HTML;
            }
        }else{
            $html .= "<div class='nofound'>No results found for '$keyword'</div>";
        }
        $html .= "</ul></div></div><div id='ft'>Copyright © 2012 - Ravikiran Janardhana</div></body></html>";
        return $html;
    }

    function getInitHTML(){
        $html = <<<HTML
<html>
<head><title>Deal Finder</title>
<link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <div class="yui3-g" id="doc">
        <div class="yui3-u" id="hd">
            <h2> Deal Finder </h2>
        </div>
        <div class="yui3-u" id="bd">
        <form method="post" id = "key-form" action="/">
            <p><input type="text" value="" name="keyword" id="keyword"/><input type="submit" value="Submit" id="sub"/></p>
        </form>
        </div>
    </div>
    <div id='ft'>Copyright © 2012 - Ravikiran Janardhana</div>
</body>
</html>
HTML;
        return $html;
    }
    function init(){
        if(!isset($_POST['keyword'])){
            $html = getInitHTML();
            echo $html;
        }else{
            $keyword = $_POST['keyword'];
            $data = getData($keyword);
            if(!$data){
                echo "Error !!!!";
                exit;
            }
            $html = getHTML($data, $keyword);
            echo $html;
        }
    }

    init();

    
?>
