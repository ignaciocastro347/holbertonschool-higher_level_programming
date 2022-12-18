$(document).ready(function () {
	const header = $("header");
	$("div#toggle_header").on("click", function () {
		header.toggleClass("red");
		header.toggleClass("green");
	})
});