SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `quizz`
--

-- --------------------------------------------------------

--
-- Structure de la table `questions`
--
DROP TABLE IF EXISTS `questions`;
CREATE TABLE IF NOT EXISTS `questions` (
  `id` int NOT NULL,
  `question` varchar(256) NOT NULL,
  `rep1` varchar(256) NOT NULL,
  `rep2` varchar(256) NOT NULL,
  `rep3` varchar(256) NOT NULL,
  `rep4` varchar(256) NOT NULL,
  `repJuste` int NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `questions`
--

INSERT INTO `questions` (`id`, `question`, `rep1`, `rep2`, `rep3`, `rep4`, `repJuste`) VALUES
(1, 'Quand sont apparus les premiers systèmes informatiques ?', 'Au 20ème siècle', 'Aux 19ème siècle', 'Aux 18ème siècle', 'Hier', 1),
(2, 'Que veut dire S.A.G.E. ?', 'Simple Action in Great Environment', 'Semi Automatic Ground Environment', 'Sage', 'Sans Avenir au Grand Est', 2),
(3, 'Qui a créé le language Python ?', 'M.Bricard', 'Yukihiro Matsumoto', 'Dennis Ritchie', 'Guido van Rossum', 4),
(4, 'Qui a écrit \"Les Misérables\" ?', 'Émile Zola', 'Victor Hugo', 'Albert Camus', 'Gustave Flaubert', 2),
(5, 'Qu\'est-ce qu\'un MVP dans le contexte d\'une entreprise ?', 'Most Valuable Player', 'Une version d\'un produit qui offre les fonctionnalités de base nécessaires pour être fonctionnelle et testée', 'Un produit conçu pour maximiser le profit dès le lancement', 'Un prototype de produit sans validation de marché', 2),
(6, 'Quelle est l\'une des cartes les plus détestées dans le jeu de cartes Yu-Gi-Oh ?', 'Exodia', 'Force miroir', 'Mystic Mine', 'Dragon blanc aux yeux bleus', 3),
(7, 'Qui a créé le language JavaScript ?', 'Sun Microsystems', 'Rasmus Lerdorf', 'Akira Toriyama', 'Brendan Eich', 4),
(8, 'Qui incarne le rôle principal de J. Robert Oppenheimer dans le film de Christopher Nolan sorti en 2023 ?', 'Leonardo DiCaprio', 'Matt Damon', 'Cillian Murphy', 'Tom Hardy', 3),
(9, 'Qui est l\'auteur de Black Clover ?', 'Eiichirō Oda', 'Yūki Tabata', 'Masashi Kishimoto', 'Tsugumi Ōba', 2),
(10, 'Qui est le fondateur de SpaceX ?', 'Jeff Bezos', 'Dwight D. Eisenhower', 'Elon Musk', 'William Edward Boeing', 3),
(11, 'Quel est le combat le plus iconique de Dragon Ball ?', 'Son Goku VS Freezer', 'Krilin VS Saitama', 'Gogeta VS Piccolo', 'Nappa VS Son Gohan', 1),
(12, 'Quelle est la plus grande maison d\'édition de manga du Japon ?', 'C\'est quoi un manga ?', 'Kazé', 'Shougakukan', 'Shueisha', 4),
(13, 'Quelle est la pire adaptation de manga/animé en Live-Action ?', 'Death Note', 'Dragon Ball Evolution', 'The Promised Neverland', 'Je sais pas', 2),
(14, 'Qui double Son Goku dans la version française de Dragon Ball ?', 'Éric Legrand', 'Masako Nozawa', 'Brigitte Lecordier', 'Toyotarō', 3),
(15, 'Quel est le deuxième nom de Son Goku ?', 'Kakarotto', 'Broly', 'Sun Wukong', 'Son Goten', 1),
(16, 'Qui a interprété l\'OST Blizzard pour le film Dragon Ball Super: Broly ?', 'PNL', 'Yoshihiro Togashi', 'Daichi Miura', 'Akira Kushida', 3),
(17, 'Quelle est la suite de Dragon Ball la moins populaire ?', 'Dragon Ball Super', 'Dragon Ball AF', 'Dragon Ball Z', 'Dragon Ball GT', 4),
(18, 'Qu\'est-ce qui est érit sur la machine à remonter le temps de Trunks dans Dragon Ball ?', 'Revenge', 'Hope !!', 'Cell', 'Terminator', 2),
(19, 'Que signifie Yu-Gi-Oh en japonais ?', 'Le roi des jeux', 'Jouons aux jeux !', 'Je ne sais pas jouer', 'Hein ?', 1),
(20, 'Quel acteur joue le rôle de Neo dans la saga \"Matrix\" ?', 'Keanu Reeves', 'Brad Pitt', 'Johnny Depp', 'Tom Cruise', 1),
(22, 'Quel film de science-fiction réalisé par Ridley Scott en 1979 met en scène un vaisseau spatial et une créature extraterrestre ?', 'Prometheus', 'Interstellar', 'Alien', 'Blade Runner', 3);

-- --------------------------------------------------------

--
-- Structure de la table `users`
--
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `username` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `mdp` varchar(256) NOT NULL,
  `score` int NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`username`, `mdp`, `score`) VALUES
('joueur1', 'gggggggg', 7523);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
