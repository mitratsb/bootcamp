# dict1={'pkg1': ['pkg3'], 'pkg2':['pkg3'], 'pkg3': [], 'pkg4':['pkg1', 'pkg2']}

def sort_dependencies(packages, package_name):
    package_dependencies = []
    # global dict1
    # packages=dict1
    if len(packages[package_name])!=0 :
        for v in packages[package_name]:
            if len(packages[v])!=0 :
                a=packages[v]
                packages[package_name] = a + packages[package_name]
        return list(dict.fromkeys(packages[package_name]))
        # return packages[package_name]
    else:
        return package_dependencies

    
# print(sort_dependencies(dict1 , "pkg4"))