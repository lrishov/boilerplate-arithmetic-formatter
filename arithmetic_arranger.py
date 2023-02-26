def arithmetic_arranger(problems, results = False):
    if len(problems) > 5:
        return "Error: Too many problems."
    problems = [x.split(" ") for x in problems]
    for x in problems:
        if x[1] not in {'+','-'}:
            return "Error: Operator must be '+' or '-'."
        if not (x[0].isdigit() and x[2].isdigit()):
            return "Error: Numbers must only contain digits."
        if (len(x[0]) > 4 or len(x[2]) > 4):
            return "Error: Numbers cannot be more than four digits."
    if results == True:
        lines = [""] * 4
        ops = {"+": (lambda x,y: int(x) + int(y)), "-": (lambda x,y: int(x) - int(y))}
    else:
        lines = [""] * 3
    for x in problems:
        lines[0] = lines[0] + " " * (max(len(x[0]), len(x[2])) - len(x[0]) + 2) + x[0] + "    "
        lines[1] = lines[1] + x[1] + " " * (max(len(x[0]), len(x[2])) - len(x[2]) + 1) + x[2] + "    "
        lines[2] = lines[2] + "-" * (max(len(x[0]), len(x[2])) + 2) + "    "
        if results == True:
            y = str(ops[x[1]] (x[0], x[2]))
            lines[3] = lines[3] + " " * (max(len(x[0]), len(x[2]))+ 2 - len(y)) + y + "    "
    lines = [x[:-4] for x in lines]
    return "\n".join(lines)
