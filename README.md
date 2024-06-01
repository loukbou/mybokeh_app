# 1. La description du projet 'Maroc-data-visualisation'

<p>
  Ce projet est sous forme d'une application Bokeh qui sert à analyser une dataset marocaine. La data choisie vise à capturer divers aspects du paysage du développement logiciel au Maroc, en se concentrant sur quatre domaines principaux : <strong>Éducation, Travail, Technologie et Communauté</strong>.
  <br><br> Notre objectif était d'utiliser les données de ce dataset pour réaliser des visualisations concrètes et informatives qui peuvent aider à mieux comprendre l'état actuel et les tendances du développement logiciel au Maroc.
  <br> À travers ces visualisations, nous espérons fournir des insights précieux aux développeurs, aux éducateurs, aux employeurs et à tous les membres de la communauté technologique marocaine.
</p>
<p>
  Le projet contient trois fichiers, chacun ayant un rôle spécifique :
  <ul>
    <li>
      Le premier fichier est un fichier Jupyter Notebook <strong>'Notebook.ipynb'</strong> qui offre une vue claire sur le dataset utilisé. Ce fichier vise principalement à explorer notre dataset avant de l'utiliser et de créer des visualisations. Il est essentiel de vérifier si le dataset est utile pour les visualisations et de le nettoyer si nécessaire. Ce fichier contient également des visualisations simples pour tester le dataset avant et après le nettoyage.
    </li>
    <li>
      Le deuxième fichier est un fichier Python <strong>'main.py'</strong> qui contient notre application Bokeh. Dans ce fichier, vous pouvez voir toutes les visualisations que nous avons réalisées. Vous pouvez ainsi obtenir une idée générale et aussi détaillée concernant les résultats de  la première enquête <em>"State of Dev Survey"</em> lancée par Developer Circles Morocco.
    </li>
  </ul>
</p>


## 3. Installation et configuration

<p>
  Pour utiliser cette application, suivez les étapes ci-dessous :
  <ol>
    <li>Clonez le dépôt depuis GitHub : <code>git clone https://github.com/najiaamghouz/maroc-data-visualization</code></li>
    <li>Accédez au répertoire du projet : <code>cd Maroc-data-visualisation</code></li>
    <li>Installez les dépendances nécessaires : <code>pip install -r requirements.txt</code></li>
    <li>Lancez l'application Bokeh : <code>bokeh serve --show main.py</code></li>
  </ol>
</p>

## 4. Contribuer

<p>
  Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre les étapes ci-dessous :
  <ul>
    <li>Forkez le dépôt sur GitHub.</li>
    <li>Créez une nouvelle branche pour votre fonctionnalité ou correction de bug : <code>git checkout -b nom-de-la-branche</code></li>
    <li>Apportez vos modifications et committez-les : <code>git commit -m "Description de vos modifications"</code></li>
    <li>Push la branche sur votre fork : <code>git push origin nom-de-la-branche</code></li>
    <li>Soumettez une pull request pour révision.</li>
  </ul>
</p>


## 5. Licence

<p>
  Ce projet est sous licence MIT. Veuillez consulter le fichier <strong>LICENSE</strong> pour plus de détails.
</p>

## 6. Les visualisations

### Voici la première visualisation

