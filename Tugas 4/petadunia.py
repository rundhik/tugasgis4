import mapnik

## PETA DUNIA ##
m = mapnik.Map(1366,768)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('green')
line_symbolizer.stroke_width = 2.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('PunyaSaya',s)
sumberdata = mapnik.Shapefile(file="peta dunia/ne_110m_admin_0_countries.shp")
lapisan = mapnik.Layer('world')
lapisan.datasource = sumberdata
lapisan.styles.append('PunyaSaya')
m.layers.append(lapisan)
m.zoom_all()
mapnik.render_to_file(m,'petadunia.png', 'png')
print "rendered image to 'petadunia.png'"

## PETA KECAMATAN INDONESIA ##
kec = mapnik.Map(1366,768)
kec.background = mapnik.Color('steelblue')
skec = mapnik.Style()
rkec = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
rkec.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('green')
line_symbolizer.stroke_width = 0.5

rkec.symbols.append(line_symbolizer)
skec.rules.append(rkec)
kec.append_style('LayerKecIndo',skec)
sumberdatakec = mapnik.Shapefile(file="peta kecamatan indonesia/INDONESIA_KEC.shp")
lapisankec = mapnik.Layer('kecamatan')
lapisankec.datasource = sumberdatakec
lapisankec.styles.append('LayerKecIndo')
kec.layers.append(lapisankec)
kec.zoom_all()
mapnik.render_to_file(kec,'Peta Kecamatan Indonesia.png', 'png')
print "rendered image to 'Peta Kecamatan Indonesia.png'"

## PETA SUNGAI INDONESIA ##
## Menumpuk peta kecamatan yang dibuat sebelumnya dengan peta sungai, peta sungai ditandai dengan warna merah ##

sungai = mapnik.Map(1366,768)
sungai.background = mapnik.Color('steelblue')
stysungai = mapnik.Style()
rulsungai = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
rulsungai.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('red')
line_symbolizer.stroke_width = 0.5

##menerapkan layer kecamatan ke style sungai yang barusan dibuat ##
##karena kecamatan ada di lapisan bawah, maka di append terlebih dahulu ke sungai.layers ##
stysungai.rules.append(rkec)
sungai.append_style('LayerKecIndo',stysungai)
lapsungai = mapnik.Layer('kecamatan')
lapsungai.styles.append('LayerKecIndo')
sungai.layers.append(lapisankec)

##generate lapisan sungai ke style sungai##
rulsungai.symbols.append(line_symbolizer)
stysungai.rules.append(rulsungai)
sungai.append_style('LayerSungaiIndo',stysungai)
sbrdtasungai = mapnik.Shapefile(file="peta sungai indonesia/IND_SNG_polyline.shp")
lapsungai = mapnik.Layer('sungai')
lapsungai.datasource = sbrdtasungai
lapsungai.styles.append('LayerSungaiIndo')
sungai.layers.append(lapsungai)
sungai.zoom_all()
mapnik.render_to_file(sungai,'Peta Sungai Indonesia.png', 'png')
print "rendered image to 'Peta Sungai Indonesia.png'"
