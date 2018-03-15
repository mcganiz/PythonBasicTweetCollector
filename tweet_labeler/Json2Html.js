$(document).ready(function(){

    var dropdown_menu = "<td>" + "<select id='dropdown' class='selectpicker'>" + "<option>GOOD</option>" + "<option>BAD</option>" + "</select>";

    $.getJSON("tweets.json", function (data) {
        $.each(data, function (index, value) {
            var tabel_row = "<tr>" + "<td>" + index + "</td>" + "<td>" + value.text + "</td>" + dropdown_menu;
            $(tabel_row).appendTo("#tweets-table tbody");
        });
    });
});
