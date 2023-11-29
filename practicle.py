import arcpy
pro_project_path = r"C:\Users\shiva\Downloads\Arcpy_9_data\Assignment_9_ProProject\MyProject.aprx"

my_project = arcpy.mp.ArcGISProject(pro_project_path)
map_list = my_project.listMaps()
for map in map_list:
    print('Map Name : {}'.format(map.name))
    lyr_list = map.listLayers()
    print('layers inside {}'.format(map.name))
    for lyr in lyr_list:
        print(lyr.name)
    print('\n')


    