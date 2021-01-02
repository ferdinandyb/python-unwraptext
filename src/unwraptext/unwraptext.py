import re


def unwrap_markdown(text):
    """TODO: Docstring for markdown.

    :function: TODO
    :returns: TODO

    """
    outlines = []
    inblock = False
    code = False

    # split into blocks
    for line in text.split('\n'):
        if not inblock:
            if line.isspace() or line == "":
                outlines.append(line)
            elif re.search(r'\S', line).group() == "#":
                outlines.append(line)
            else:
                inblock = True
                outlines.append([line])
                if re.search(r'```', line):
                    code = True
        else:
            if code:
                outlines.append(line)
                if "```" in line:
                    inblock = False
                    code = False
            else:
                if line.isspace() or line == "":
                    outlines.append(line)
                    inblock = False
                elif re.search(r'\S', line).group() == "#":
                    outlines.append(line)
                    inblock = False
                else:
                    outlines[-1].append(line)

    for i, block in enumerate(outlines):
        if type(block) == list:
            if sum([re.search(r'\S', b).group() in "*-" for b in block]) < 2:
                # not a list
                block = [b.lstrip() for b in block]
                outlines[i] = " ".join(block)
            else:
                newblock = []
                for line in block:
                    if re.search(r'\S', line).group() in "*-":
                        newblock.append(line)
                    else:
                        newblock[-1] += " " + line.lstrip()
                outlines[i] = newblock

    outlines_final = []
    for block in outlines:
        if type(block) == list:
            for line in block:
                outlines_final.append(line)
        else:
            outlines_final.append(block)
    outtext = '\n'.join(outlines_final)
    return outtext


def add_one(number):
    return number + 1
