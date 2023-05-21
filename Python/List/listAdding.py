statesOfAmerica = ["Alabama", "Alaska", "Arizona", "Arkansas", "California",\
                    "Colorado", "Connecticut", "Delaware", "Florida"]


statesOfAmerica[-2]# - "Delaware"
statesOfAmerica.append("Georgia")# + "Georgia"
statesOfAmerica.extend(["Hawaii", "Idaho"])# + "Hawaii" + "Idaho"
statesOfAmerica.insert(0, "Iowa")# + "Iowa"
statesOfAmerica.pop(1)# - "Alabama"

numOfStates = len(statesOfAmerica)

print(statesOfAmerica[-1])#
print(statesOfAmerica[numOfStates -1])
