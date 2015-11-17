import numpy as np

def write_sparse_to_text(data, filepath):
    # data is scipy.sparse.lil_matrix, with target as first entry)
    f = open(filepath, 'wb')
    for row in data:
        ind = row.rows
        vals = row.data
        target = vals[0][0]
        entries = ["{}:{}".format(int(i), v) for (i, v) in zip(ind[0][1:], vals[0][1:]) if not np.isnan(v)]
        line = ' '.join([str(target)] + entries)
        line += '\n'
        f.write(line)
    f.close()
