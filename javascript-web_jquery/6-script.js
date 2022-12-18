$(document).ready(function () {
	const header = $("header");
	$("div#update_header").on("click", function () {
		header.html("New Header!!!");
	})
});