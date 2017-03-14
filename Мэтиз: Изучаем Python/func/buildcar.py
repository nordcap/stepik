def build_car(name, builder, **info):
    profile = {}
    profile['name'] = name
    profile['builder'] = builder
    for key, value in info.items():
        profile[key] = value
    return profile