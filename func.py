def testfunc(name, *hobbies, **deeds):
    print(name)
    for hobby in hobbies:
        hobby = "study"
        print(hobby)
    for k, v in deeds.items():
        print(k, v)
        print(type(k))
    # hobbies[0] = "study"   this is wrong cuz hobbies is a tuple
testfunc('matrix', 'eat', 'sleep', firstdo = "born", nextdo = "sleep")