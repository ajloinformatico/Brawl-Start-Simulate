<h1>BrawlersStart</h1>
BrawlersStart es un programa escrito en python
que simula la apertura de cartas en Brawl Star
<h2>Características</h2>
<ul>
<li>
Se suministra un archivo denominado brawlers 
con distintos personajes del juego organizados en dos líneas cada uno.
La primera es el tipo brawler y el segundo el nombre
Ejemplo:<br>
especial<br>
barley<br>
superespecial<br>
rico
</li>
<li>
Se cargarán los brawlers en memoria.
</li>
<li>
Se solicitará el nombre al jugador. Cada jugador cuenta con un archivo con su nombre y la 
misma estructura que el archivo brawler con los personajes de los que disponga. Si ese archivo no existe se creará
un archivo nuevo para el jugador vacio.
</li>
<li>
Una vez cargador el jugador se mostrará el nombre del jugador, sus personajes y se le pedirá que introduzca un texto
</li>
<li>
Si el jugador escribe <b>fin</b> Se sobreescribe el archivo con los personajes de los que disponga
</li>
<li>
Si el jugador escribe <b>borrar partida</b> Se eleiminará su archivo y el juego preguntará si desea volver a jugar
</li>
<li>
Si el jugador escribe <b>simular</b> seguido de un <b>número</b>, hasta un máximo de 10 días.<br>
Por ejemplo:<br>
<b>simular 9</b>
</li>
</ul>
<h2>Notas</h2>
Se usará la librería random.