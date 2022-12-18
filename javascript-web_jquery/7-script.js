$(document).ready(function () {
	console.log("asdasd")
	const header = $("div#character");
	getCharacter().then((character) => {
		header.html(character.name);
	});
});
const getCharacter = async () => {
	const response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
	return await response.json();
}