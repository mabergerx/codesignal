def solution(names):
    
    counts = {name: 1 for name in set(names)}
    
    new_names = []
    
    for name in names:
        if name not in new_names:
            new_names.append(name)
        else:
            new_name = f"{name}({counts[name]})"
            counter = 1
            while new_name in new_names:
                new_name = f"{name}({counts[name]+counter})"
                counter += 1
            new_names.append(new_name)
            counts[name] += counter
    
    return new_names