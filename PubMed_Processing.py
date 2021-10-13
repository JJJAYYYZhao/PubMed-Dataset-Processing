
import pickle as pkl
def load_cora():
    names = ['x']
    with open("F:/焦糖/PubMed/ind.pubmed.ty", 'rb') as f:
            data = pkl.load(f, encoding='latin1')
            #print(data.shape)   #(18717, 500)-ind.pubmed.allx是18717行，500列,有500个特征
            #print(data)
            #n=data.todense()
            m=data.tolist()
            
  # 变量data是个scipy.sparse.csr.csr_matrix，类似稀疏矩阵，输出得到的是矩阵中非0的行列坐标及值
            
            #nonzero=data.nonzero()
            #print(nonzero[1]) 
            #m=nonzero[1].tolist()
            #print(m)
            #输出非零元素对应的行坐标和列坐标
# (array([  0,   0,   0, ..., 139, 139, 139], dtype=int32), array([  19,   81,  146, ..., 1263, 1274, 1393], dtype=int32))
            # nonzero是个tuple
            
            with open("F:/焦糖/dataset/pubmed2.txt",'w') as out_file:
                for i in range(len(m)):
                   out_file.write(str(m[i])+"\n")
                   
            
            #print(data.toarray())
# [[0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  ...
#  [0. 0. 0. ... 0. 1. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 1. 0. ... 0. 0. 0.]]

load_cora()