$(document).ready(function () {
	const ul = $("ul.my_list");
	$("div#add_item").on("click", function () {
		ul.append("<li>Item</li>");
	})
});