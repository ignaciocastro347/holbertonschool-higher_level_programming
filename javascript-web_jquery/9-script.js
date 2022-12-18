$(document).ready(function () {
	getTranslation().then((res) => {
		$("div#hello").html(res.hello);
	});
});
const getTranslation = async () => {
	const response = await fetch("https://stefanbohacek.com/hellosalut/?lang=fr");
	return await response.json();
}