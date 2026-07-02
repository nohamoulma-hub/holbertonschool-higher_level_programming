// On sélectionne l'élément où on va afficher le nom
const character = document.querySelector('#character');

// On envoie une requête vers l'API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  // 1er .then : on reçoit la réponse HTTP brute, on extrait son contenu en JSON
  .then((response) => response.json())
  // 2ème .then : on reçoit enfin les données exploitables (l'objet JSON)
  .then((data) => {
    // On affiche le nom du personnage dans l'élément #character
    character.textContent = data.name;
  });
  