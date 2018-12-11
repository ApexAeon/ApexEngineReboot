import json, pygame, os, sys

class Resource_Manager():
    
    def __init__():
        print("Initialized Resource Manager!")
        resources = {"ERROR":#error surface}
                     
    def load_list(resource_list):
        unload_all()
        for resource_name_type_pair in resource_list:
            load_resource(resource_name_type_pair["name"], resource_name_type_pair["type"])
                     
    def get_resource(resource_name, resource_type):
        if resource_name in resources:
            return resources[resource_name][0]
        else:
            raise #stuff
            return resources["ERROR_"+resource_type] # If resource not loaded, return error placeholder
                     
    def unload_all(): # Never unload the error surface
        resources = {"ERROR":#error surface}
                     
    def load_resource(resource_name, resource_type):
        if resource_name in resources:
            raise #HELL
        else:
            try: 
                if resource_type == "JSON":
                    file_name = [os.path.join(root, name)
                            for root, dirs, files in os.walk('..')
                            for name in files
                            if name.endswith((data_name+'.json'))]
                    resources[resource_name] = json.load(file_name)
                elif resource_type == "IMAGE":
                    file_name = [os.path.join(root, name)
                            for root, dirs, files in os.walk('..')
                            for name in files
                            if name.endswith((data_name+'.png'))]
                    resources[resource_name] = pygame.image.load(file_name)
            except: #IDK
                resources[resource_name] = [resources["ERROR_"+resource_type][0], resource_type] # If file cannot be found, replace it with the error placeholder resource.
                raise #SOMETHING
                     
