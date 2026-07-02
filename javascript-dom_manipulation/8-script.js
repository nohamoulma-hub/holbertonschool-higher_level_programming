// On attend que le DOM (le HTML) soit chargé et prêt
document.addEventListener('DOMContentLoaded', function () {
  // Une fois le DOM prêt, on peut lancer la requête vers l'API
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    // 1er .then : on reçoit la réponse HTTP, on extrait son contenu en JSON
    .then((response) => response.json())
    // 2ème .then : on reçoit enfin l'objet JSON exploitable
    .then((data) => {
      // Maintenant que le DOM est prêt, on peut sélectionner l'élément en toute sécurité
      const hello = document.querySelector('#hello');

      // On affiche la traduction (contenue dans data.hello) dans cet élément
      hello.textContent = data.hello;
    });
});
