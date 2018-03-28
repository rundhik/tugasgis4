# tugasgis4
Tugas GIS Minggu ke 4<br/>

Logbook :<br/>

OS yang digunakan : Ubuntu Linux 16.04 LTS<br/>
Versi Python : 2.7.12<br/>
Versi Mapnik : 2.2.0<br/>

Problem :<br/>
a) intalasi environtment mapnik pada linux mengalami kendala ketika menginstall packages libmapnik <br/>
b) coding rendering warna pada linux dan windows berbeda<br/>
c) mengatur ketebalan stroke shape file tidak memberikan efek, contoh : line_symbolizer.stroke_width = 10<br/>


Solution :<br/>
a) langsung menginstall paket libmapnik-dev, ditambah paket python-mapnik dan mapnik-utils<br/>
b) di linux langsung menggunakan syntax : mapnik.Color('value') , contoh value : white, green, red dsb<br/>
c) menggunakan float numbering (desimal), contoh : line_symbolizer.stroke_width = 10.0<br/>

