import mapnik

#Membuat Map
m = mapnik.Map(6024,2480, '+init=epsg:4326')
m.background = mapnik.Color('steelblue')

#------------------------Layer1 Surabaya----------------------#
#Membuat lapisan
layer_sby = mapnik.Layer('SurabayaLayer1', '+init=epsg:4326')
layer_sby.datasource = mapnik.Shapefile(file='../Tugas 4/peta kecamatan indonesia/INDONESIA_KEC.shp') #mengambil lapisan dari sumber data

#Membuat Style
ssby = mapnik.Style()


#Membuat poligon area
rsby = mapnik.Rule()
polygon_sby = mapnik.PolygonSymbolizer(mapnik.Color(217, 235, 203))
rsby.symbols.append(polygon_sby) #membuat rule polygon indonesia

#Menggambar garis tepi
#line_sby = mapnik.LineSymbolizer()
#line_sby = mapnik.LineSymbolizer(mapnik.Color('grey'),1)
#line_sby.stroke_width = 2.0
#rsby.symbols.append(line_sby) #menerapkan garis tepi ke rule map

#Poin wisata
ssby_wisata = mapnik.Style()
rsby_wisata = mapnik.Rule()
poin_wisata = mapnik.MarkersSymbolizer()
poin_wisata.filename = 'beach.png'
poin_wisata.width = mapnik.Expression('20')
poin_wisata.height = mapnik.Expression('20')
poin_wisata.allow_overlap = True
rsby_wisata.symbols.append(poin_wisata) #membuat rule poin_wisata

label = mapnik.TextSymbolizer(mapnik.Expression('[Kecamatan]'), 'DejaVu Sans Book',5,mapnik.Color('Red'
	))
label.halo_radius = 1
label.avoid_edges = False
rsby_wisata.symbols.append(label) #membuat rule label

#Membuat Layer Tempat Wisata
layer_wisata = mapnik.Layer('Wisata', '+init=epsg:4326')
ds = mapnik.MemoryDatasource()
layer_wisata.datasource = ds
fitur_wisata = mapnik.Feature(mapnik.Context(),1)
fitur_wisata['Kecamatan'] = 'Kenjeran'
fitur_wisata.add_geometries_from_wkt("POINT(112.7078354 -7.260369)")
ds.add_feature(fitur_wisata)
#layer_wisata.srs = longlat.params()

#Menerapkan rule-rule yang ada ke style yang telah dibuat
ssby.rules.append(rsby)
ssby_wisata.rules.append(rsby_wisata) 

#Menerapkan Style utama ke peta yang telah dibuat
m.append_style('StyleLayerSby',ssby) #memberi nama Style
m.append_style('PoinWisata', ssby_wisata) #memberinama style poinwisata
layer_sby.styles.append('StyleLayerSby') #meletakkan style sby ke dalam layer_sby
layer_wisata.styles.append('PoinWisata') #meletakkan style wisata ke dalam layer_wisata
m.layers.append(layer_sby) #meletakkan layer Surabaya ke dalam peta
m.layers.append(layer_wisata) #meletakkan layer wisata ke dalam peta
#-------------------------End Layer1 Surabaya----------------------------------#

#Mempersiapkan semua layer ke map
m.zoom_all()

#render gambar
mapnik.render_to_file(m,'Pantai Kenjeran Surabaya.pdf', 'pdf')
print "Sukses merender file 'Pantai Kenjeran Surabaya.pdf'"