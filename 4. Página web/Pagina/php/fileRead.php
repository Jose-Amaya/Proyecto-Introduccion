<!DOCTYPE HTML>

<html>

<head>
    
    <title>Testing</title>
    
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
    <link rel="stylesheet" href="../bootstrap-4.0.0-dist/css/bootstrap.css">
    <link rel="stylesheet" href="../css/changes.css">

    <script src="../js/jquery-3.3.1.js"></script>
    
    
    <script src="../js/jquery-1.7.1.min.js"></script>
    <script src="../js/jquery.simplyscroll.js"></script>
    <link rel="stylesheet" href="../css/jquery.simplyscroll.css" media="all" type="text/css">
    <script type="text/javascript">
        
    (function($) {
        $(function() {
            $("#scroller").simplyScroll();
        });
    })(jQuery);
        (function($) {
        $(function() {
            $("#scroller2").simplyScroll();
        });
    })(jQuery);
    </script>
    
    
</head>

<body id="mainbody">


    
<?php 
$file = fopen("/home/pi/project/data/files/infoWeb.txt","r"); # Se abre el archivo

$JEPIRACHI115 = fgets($file);
$FLORES = fgets($file);
$BARRANQUILLA = fgets($file);
$GUAJIRA = fgets($file);
$TASAJERO = fgets($file);
$TERMOSIERRAB = fgets($file);
$TERMOEMCALI1 = fgets($file);
$PAIPA = fgets($file);
$TERMOCENTROCC = fgets($file);
$ZIPAEMG = fgets($file);
$CARTAGENA = fgets($file);
$MERILECTRICA1 = fgets($file);
$LAHERRADURA = fgets($file);
$JAGUAS = fgets($file);
$SANCARLOS = fgets($file);
$SOGAMOSO = fgets($file);
$AMOYALAESPERANZA = fgets($file);
$MIELI = fgets($file);
$CALDERAS = fgets($file);
$GUAVIO = fgets($file);
$BETANIA = fgets($file);
$ELQUIMBO = fgets($file);
$PARAISO = fgets($file);
$LAGUACA = fgets($file);
$TEQUENDAMA = fgets($file);
$LATASAJERA = fgets($file);
$CARACOLI = fgets($file);
$ELLIMONAR = fgets($file);
$DARIOVALENCIASAMPER = fgets($file);
$LAGUNETA = fgets($file);
$PAJARITO = fgets($file);
$SANJOSEDELAMONTANA = fgets($file);
$TRONERAS = fgets($file);
$GUADALUPE3 = fgets($file);
$GUADALUPE4 = fgets($file);
$PORCEII = fgets($file);
$PORCEIII = fgets($file);
$GUATAPE = fgets($file);
$RIOABAJO = fgets($file);
$SONSON = fgets($file);
$RIOFRIOTAMESIS = fgets($file);
$AYURA = fgets($file);
$NIQUIA = fgets($file);
$URRA1 = fgets($file);
$CHIVOR = fgets($file);
$CUCUANA = fgets($file);
$CALIMA = fgets($file);

fclose($file);
    
?>
    
<!-- # OLD SOLUTION
<div id="div4" class="d-flex flex-row flex-nowrap text-nowrap card-columns">


<div class="card col-xl-2 changing">
    
<h1 class="card-header">Eólica 1</h1>
  <div class="card-body">
    <h4 class="card-title">Jepirachi</h4>
    <#?php
    if ($JEPIRACHI115 > 0) {
     echo("<p class=\"card-text\">En funcionamiento</p>");
    echo("<p class=\"btn btn-primary\">" . $JEPIRACHI115 . " MWh </p>");
    }
    else {
    echo("<p class=\"card-text\">No está en funcionamiento</p>");
    }
    ?>
  </div>
    
</div>

    
    
</div>
    
-->
<ul id="scroller">
        
