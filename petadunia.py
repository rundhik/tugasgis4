import mapnik

## PETA DUNIA ##
m = mapnik.Map(1080,640)
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
kec = mapnik.Map(1080,640)
kec.background = mapnik.Color('steelblue')
skec = mapnik.Style()
rkec = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
rkec.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('green')
line_symbolizer.stroke_width = 2.0

rkec.symbols.append(line_symbolizer)
skec.rules.append(rkec)
kec.append_style('LayerKecIndo',skec)
sumberdatakec = mapnik.Shapefile(file="peta dunia/ne_110m_admin_0_countries.shp")
lapisankec = mapnik.Layer('world')
lapisankec.datasource = sumberdatakec
lapisankec.styles.append('LayerKecIndo')
kec.layers.append(lapisan)
kec.zoom_all()
mapnik.render_to_file(kec,'Peta Kecamatan Indonesia.png', 'png')
print "rendered image to 'Peta Kecamatan Indonesia.png'"
