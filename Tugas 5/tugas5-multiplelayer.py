import mapnik

#Membuat Map
m = mapnik.Map(1308,1024)
m.background = mapnik.Color('steelblue')

#------------------------Layer1 Belanda----------------------#
#Membuat lapisan
layer_adm0 = mapnik.Layer('BelandaLayer1')
layer_adm0.datasource = mapnik.Shapefile(file='shapefiles/NLD_adm0.shp')#mengambil lapisan dari sumber data

#Membuat Style
sadm0 = mapnik.Style()
radm0 = mapnik.Rule()

#Membuat poligon area
polygon_adm0 = mapnik.PolygonSymbolizer(mapnik.Color(217, 235, 203))
radm0.symbols.append(polygon_adm0) #menerapkan simbol poligon ke rule map

#Menggambar garis tepi
line_adm0 = mapnik.LineSymbolizer()
line_adm0 = mapnik.LineSymbolizer(mapnik.Color('grey'),1)
line_adm0.stroke_width = 0.5
radm0.symbols.append(line_adm0) #menerapkan garis tepi ke rule map

#Menerapkan rule-rule yang ada ke style yang telah dibuat
sadm0.rules.append(radm0)

#Menerapkan style ke peta yang telah dibuat
m.append_style('Layer1',sadm0)


layer_adm0.styles.append('Layer1') #menerapkan lapisan yang barusan dibuat dengan nama Layer1
m.layers.append(layer_adm0)
#-------------------------End Layer1 Belanda----------------------------------#

#------------------------Layer2 Belanda----------------------#
#Membuat lapisan
layer_adm1 = mapnik.Layer('BelandaLayer2')
layer_adm1.datasource = mapnik.Shapefile(file='shapefiles/NLD_adm1.shp')


#Membuat Style 
style_adm1 = mapnik.Style()
rule_adm1 = mapnik.Rule()
#Membuat poligon area 
#rule_adm1.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color(250, 190, 183))) #pink
#style_adm1.rules.append(rule_adm1)

#Membuat waterbody
rule_adm1_waterbody = mapnik.Rule()
rule_adm1_waterbody.filter = mapnik.Expression("[TYPE_1]='Water body'")
polygon_adm1_waterbody = mapnik.PolygonSymbolizer(mapnik.Color('steelblue')) #ijomuda
polygon_adm1_waterbody.smooth = 1.0
rule_adm1_waterbody.symbols.append(polygon_adm1_waterbody)
style_adm1.rules.append(rule_adm1_waterbody) #menerapkan rule waterbody ke style
#Menerapkan style ke peta yang telah dibuat
m.append_style('Layer2',style_adm1)
layer_adm1.styles.append('Layer2') #menerapkan lapisan yang barusan dibuat dengan nama Layer2
m.layers.append(layer_adm1)

layer_air = mapnik.Layer('BelandaLayer2a')
layer_air.datasource = mapnik.Shapefile(file='shapefiles/NLD_water_areas_dcw.shp')


#Membuat Style 
style_air = mapnik.Style()
rule_air = mapnik.Rule()
#Membuat poligon area 
rule_air.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('steelblue')))
style_air.rules.append(rule_air)

m.append_style('Layer2a',style_air)
layer_air.styles.append('Layer2a') #menerapkan lapisan yang barusan dibuat dengan nama Layer2a
m.layers.append(layer_air)
#-------------------------End Layer2 Belanda----------------------------------#

#------------------------Layer3 Belanda----------------------#

#Membuat lapisan
layer_adm2 = mapnik.Layer('BelandaLayer3')
layer_adm2.datasource = mapnik.Shapefile(file='shapefiles/NLD_adm2.shp') #mengambil lapisan dari sumber data
#Membuat Style
style_adm2 = mapnik.Style()
rule_adm2 = mapnik.Rule()
#Menggambar garis tepi
line_adm2 = mapnik.Stroke()
line_adm2.add_dash(2,2)
#line_adm2.add_dash(2,2)
line_adm2.color = mapnik.Color('black')
line_adm2.width = 1.0
rule_adm2.symbols.append(mapnik.LineSymbolizer(line_adm2)) #menerapkan garis tepi ke rule map

#Menerapkan rule-rule yang ada ke style yang telah dibuat
style_adm2.rules.append(rule_adm2)

#Menandai ibukota
rule_ibukota = mapnik.Rule()
rule_ibukota.filter = mapnik.Expression("[NAME_2]='Amsterdam'")
rule_ibukota.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color('yellow')))
style_adm2.rules.append(rule_ibukota)
#Menerapkan style ke peta yang telah dibuat
m.append_style('Layer3',style_adm2)

layer_adm2.styles.append('Layer3') #menerapkan lapisan yang barusan dibuat dengan nama Layer4
m.layers.append(layer_adm2)
#-------------------------End Layer3 Belanda----------------------------------#

#------------------------Layer4 Belanda----------------------#

#Membuat lapisan
layer_jalan = mapnik.Layer('BelandaLayer4')
layer_jalan.datasource = mapnik.Shapefile(file='shapefiles/NLD_roads.shp') #mengambil lapisan dari sumber data
#Membuat Style
style_jalan = mapnik.Style()
rule_jalan = mapnik.Rule()
#Menggambar garis tepi
line_jalan = mapnik.Stroke()
line_jalan.color = mapnik.Color(171,158,137)
line_jalan.line_cap = mapnik.line_cap.ROUND_CAP
rule_jalan.symbols.append(mapnik.LineSymbolizer(line_jalan)) #menerapkan garis tepi ke rule map

#Menerapkan rule-rule yang ada ke style yang telah dibuat
style_jalan.rules.append(rule_jalan)

#Menerapkan style ke peta yang telah dibuat
m.append_style('Layer4',style_jalan)

layer_jalan.styles.append('Layer4') #menerapkan lapisan yang barusan dibuat dengan nama Layer4
m.layers.append(layer_jalan)
#-------------------------End Layer4 Belanda----------------------------------#

#------------------------Layer5 Belanda----------------------#

#Membuat lapisan
layer_rel = mapnik.Layer('BelandaLayer5')
layer_rel.datasource = mapnik.Shapefile(file='shapefiles/NLD_rails.shp') #mengambil lapisan dari sumber data
#Membuat Style
style_rel = mapnik.Style()
rule_rel = mapnik.Rule()
#Menggambar garis tepi
line_rel = mapnik.Stroke()
line_rel.color = mapnik.Color('purple')
line_rel.line_cap = mapnik.line_cap.ROUND_CAP
rule_rel.symbols.append(mapnik.LineSymbolizer(line_rel)) #menerapkan garis tepi ke rule map

#Menerapkan rule-rule yang ada ke style yang telah dibuat
style_rel.rules.append(rule_rel)

#Menerapkan style ke peta yang telah dibuat
m.append_style('Layer5',style_rel)

layer_rel.styles.append('Layer5') #menerapkan lapisan yang barusan dibuat dengan nama Layer5
m.layers.append(layer_rel)
#-------------------------End Layer5 Belanda----------------------------------#

#Mempersiapkan semua layer ke map
m.zoom_all()

#render gambar
mapnik.render_to_file(m,'Belanda.pdf', 'pdf')
print "Sukses merender file 'Belanda.pdf'"