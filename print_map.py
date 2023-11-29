import arcpy
pro_project_path = r"C:\Users\shiva\Documents\ArcGIS\Projects\Automatic_map_production\Automatic_map_production.aprx"

my_project = arcpy.mp.ArcGISProject(pro_project_path)
map_list = my_project.listMaps()
for map in map_list:
    print(map.name)
    if map.name == "Current":
        lyr_list = map.listLayers()
        for lyr in lyr_list:
            print(lyr.name)

layout_list =  my_project.listLayouts()

for layout in layout_list:
    if layout.name == "Layout":
        output_path = r"C:\Users\shiva\Downloads\ProProject_Mapping\san_diego.pdf"
        layout.exportToPDF(output_path)
    print("completed")