def create_access_table(fanout):
    """
        Create access table ungracefully, because silent hosts can't be found in Hedera.
        In fact, this should be done automatically. (hmc)
        self.access_table = {(sw,port):(ip, mac),}
    """
    table = {}
    num = 1
    k = 1
    for i in xrange(3001, 3001 + (fanout ** 2) / 2):
        for j in xrange(fanout / 2 + 1, fanout + 1):
            table[(i, j)] = ('10.%d.0.%d' % (int(str(i)[-2:]), k), '00:00:00:00:00:%02x' % num)
            num += 1
            k += 1
            if k == fanout / 2 + 1:
                k = 1
    return table

table =  create_access_table(4)

for x in table.keys():
    print x,table[x]