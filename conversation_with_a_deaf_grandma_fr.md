 ### Exercice: conversation avec une grand-mère sourde (d'après [Chris Pine](https://pine.fm/LearnToProgram/chap_06.html))
> Quoi que vous disiez à Mamie, elle vous crie `"HUH?! SPEAK UP, SONNY!"`, à moins que vous ne vous mettiez à crier vous aussi (c'est-à-dire à taper tout en majuscules). Elle vous crie alors en réponse: `"NO, NOT SINCE 1938!"` (avec une année aléatoire entre 1930 et 1950). Pour terminer la conversation, commencez votre phrase par `"BYE"`.
>
> 1. Écrivez un simulateur de grand-mère sourde (américaine, française ou allemande, comme vous préférez) sous la forme d'une procédure `talk` sans paramètres.
>
>         In []: talk()
>                > Hello Grandma!
>                HUH?!  SPEAK UP, SONNY!
>                > HELLO! ARE YOU OK THIS MORNING?
>                NO, NOT SINCE 1932!
>                > BYE GRANDMA!
>                BYE, SONNY!
>
> 2. Ajoutez à ce [_chatterbot_](http://en.wikipedia.org/wiki/Chatterbot) les fonctionnalités de votre choix. Le but est d'utiliser un maximum d'[opérations sur les séquences](http://rgruet.free.fr/PQR27/PQR2.7.html#SequenceTypes) et de [méthodes sur les chaînes](http://rgruet.free.fr/PQR27/PQR2.7.html#stringMethods). Dans l'exercice original, l'auteur suggère que Mamie ne vous laisse pas partir avant que vous n'ayez crié trois fois de suite `"BYE"`. Elle peut aussi déformer ce que vous dites, radoter, réagir à la longueur de vos interventions, à certains mots-clefs, à la ponctuation, etc. La seule limite est votre inventivité. Travaillez en équipe sur un même _gist_, dont le propriétaire intégrera les modifications que vous lui proposerez en commentaire.