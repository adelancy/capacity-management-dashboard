/**
 * Created by adrian.p.delancy on 10/27/2016.
 */

var module = {
    addButtonListeners: function(){
        $('#team-select-dropdown').addEventListener('click', select_button_listener);
    }
};


var select_button_listener = function(event) {
    event.preventDefault();
    console.log('doing something');
};


//Main Function Todo: Replace with Require js module if the logic starts to get more complicated
$(document).ready(function () {

})();