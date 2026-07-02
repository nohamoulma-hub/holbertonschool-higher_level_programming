#!/usr/bin/node

// On récupère uniquement les vrais arguments (on enlève node et le chemin du script)
const args = process.argv.slice(2);

// Cas 0 ou 1 argument : on affiche 0 et on s'arrête là
if (args.length <= 1) {
  console.log(0);
} else {
  // On transforme le tableau de chaînes ('4', '2', ...) en tableau de nombres (4, 2, ...)
  const numbers = args.map((arg) => parseInt(arg));

  // On trie le tableau du plus grand au plus petit
  // (a, b) => b - a : si le résultat est positif, b passe avant a => tri décroissant
  numbers.sort((a, b) => b - a);

  // Une fois trié du plus grand au plus petit, le deuxième plus grand
  // se trouve à l'index 1 (l'index 0 étant le plus grand)
  console.log(numbers[1]);
}
