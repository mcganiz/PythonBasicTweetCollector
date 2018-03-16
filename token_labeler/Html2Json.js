$(document).ready(function(){

  var token_flag = 0
	var $table = $('#tweets-table');
	var itemsLength = $table.find('th').length;
	
	$( "#save-btn" ).click(function() {

		var tweets = [];
		
		$("tbody tr").each(function(index, value) {
			$this = $(this);
    	
			var obj = {};
			var tweet_json = {};

    	for (i=0;i<itemsLength;i++) {
				if (i < 2){
        	var key = $table.find('th').eq(i).text();
        	var value = $this.find('td').eq(i).text();
        	if (i == 0 && value == 'tweet') {
						token_flag = 0;
						tokens = [];
        	} else if (i == 0 && value == '0') {
        		token_flag = 1;
        	}
        	if (token_flag == 1) {
        		if (i == 1) {
        			obj['token'] = value;
        		} else {
        			obj[key] = value;
        		}
    			} else {
    				tweet_json[key] = value;
    			}
				} else {
					var key = $table.find('th').eq(i).text();
    		  var value = $this.find('td').eq(i).find('.selectpicker option:selected').text();
					if (token_flag == 1) {
    				obj[key] = value;
    			} else {
    				tweet_json[key] = value;
    			}
				}
    	}
    	if (token_flag == 1) {
    		tokens.push(obj);
    	} else {
    		tweet_json['tokens'] = tokens;
      	tweets.push(tweet_json);
    	}
		});
		
		var data = "text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(tweets));
		$('<a href="data:' + data + '" class="btn btn-info" role="button" download="export.json">download JSON</a>').appendTo('div.table-responsive');
	});
})
