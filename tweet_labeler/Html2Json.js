$(document).ready(function(){

	$( "#save-btn" ).click(function() {

		var tweets = [];

		$("tbody tr").each(function(index, value) {
			$this = $(this);
    			var $table = $('#tweets-table');
    			var itemsLength = $table.find('th').length;
			var obj = {};

    			for (i=1;i<itemsLength;i++) {
				if (i < 2){
        				var key = $table.find('th').eq(i).text();
        				var value = $this.find('td').eq(i).text();
        				obj[key] = value;
				} else {
					var key = $table.find('th').eq(i).text();
    		    			var value = $this.find('td').eq(i).find('#dropdown option:selected').text();
					obj[key] = value;
				}
    			}
    			
			tweets.push(obj)
		});
		
		var data = "text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(tweets));
		$('<a href="data:' + data + '" class="btn btn-info" role="button" download="export.json">download JSON</a>').appendTo('div.table-responsive');
	});
})