<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">E 1</h1>
<div class="card-body">
<h4 class="card-title">Parque Eólico de Jepírachi</h4>
<?php
if ($JEPIRACHI115 > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $JEPIRACHI115 . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">T 1</h1>
<div class="card-body">
<h4 class="card-title">Termoflores</h4>
<?php
if ($FLORES > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $FLORES . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">T 2</h1>
<div class="card-body">
<h4 class="card-title">Termobarranquilla</h4>
<?php
if ($BARRANQUILLA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $BARRANQUILLA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">T 3</h1>
<div class="card-body">
<h4 class="card-title">Termoguajira</h4>
<?php
if ($GUAJIRA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $GUAJIRA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">T 4</h1>
<div class="card-body">
<h4 class="card-title">Termotasajero</h4>
<?php
if ($TASAJERO > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $TASAJERO . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">T 5</h1>
<div class="card-body">
<h4 class="card-title">Termosierra</h4>
<?php
if ($TERMOSIERRAB > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $TERMOSIERRAB . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">T 6</h1>
<div class="card-body">
<h4 class="card-title">Termoemcali</h4>
<?php
if ($TERMOEMCALI1 > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $TERMOEMCALI1 . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">T 7</h1>
<div class="card-body">
<h4 class="card-title">Termopaipa</h4>
<?php
if ($PAIPA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $PAIPA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">T 8</h1>
<div class="card-body">
<h4 class="card-title">Termocentro</h4>
<?php
if ($TERMOCENTROCC > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $TERMOCENTROCC . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">T 9</h1>
<div class="card-body">
<h4 class="card-title">Termoeléctrica Martin del Corral</h4>
<?php
if ($ZIPAEMG > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $ZIPAEMG . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">T 10</h1>
<div class="card-body">
<h4 class="card-title">Central Termica de Cartagena</h4>
<?php
if ($CARTAGENA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $CARTAGENA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">T 11</h1>
<div class="card-body">
<h4 class="card-title">Central Merilectric</h4>
<?php
if ($MERILECTRICA1 > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $MERILECTRICA1 . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



        
</ul>

<ul id="scroller2">
        
<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 1</h1>
<div class="card-body">
<h4 class="card-title">Central la Herradura</h4>
<?php
if ($LAHERRADURA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $LAHERRADURA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 2</h1>
<div class="card-body">
<h4 class="card-title">Central Jaguas</h4>
<?php
if ($JAGUAS > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $JAGUAS . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 3</h1>
<div class="card-body">
<h4 class="card-title">Central San Carlos</h4>
<?php
if ($SANCARLOS > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $SANCARLOS . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 4</h1>
<div class="card-body">
<h4 class="card-title">Hidrosogamoso</h4>
<?php
if ($SOGAMOSO > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $SOGAMOSO . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 5</h1>
<div class="card-body">
<h4 class="card-title">Amoya la esperanza</h4>
<?php
if ($AMOYALAESPERANZA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $AMOYALAESPERANZA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 6</h1>
<div class="card-body">
<h4 class="card-title">Miel I</h4>
<?php
if ($MIELI > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $MIELI . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 7</h1>
<div class="card-body">
<h4 class="card-title">Calderas</h4>
<?php
if ($CALDERAS > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $CALDERAS . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 8</h1>
<div class="card-body">
<h4 class="card-title">Guavio</h4>
<?php
if ($GUAVIO > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $GUAVIO . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 9</h1>
<div class="card-body">
<h4 class="card-title">Represa Betania</h4>
<?php
if ($BETANIA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $BETANIA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 10</h1>
<div class="card-body">
<h4 class="card-title">El Quimbo</h4>
<?php
if ($ELQUIMBO > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $ELQUIMBO . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 11</h1>
<div class="card-body">
<h4 class="card-title">Paraiso</h4>
<?php
if ($PARAISO > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $PARAISO . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 12</h1>
<div class="card-body">
<h4 class="card-title">Guaca</h4>
<?php
if ($LAGUACA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $LAGUACA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 13</h1>
<div class="card-body">
<h4 class="card-title">Tequendama</h4>
<?php
if ($TEQUENDAMA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $TEQUENDAMA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 14</h1>
<div class="card-body">
<h4 class="card-title">La Tasajera</h4>
<?php
if ($LATASAJERA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $LATASAJERA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 15</h1>
<div class="card-body">
<h4 class="card-title">Caracoli</h4>
<?php
if ($CARACOLI > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $CARACOLI . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 16</h1>
<div class="card-body">
<h4 class="card-title">Limonar</h4>
<?php
if ($ELLIMONAR > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $ELLIMONAR . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 17</h1>
<div class="card-body">
<h4 class="card-title">Dario Valencia</h4>
<?php
if ($DARIOVALENCIASAMPER > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $DARIOVALENCIASAMPER . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 18</h1>
<div class="card-body">
<h4 class="card-title">Laguneta</h4>
<?php
if ($LAGUNETA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $LAGUNETA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 19</h1>
<div class="card-body">
<h4 class="card-title">Minicentral Pajarito</h4>
<?php
if ($PAJARITO > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $PAJARITO . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 20</h1>
<div class="card-body">
<h4 class="card-title">Minicentral San Jose de la Montaña</h4>
<?php
if ($SANJOSEDELAMONTANA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $SANJOSEDELAMONTANA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 21</h1>
<div class="card-body">
<h4 class="card-title">Troneras</h4>
<?php
if ($TRONERAS > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $TRONERAS . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 22</h1>
<div class="card-body">
<h4 class="card-title">Guadalupe III</h4>
<?php
if ($GUADALUPE3 > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $GUADALUPE3 . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 23</h1>
<div class="card-body">
<h4 class="card-title">Guadalupe IV</h4>
<?php
if ($GUADALUPE4 > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $GUADALUPE4 . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 24</h1>
<div class="card-body">
<h4 class="card-title">Porce II</h4>
<?php
if ($PORCEII > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $PORCEII . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 25</h1>
<div class="card-body">
<h4 class="card-title">Porce III</h4>
<?php
if ($PORCEIII > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $PORCEIII . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 26</h1>
<div class="card-body">
<h4 class="card-title">Guatape</h4>
<?php
if ($GUATAPE > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $GUATAPE . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 27</h1>
<div class="card-body">
<h4 class="card-title">Rio Abajo</h4>
<?php
if ($RIOABAJO > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $RIOABAJO . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 28</h1>
<div class="card-body">
<h4 class="card-title">Sonson</h4>
<?php
if ($SONSON > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $SONSON . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 29</h1>
<div class="card-body">
<h4 class="card-title">Tamesis</h4>
<?php
if ($RIOFRIOTAMESIS > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $RIOFRIOTAMESIS . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 30</h1>
<div class="card-body">
<h4 class="card-title">Ayura</h4>
<?php
if ($AYURA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $AYURA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 31</h1>
<div class="card-body">
<h4 class="card-title">Niquia</h4>
<?php
if ($NIQUIA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $NIQUIA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 32</h1>
<div class="card-body">
<h4 class="card-title">Urra I</h4>
<?php
if ($URRA1 > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $URRA1 . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 33</h1>
<div class="card-body">
<h4 class="card-title">Chivor</h4>
<?php
if ($CHIVOR > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $CHIVOR . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 34</h1>
<div class="card-body">
<h4 class="card-title">Cucuana</h4>
<?php
if ($CUCUANA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $CUCUANA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>



<li>
<div class="card col-xl-2 changing">
<h1 class="card-header">H 35</h1>
<div class="card-body">
<h4 class="card-title">Calima</h4>
<?php
if ($CALIMA > 0) {
echo("<p class=\"card-text\">En funcionamiento</p>");
echo("<p class=\"btn btn-primary\">" . $CALIMA . " MWh </p>");
}
else {
echo("<p class=\"card-text\">No está en funcionamiento</p>");
}
?>
</div>
</div>
</li>
        
</ul>
    
    
    <script src="../js/execute.js"></script>
    <script src="../js/popper.js"></script>
    <script src="../bootstrap-4.0.0-dist/js/bootstrap.js"></script>
    
</body>

</html>