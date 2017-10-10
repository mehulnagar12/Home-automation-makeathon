#Read and write serial data with Arduino

"""
Data receive format:
data = {
    led: {
        1: 1/0,
        2: 1/0,
        3: 1/0,
        4: 1/0,
        5: 1/0
    },
    temperature: room_temp_celsius,
    smoke: 1/0,
    security: 1/0
}
Data send format:
data = {
    led: {
        1: 1/0,
        2: 1/0,
        3: 1/0,
        4: 1/0,
        5: 1/0
    },
    IR: ir_value
}
"""
testdata={}
testdata["led"] = {}
testdata["led"][1] = 0
testdata["led"][2] = 0
testdata["led"][3] = 1
testdata["led"][4] = 1
testdata["led"][5] = 0
testdata["temperature"] = 22
testdata["smoke"] = 0
testdata["security"] = 1

def read():
    return testdata

def write(data):
    print("WRITTEN")
