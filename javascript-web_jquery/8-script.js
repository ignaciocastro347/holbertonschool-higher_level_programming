$(document).ready(function () {
	getMovies().then((movies) => {
		movies.results.forEach((movie) => {
			$("ul#list_movies").append(`<li>${movie.title}</li>`);
		})
	});
});
const getMovies = async () => {
	const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
	return await response.json();
}