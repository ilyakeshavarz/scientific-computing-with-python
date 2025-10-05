def arithmetic_arranger(problems, show_answers=False):
    l1 = []
    l2 = []
    l3 = []
    l4 = []

    if len(problems) > 5 :
        return 'Error: Too many problems.'
    
    for problem in problems :
        nums = str(problem).split(" ")
        num1 = nums[0]
        op = nums[1]
        num2 = nums[2]

        if op not in ['+' , '-'] :
            return "Error: Operator must be '+' or '-'."
        if str(num1).isdigit() == False or str(num2).isdigit() == False :
            return 'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4 :
            return 'Error: Numbers cannot be more than four digits.'
        
        wi = max(len(num1) , len(num2)) + 2
        l1.append(num1.rjust(wi))
        l2.append(op + num2.rjust(wi -1))
        l3.append('-' * wi)

        f_num = int(num1) + int(num2)
        if show_answers :
            if op == '+' :
                f_num = int(num1) + int(num2)
            else :
                f_num = int(num1) - int(num2)
            l4.append(str(f_num).rjust(wi))
                
    a_problems = '    '.join(l1) + '\n'
    a_problems += '    '.join(l2) + '\n'
    a_problems += '    '.join(l3)

    if show_answers :
        a_problems += '\n' + '    '.join(l4)
    return a_problems
