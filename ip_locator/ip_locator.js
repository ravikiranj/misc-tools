YAHOO.namespace("ip_locator");
YAHOO.ip_locator = function() {
    var YUD = YAHOO.util.Dom;
    var YUE = YAHOO.util.Event;

    function __init(){
        YUE.addListener("submit_form", "click", _handleClick);
    }

    function _handleClick(e) {
        var targ = YUE.getTarget(e);
        var target = targ;
        var tagName = targ.tagName.toUpperCase();
        if(tagName != 'A' && tagName != 'INPUT' && tagName != 'BUTTON' && tagName != 'IMG') {
            return;
        }
        if(!targ.className) {
            while(target){
                target = target.parentNode;
                if(target.className){ 
                    targ = target;
                    break;
                }
            }
            if(!targ.className) {
                return;
            }
        }
        /*Process for various events based on className*/
        if(YUD.hasClass(targ, "submit-btn")) {
            getLocationInfo(targ);
            YUE.preventDefault(e);
        }else if (YUD.hasClass(targ, "gray")){
            clearTextBox(targ);
            YUE.preventDefault(e);
        }
    }

    function clearTextBox(targ){
        targ.value = '';
        YUD.removeClass(targ, 'gray');
    }

    function getLocationInfo(targ){
        //Get ip
        var ip = YUD.get('ip_text').value;
        var ipRegex = /\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}/;
        if(!ip.match(ipRegex)){
            alert("Please enter a valid IP Address to continue...");
            return;
        }
        //Show loading icon
        var loadingIcon = YUD.get('loading-icon');
        YUD.setStyle(loadingIcon, 'display', 'block');
        var url = 'http://localhost/tools/ip_locator_ajax.php?ip='+ip;
        var callback = {
                        success: getLocationInfoSuccess,
                        failure: getLocationInfoFailure
        };
        var request = YAHOO.util.Connect.asyncRequest('GET', url, callback);
    } 

    function getLocationInfoSuccess(o){
        //Hide loading icon
        var loadingIcon = YUD.get('loading-icon');
        YUD.setStyle(loadingIcon, 'display', 'none');
        if(o.responseText){
            var result = YUD.get('result');
            result.innerHTML = o.responseText;
        }
    }

    function getLocationInfoFailure(o){
        //Hide loading icon
        var loadingIcon = YUD.get('loading-icon');
        YUD.setStyle(loadingIcon, 'display', 'none');
    }

    __init();
}();
