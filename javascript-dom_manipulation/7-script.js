// On sélectionne la liste où on va ajouter les titres
const listMovies = document.querySelector('#list_movies');

// On récupère les données depuis l'API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    // 'data.results' est un tableau contenant tous les films
    for (const movie of data.results) {
      // Pour chaque film, on crée un nouvel élément <li>
      const li = document.createElement('li');
      // On y met le titre du film
      li.textContent = movie.title;
      // On ajoute ce <li> dans la liste
      listMovies.appendChild(li);
    }
  });
