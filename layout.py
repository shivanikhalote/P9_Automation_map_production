import arcpy
pro_project_path = r"C:\Users\shiva\Downloads\Arcpy_9_data\Assignment_9_ProProject\MyProject.aprx"
my_project = arcpy.mp.ArcGISProject(pro_project_path)
layout_list = my_project.listLayouts()

for layout in layout_list:
    print('layout name : {}'.format(layout.name))
    layout.exportToPNG(r"C:\Users\shiva\Downloads\wilson\wilson_layout.png")
    print("completed")