![V1](https://github.com/najiaamghouz/maroc-data-visualization/assets/171170836/525e9f45-38cc-4f49-bd42-9a6cd6fd2643)
 
<p>
  la premiere visualisation simple elle contient juste la distribution des niveaux d'éducation dans l'ensemble de données présenté.
  <ul>
     <li> La visualisation montre une tendance claire où la majorité des développeurs ont un niveau Bac +5, suggérant peut-être une préférence ou une exigence pour ce niveau dans le contexte étudié.</li>
    <li> Le faible nombre de développeurs avec un niveau Bac +8 pourrait indiquer une plus grande rareté de ce niveau d'éducation ou des exigences spécifiques et plus élevées pour atteindre ce niveau.</li>
  </ul>
</p>


### Voici la deuxième visualisation


![V3](https://github.com/najiaamghouz/maroc-data-visualization/assets/171170836/23b7635d-0954-450b-be8b-75372d3ac327)


<p>
 La deuxième visualisation sert à représenter la distribution des développeurs entre ceux qui préfèrent immigrer en dehors du Maroc et ceux qui préfèrent rester au Maroc.
  <ul>
     <li>La visualisation montre une tendance claire où la majorité des développeurs back-end (environ 200 personnes) envisagent l'immigration, ce qui pourrait suggérer des facteurs comme de meilleures opportunités de travail, des conditions de vie, ou d'autres motivations personnelles ou professionnelles.</li>
    <li> Le nombre plus faible de développeurs back-end (environ 80 personnes) sans plans d'immigration pourrait indiquer une satisfaction avec leur situation actuelle ou des obstacles à l'immigration. </li>
  </ul>
</p>

### Voici une autre version de la deuxième visualisation

![V4](https://github.com/najiaamghouz/maroc-data-visualization/assets/171170836/110bc7d6-507c-4007-99e6-67f08799e793)



<p>
La visualisation montre un histogramme représentant <code> les plans d'immigration des cadres supérieurs (Senior executive/VP) </code>.
  <ul>
     <li>La visualisation montre une tendance où la majorité des cadres supérieurs préfèrent rester au Maroc, n'envisageant pas l'immigration.</li>
    <li> Le nombre plus faible de cadres supérieurs ayant des plans d'immigration pourrait indiquer une satisfaction avec leur situation actuelle ou des obstacles à l'immigration. </li>
  </ul>
</p>

> [!IMPORTANT]
> Cette visualisation est interactive ; on peut à chaque fois choisir un intitulé de poste différent pour voir la répartition des plans d'immigration parmi les développeurs.

### Voici la troisième visualisation

![V5](https://github.com/najiaamghouz/maroc-data-visualization/assets/171170836/54bd045e-3ef1-47a8-9618-7afb504f4229)

<p>
La visualisation montre un histogramme représentant les intitulés de poste en fonction de l'expérience en codage (années d'expérience) pour une sélection de 1-3 ans.
  <ul>
     <li>La visualisation montre une forte tendance vers les postes de "Developer, full-stack" parmi ceux ayant 1-3 ans d'expérience en codage.</li>
    <li> Les rôles de développeur spécialisés comme front-end et back-end sont également populaires. </li>
     <li> Les postes non directement liés au développement, comme ceux dans l'éducation, le DevOps, et le design, sont beaucoup moins représentés. </li>
  </ul>
</p>

> [!IMPORTANT]
> Cette visualisation est aussi interactive et permet de choisir différentes plages d'années d'expérience pour voir la répartition des intitulés de poste parmi les développeurs.

### Voici la quatrième visualisation

![V6](https://github.com/najiaamghouz/maroc-data-visualization/assets/171170836/60723095-8fd0-4f0e-8d30-f09d35c43e16)


<p>
La visualisation  montre un histogramme représentant les plateformes d'apprentissage les plus populaires et les plus utilisées par les développeurs qui apprendre d'une façon continu, avec une fréquence d'apprentissage sélectionnée comme "Every few months". 
  <ul>
     <li>La visualisation montre une forte préférence pour les ressources en ligne gratuites et accessibles comme YouTube et la documentation officielle.</li>
    <li> Les ressources payantes et les livres sont également bien utilisés, indiquant que les apprenants sont disposés à investir dans des ressources de qualité.</li>
     <li> Les ressources de l'entreprise et autres sources sont les moins populaires, peut-être en raison de leur accessibilité limitée ou de leur qualité perçue. </li>
  </ul>
</p>

### Voici la cinquième visualisation

![V7](https://github.com/najiaamghouz/maroc-data-visualization/assets/171170836/13bb329f-1f41-460b-b8e1-f112be47c3d5)


<p>
La visualisation  montre un histogramme représentant les sources les plus courantes d'aide pour les développeurs en fonction de leur expérience en codage. 
  <ul>
     <li>"Google it" semble être la source d'aide la plus populaire parmi les développeurs <code> ayant 1 à 3 ans d'expérience </code>, avec plus de 500 utilisateurs.</li>
    <li> "Call a coworker or friend" et "Do other work and come back later" sont des méthodes moins fréquemment utilisées, mais encore présentes parmi cette population de développeurs.</li>
  </ul>
</p>

> [!IMPORTANT]
> Cette visualisation montre un graphique interactif qui permet aux utilisateurs de visualiser les sources d'aide les plus courantes pour les développeurs en fonction de leur expérience en codage. 

### Voici la dérnière visualisation


![V8](https://github.com/najiaamghouz/maroc-data-visualization/assets/171170836/0d6c1bf6-d65d-40cd-a508-3a7c8ff5d687)



<p>
Le graphique présenté est un diagramme circulaire (ou donut chart) représentant la distribution des problèmes liés à l'enseignement. 
</p>

> [!IMPORTANT]
>  Le problème le plus dominant représenté dans cette visualisation est lié aux 'Sujets définis académiquement (système)'. Cela suggère que les répondants trouvent que les sujets définis par le système académique posent les plus grands défis dans l'enseignement.

<p> 
  <br>
</p>


## Voici les points clés importants

Merci d'avoir pris le temps de parcourir ce projet. À travers les différentes analyses et visualisations interactives présentées, nous avons pu obtenir des insights précieux sur divers aspects de l'expérience des développeurs, leurs préférences, et les défis qu'ils rencontrent.

1. **Plans d'Immigration** : La majorité des développeurs, notamment ceux occupant des postes de back-end, montrent une forte inclination à immigrer pour de meilleures opportunités. Cette tendance peut refléter des aspirations professionnelles globales et la recherche de conditions de travail optimales.
  
2. **Expérience en Codage et Titres de Poste** : Les développeurs avec peu d'expérience (1-3 ans) sont majoritairement des développeurs full-stack. Cela pourrait indiquer une entrée commune dans le domaine par le biais de compétences polyvalentes.

3. **Fréquence d'Apprentissage Continu** : YouTube et la documentation officielle se révèlent être les plateformes d'apprentissage les plus populaires, soulignant l'importance des ressources facilement accessibles et actualisées pour les développeurs.

4. **Sources d'Aide** : Les développeurs débutants (1-3 ans) préfèrent des sources d'aide comme les vidéos tutoriels et StackOverflow, indiquant une reliance sur des ressources facilement digestibles et interactives.

5. **Défis dans l'Enseignement** : Les 'Sujets définis académiquement (système)' sont le problème le plus dominant, ce qui souligne un besoin crucial d'aligner les curriculums académiques avec les réalités et exigences pratiques de l'industrie.

<p> 
  <br>
</p>

### Conclusion

Ce projet vise à fournir une vue d'ensemble complète et interactive des divers facteurs influençant les développeurs dans leurs carrières. Les visualisations interactives permettent une exploration dynamique des données, offrant des perspectives qui peuvent guider les éducateurs, les étudiants, et les professionnels du secteur. Les insights obtenus peuvent être utilisés pour améliorer les stratégies éducatives, les politiques d'entreprise, et les parcours de développement professionnel.

Nous espérons que ce projet vous a offert une compréhension plus approfondie des dynamiques et des tendances actuelles dans le monde du développement logiciel. Votre feedback et vos contributions sont précieux pour continuer à enrichir et améliorer ce projet. 

Merci de votre intérêt et bonne exploration !

---

Si vous avez des questions ou des suggestions, n'hésitez pas à ouvrir une issue ou à nous contacter. Ensemble, faisons progresser la connaissance et l'innovation dans le domaine du développement logiciel.

---





