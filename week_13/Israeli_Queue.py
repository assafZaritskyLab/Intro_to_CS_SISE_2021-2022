class IsraeliQueueItem:
    """ Class that represents an item in an Israeli queue"""

    def __init__(self, value, priority, group_id):
        """ Constructor """
        if not isinstance(priority, int) or not isinstance(group_id, int):
            raise TypeError('Invalid arguments types')
        if priority <= 0 or group_id <= 0:
            raise ValueError('Invalid arguments values')
        self.value = value
        self.priority = priority
        self.group_id = group_id

    def __repr__(self):
        """ Printing method """
        return "Value:" + str(self.value) + ", Priority:" + str(self.priority) + ", GroupID:" + str(self.group_id) + "."


class IsraeliQueue:
    """ Class that represents an Israeli queue"""

    def __init__(self):
        """ Constructor """
        self.content = []

    def __len__(self):
        """ Returns the number of groups in the queue"""
        return len(self.content)

    def enqueue(self, val, priority, group_id):
        """ Add an item to the queue """
        for i in range(len(self)):
            curr_group_id = self.content[i][0].group_id
            if group_id == curr_group_id:
                self.content[i].append(IsraeliQueueItem(val, priority, group_id))
                return
        self.content.append([IsraeliQueueItem(val, priority, group_id)])

    def dequeue_item(self):
        """ Take out and return the item with the highest priority """
        max_priority = 0
        item_to_remove = (0, 0)
        for group_ind in range(len(self.content)):
            for item_ind in range(len(self.content[group_ind])):
                item = self.content[group_ind][item_ind]
                if item.priority > max_priority:
                    max_priority = item.priority
                    item_to_remove = (group_ind, item_ind)
        res = self.content[item_to_remove[0]][item_to_remove[1]]
        del self.content[item_to_remove[0]][item_to_remove[1]]
        # Remove group if empty
        if len(self.content[item_to_remove[0]]) == 0:
            del self.content[item_to_remove[0]]
        return res

    def group_total_priority(self, group):
        """ Helper method - sums the priorities of all items in group """
        res = 0
        for item in group:
            res += item.priority
        return res

    def dequeue_group(self):
        """ Takes out and return the group with the highest priority of all items"""
        max_group_ind = 0
        max_group_priorities = 0
        for group_ind, group in enumerate(self.content):
            group_tot_prio = self.group_total_priority(group)
            if group_tot_prio > max_group_priorities:
                max_group_ind = group_ind
                max_group_priorities = group_tot_prio
        res = self.content[max_group_ind]
        del self.content[max_group_ind]
        return res

    def __repr__(self):
        """ Priniting method"""
        res = ''
        for group in self.content:
            res += 'Group ' + str(group[0].group_id) + ' items:\n'
            i = 1
            for item in group:
                res += str(i) + '. ' + str(item) + '\n'
                i += 1
        return res


def sort_queue_by_priorities(queue):
    """ Returns all queue's items sorted by:
    1. group_id
    2. priority
    """
    all_items = []
    for group in queue.content:
        for item in group:
            all_items.append(item)

    def comp(item):
        """ Helper function - extracts data from item (for using sorted) """
        return item.group_id, item.priority

    return sorted(all_items, key=comp)


iq = IsraeliQueue()
iq.enqueue(10, 10, 1)
iq.enqueue(20, 20, 1)
iq.enqueue(30, 30, 2)
iq.enqueue(5, 5, 2)
iq.dequeue_item()
