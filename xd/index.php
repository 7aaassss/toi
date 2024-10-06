<?php
$xml = new DOMDocument;
$xml->load('library.xml');

$xsl = new DOMDocument;
$xsl->load('style.xsl');

$proc = new XSLTProcessor;
$proc->importStylesheet($xsl);

echo $proc->transformToXML($xml);
?>
