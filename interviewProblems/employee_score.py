'''Google uses FTE short for Full Time Employee. The FTE Score for an FTE equals "Total number of direct and indirect FTEs report to the FTE, then plus 1. The 'plus one' here means adding the FTE itself as self-reporting.

An FTE without any other FTEs reporting to it, will has FTE Score 1.

Each FTE has unique eid (employee_id). Given a direct report map, where key is an eid, value is an array of eids who directly report to key. This map should contain all employees.

Here is an example of direct report map:
empl_dict = {'123': ['234', '345'],
  '234': ['456', '789'], 
  '345':[],
  '456':[],
  '789':[]}

Invalid cases:
Value not in key
Value = None
Duplicate keys
Multiple managers
Manager reports to person they manage

     4  ← CEO
  2      3
3          
Given id calculate score
Memory = {}


def calculate_employee_score(emp_dict, emp_id)
	# input validation
score_queue = [emp_id]
score = 0
	While len(score_queue) > 0:
		cur_id = score_queue.pop(0)
		score += 1
		score_queue.extend(emp_dict[cur_id])
	# add to memory
return score



('123') ⇒ 5
'''

class empl_tree:
    def __init__(self, input_value, children=[]):
        self.val = input_value
        self.children = children

memory = {}
empl_dict = {'123':['234', '345'],
    '234': ['456', '789'], 
    '345':[],
    '456':[],
    '789':[]}

def calculate_employee_score(emp_dict, emp_id):
	# input validation
    if emp_id in memory: return memory[emp_id]

    score_queue = [emp_id]
    score = 0
    while len(score_queue) > 0:
        cur_id = score_queue.pop(0)
        score += 1
        score_queue.extend(emp_dict[cur_id])
    # add to memory
    memory[emp_id] = score
    return score

def calculate_employee_score_recurse(emp_dict,emp_id, memory = {}):
    if emp_id in memory: return memory[emp_id]
    score = 1

    if emp_id not in emp_dict:
        return 0        
    elif len(empl_dict[emp_id]) > 0:
        for r in empl_dict[emp_id]:
            score += calculate_employee_score_recurse(emp_dict, r, memory)
    
    memory[emp_id] = score
    return score

def calculate_employee_score_tree(ex_tree, emp_id, memory={}):
    if emp_id in memory: return memory[emp_id]
    score = 1

    if len(ex_tree.children) > 0:
        for r in ex_tree.children:
            score += calculate_employee_score_tree(r, r.val, memory)

    memory[emp_id] = score
    return score




if __name__ == "__main__":

    # print(calculate_employee_score_recurse(empl_dict, '123'))
    # print(calculate_employee_score_recurse(empl_dict, '234'))
    # print(calculate_employee_score_recurse(empl_dict, '345'))
    # print(calculate_employee_score_recurse(empl_dict, '456'))


    my_tree = empl_tree("123", 
        [empl_tree("234",
            [empl_tree("456"),empl_tree("789")]), 
        empl_tree("345")])
        
    print(calculate_employee_score_tree(my_tree, '123'))
    print(calculate_employee_score_tree(my_tree, '234'))
    print(calculate_employee_score_tree(my_tree, '345'))
    print(calculate_employee_score_tree(my_tree, '456'))
    print(calculate_employee_score_tree(my_tree, '567'))

    