$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let itr = 0; itr < data.results.length; itr++) {
    $('UL#list_movies').append('<li>' + data.results[itr].title + '</li>')
  }
});
