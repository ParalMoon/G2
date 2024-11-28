using PyCall
np = pyimport("numpy")

a = np.array([1,2])
b = np.array([2,3])
c = np.dot(a,b)

println(c)

```
ENV["PYTHON"] = "/home/codespace/.python/current/bin/python3"
using Pkg
Pkg.build("PyCall")
```

