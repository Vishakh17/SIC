x={"a":{"python":10,"java":20},"b":30,"c":40}
import copy
y=copy.deepcopy(x)
y["a"]["python"]=100
print(x)
print(y)