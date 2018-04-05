<h2>Tugas 5</h2>
<h4>Membuat Peta Multiple Layer</h4>
<ul>
 	<li>Mendownload data ESRI Shapefiles negara Belanda pada situs <a title="Shapefiles Netherlands" href="diva-gis.org/gdata" target="_blank" rel="noopener">DIVA-GIS</a></li>
 	<li >Mendonwload shapefile adm0, adm1, adm2, road dan rails (5 Layer)</li>
 	<li>Menerapkan layer1 dari shapefile adm0 sebagai base polygon negara Belanda</li>
 	<li>Menearapkan layer2 dari shapefile adm1 dan memfilter wilayah berair dan bersungai</li>
 	<li>Menerapkan layer3 dari shapefile adm2 dan menandai ibukota negara Belanda -&gt; Amsterdam</li>
 	<li>Menerapkan layer4 dari shapefile roads untuk menggambar jalan raya</li>
 	<li>Merapkan layer5 dari shapefile rails untuk menggambar rute rel kereta api</li>
</ul>
Kendala : memberi batas wilayah sesuai provinsi belum berhasil karena kombinasi sintaks Expression masih salah
<h4>Membuat Poin Symbolizer pada Peta</h4>
<ul>
 	<li>Mendownload data ESRI shapefiles Kecamatan Indonesia dari <a title="Shapefile Kecamatan Indonesia" href="http://www.info-geospasial.com/2015/10/data-shp-seluruh-indonesia.html" target="_blank" rel="noopener">sini</a>.</li>
 	<li>Membuat Layer1 kecamatan Indonesia tanpa garis tepi</li>
 	<li>Menyalin koordinat Pantai Kenjeran dari GoogleMaps dan diletakkan pada MapDatasource class Feature POINT</li>
 <li>Mendownload icon pantai untuk map <a title="Icon Pantai" href="https://www.flaticon.com/free-icon/beach_272859#term=tourism&page=1&position=61" target="_blank" rel="noopener">di sini</a></li>
 <li>Penulisan koordinat di POINT pada tugas dibalik dari koordinat dari yang diambil pada GoogleMaps</li>
</ul>
Kendala : TextSymbolizer tidak muncul, Attribut sudah disesuaikan dengan data shapefile yaitu 'Kecamatan' namun tidak bisa muncul di peta
