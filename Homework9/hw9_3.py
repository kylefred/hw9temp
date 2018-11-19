import pandas
import numpy

numpy.random.seed(0)

data = numpy.random.rand(20, 5)
df = pandas.DataFrame(data = data, columns = ['Col1','Col2','Col3','Col4','Col5'])

print(df.mean())
