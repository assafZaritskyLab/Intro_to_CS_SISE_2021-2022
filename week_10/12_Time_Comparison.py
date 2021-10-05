
from week_10.Linked_List import Linked_List
import timeit


# Time comparison
big_link_lst = Linked_List()
for i in range(100):
    big_link_lst.add_at_start(i)

start = timeit.default_timer()
rec_accumulated_lst = big_link_lst.accumulated_rec()
stop = timeit.default_timer()
rec_time = stop - start
print('Time: ', rec_time)

start = timeit.default_timer()
iter_acc_lst = big_link_lst.accumulated_iter()
stop = timeit.default_timer()
iter_time = stop - start
print('Time: ', iter_time)
print('Recursion was', int(iter_time / rec_time), 'times faster!')