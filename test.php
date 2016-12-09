<?php
//require
require_once('phpQuery-onefile.php');

//get a page
$html = file_get_contents('http://chiebukuro.yahooapis.jp/Chiebukuro/V1/questionSearch?appid=<アプリケーションID>&query=apple&condition=solved');

//DOM取得
$doc = phpQuery::newDocument($html);

//要素取得
echo $doc["Content"]->text();
echo $doc["BestAnswer"]->text();

?>
