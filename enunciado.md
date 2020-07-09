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
<li>
Cada día se abrirán dos cajas brawler. Cada caja brawler puede traer un brawler con la siguiente probabilidad en sus tipos.<br>
<ul>
<li>legendario: 0.062%</li>
<li>mitico: 0.02496%</li>
<li>epico: 0.5472%</li>
<li>superespecial: 1.2096%</li>
<li>especial: 2.7312%</li>
</ul>
</li>
<li>
Cada 2.5 días se abrirá una caja grande. <b>equivale a 3 cajas brawler</b>
</li>
<li>Cada personaje que recibe de un personaje de un tipo de brawler debe ser un personaje que no posea si los posee todos de un tipo se le dará la enorabuena. Si los posee todos se le dirá que ha ganado</li>
</ul>
<h2>Notas</h2>
Se usará la librería random.<br>
La sentencia random.uniform(0.00001, 100.0) devuelve un número
flotante de entre 0,00001 y 100<br>
Es intenteresante crear una lista desordenada con los brawlers que notiene el jugador
y otra con los que si