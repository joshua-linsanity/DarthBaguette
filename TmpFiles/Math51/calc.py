import numpy as np

v1 = np.array([1,0,0,])
v2 = np.array([0,1,0,])
v3 = np.array([0,0,1,])

v_list = np.array([v1,v2,v3])

w1 = np.array([1,-2,2])
w2 = np.array([2,2,1])
w3 = np.array([-2,1,2])

w_list = np.array([w1,w2,w3])

for v in v_list:
    print("v = ", v)
    for w in w_list:
        print("coefficient = ", np.dot(v,w) / np.linalg.norm(w)**2)

