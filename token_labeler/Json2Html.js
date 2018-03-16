$(document).ready(function(){

  var tweet_menu = "<td>" +
						"<select id='dropdown' class='selectpicker'>" +
						"<option>GOOD</option>" +
						"<option>BAD</option>" + 
						"</select></td></tr>";
	var dropdown_menu = "<td>" +
						"<select id='dropdown' class='selectpicker'>" +
						"<option>URL</option>" +
						"<option>LOCATION</option>" + 
						"</select></td></tr>";

    $.getJSON("tweets.json", function (data) {
        $.each(data, function (index, value) {
            var tabel_row = "<tr>" + "<td>" + "tweet" + "</td>" + "<td>" + value.text + "</td>" + tweet_menu;
						$(tabel_row).appendTo("#tweets-table tbody");
						$.each(value.tokens, function (index, value) {
	    				var tokens = "<tr>" + "<td>" + value.id + "</td>" + "<td>" + value.token + "</td>" + dropdown_menu;
							$(tokens).appendTo("#tweets-table tbody");
						});
        });
    });
});
