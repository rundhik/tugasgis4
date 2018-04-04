import mapnik

#Membuat Map
m = mapnik.Map(1308,864)
m.background = mapnik.Color('steelblue')

#------------------------Layer1 Surabaya----------------------#
#Membuat lapisan
layer_sby = mapnik.Layer('SurabayaLayer1')
layer_sby.datasource = mapnik.Shapefile(file='../Tugas 4/peta kecamatan indonesia/INDONESIA_KEC.shp')#mengambil lapisan dari sumber data

#Membuat Style
ssby = mapnik.Style()
rsby = mapnik.Rule()

#Membuat poligon area
polygon_sby = mapnik.PolygonSymbolizer(mapnik.Color(217, 235, 203))
rsby.symbols.append(polygon_sby) #menerapkan simbol poligon ke rule map

#Menggambar garis tepi
#line_sby = mapnik.LineSymbolizer()
#line_sby = mapnik.LineSymbolizer(mapnik.Color('grey'),1)
#line_sby.stroke_width = 2.0
#rsby.symbols.append(line_sby) #menerapkan garis tepi ke rule map

#Poin wisata
rsby_wisata = mapnik.Rule()
poin_wisata = mapnik.MarkerSymbolizer()
poin_wisata.filename = 'beach.png'
poin_wisata.allow_overlap = True
rsby_wisata.symbols.append(poin_wisata)

label = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'), 'DejaVu Sans Book',5,mapnik.Color('Red'
	))
label.halo_radius = 1
label.avoid_edges = False
rsby_wisata.append(label)



#Menerapkan rule-rule yang ada ke style yang telah dibuat
ssby.rules.append(rsby)

#Menerapkan style ke peta yang telah dibuat
m.append_style('Layer1',ssby)


layer_sby.styles.append('Layer1') #menerapkan lapisan yang barusan dibuat dengan nama Layer1
m.layers.append(layer_sby)
#-------------------------End Layer1 Surabaya----------------------------------#



#Mempersiapkan semua layer ke map
m.zoom_all()

#render gambar
mapnik.render_to_file(m,'Surabaya.pdf', 'pdf')
print "Sukses merender file 'Surabaya.pdf'"