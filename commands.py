codepage = "λƛ¬∧⟑∨⟇÷«\n»°•․⍎Ṛ½∆øÏÔÇæʀʁɾɽÞƈ∞⫙ !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ß⎝⎠⎡⎣⨥⨪∺❝ð→←ÐřŠč√⳹ẊȦȮḊĖẸṙ∑Ĥ⟨⟩ı⁌\tΤĴ²‿⁂ĸ¶⁋⁑Ńń‼⨊≈ðʗ◁⊐∫⍋⍒∈ₛ£Œœ≕≠¥ⁱ‹›⍲⍱‸¡⊑≀℅≤≥↜≗⋯⧢ũ⁰¹ªₑϊ≎⇿⊛×¯±⊂⍞፣₴⍉ΐ₁⊘ᶢ₌↭ſƀƁ⁚⌈⌊⊓⊣Ḟḟ∪∩⊍⁜⌑Ḇ₂⁾₦¼ƒɖꝒ′₥α″βγΠ"
command_dict = {

    "!": ("stack.append(len(stack))", 0),
    "$": ("top = pop(stack); over = pop(stack); stack += [top, over]", 2),
    "%": ("rhs, lhs = pop(stack, 2); stack.append(modulo(lhs, rhs))", 2),
    "*": ("rhs, lhs = pop(stack, 2); stack.append(multiply(lhs, rhs))", 2),
    "+": ("rhs, lhs = pop(stack, 2); stack.append(add(lhs, rhs))", 2),
    ",": ("VY_print(pop(stack)); printed = True", 1),
    "-": ("rhs, lhs = pop(stack, 2); stack.append(subtract(lhs, rhs))", 2),
    "/": ("rhs, lhs = pop(stack, 2); stack.append(divide(lhs, rhs))", 2),
    ":": ("temp = deref(pop(stack)); stack += [temp]*2", 1),
    "^": ("stack = stack[::-1]", 0),
    "_": ("pop(stack)", 1),
    "<": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.LESS_THAN))", 2),
    ">": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.GREATER_THAN))", 2),
    "=": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.EQUALS))", 2),
    "?": ("stack.append(get_input())", 0),
    "A": ("stack.append(int(all(iterable(pop(stack)))))", 1),
    "B": ("stack.append(VY_int(pop(stack), 2))", 1),
    "C": ("stack.append(chrord(pop(stack)))", 1),
    "D": ("temp = deref(pop(stack)); stack += [temp]*3", 1),
    "E": ("stack.append(VY_eval(pop(stack)))", 1),
    "F": ("fn, vector = pop(stack, 2); stack.append(VY_filter(fn, vector))", 2),
    "G": ("stack.append(VY_max(iterable(pop(stack))))", 1),
    "H": ("stack.append(VY_int(pop(stack), 16))", 1),
    "I": ("stack.append(VY_int(pop(stack)))", 1),
    "J": ("rhs, lhs = pop(stack, 2); stack.append(join(lhs, rhs))", 2),
    "K": ("stack.append(divisors_of(pop(stack)))", 1),
    "L": ("stack.append(len(iterable(pop(stack))))", 1),
    "M": ("fn, vector = pop(stack, 2); stack.append(VY_map(fn, vector))", 2),
    "N": ("stack.append(multiply(pop(stack), -1))", 1),
    "O": ("needle, haystack = pop(stack, 2); stack.append(iterable(haystack).count(needle))", 2),
    "P": ("rhs, lhs = pop(stack, 2); stack.append(VY_str(lhs).strip(VY_str(rhs)))", 2),
    "Q": ("exit()", 0),
    "R": ("fn, vector = pop(stack, 2); stack.append(VY_reduce(fn, vector))", 2),
    "S": ("stack.append(VY_str(pop(stack)))", 1),
    "T": ("stack.append([n for n in iterable(pop(stack)) if bool(n)])", 1),
    "U": ("stack.append(uniquify(pop(stack)))", 1),
    "V": ("replacement, needle, haystack = pop(stack, 3); stack.append(replace(haystack, needle, replacement))", 3),
    "W": ("stack = [deref(stack)]", 0),
    "X": ("context_level += 1", 0),
    "Y": ("rhs, lhs = pop(stack, 2); stack.append(interleave(lhs, rhs))", 2),
    "Z": ("rhs, lhs = pop(stack, 2); stack.append(Generator(VY_zip(iterable(lhs), iterable(rhs))))", 2),
    "a": ("stack.append(int(any(iterable(pop(stack)))))", 1),
    "b": ("stack.append(VY_bin(pop(stack)))", 1),
    "c": ("needle, haystack = pop(stack, 2); haystack = iterable(haystack, str)\nif type(haystack) is str: needle = VY_str(needle)\nstack.append(int(needle in iterable(haystack, str)))", 2),
    "d": ("stack.append(multiply(pop(stack), 2))", 1),
    "e": ("rhs, lhs = pop(stack, 2); stack.append(exponate(lhs, rhs))", 2),
    "f": ("stack.append(flatten(iterable(pop(stack))))", 1),
    "g": ("stack.append(VY_min(iterable(pop(stack))))", 1),
    "h": ("stack.append(iterable(pop(stack))[0])", 1),
    "i": ("rhs, lhs = pop(stack, 2)\nif type(rhs) is list: stack.append(iterable(lhs)[slice(*rhs)])\nelse: stack.append(iterable(lhs)[rhs])", 2),
    "j": ("rhs, lhs = pop(stack, 2); stack.append(str(rhs).join([str(x) for x in iterable(lhs)]))", 2),
    "l": ("rhs, lhs = pop(stack, 2); stack.append(nwise_pair(lhs, rhs))", 2),
    "m": ("item = pop(stack); stack.append(add(item, reverse(item)))", 1),
    "n": ("stack.append(context_values[context_level % len(context_values)])", 0),
    "o": ("needle, haystack = pop(stack, 2); stack.append(remove(haystack, needle))", 2),
    "p": ("rhs, lhs = pop(stack, 2); stack.append(int(str(lhs).startswith(str(rhs))))", 2),
    "q": ("stack.append('`' + VY_str(pop(stack)) + '`')", 1),
    "r": ("rhs, lhs = pop(stack, 2); stack.append(orderless_range(lhs, rhs))", 2),
    "s": ("stack.append(VY_sorted(pop(stack)))", 1),
    "t": ("stack.append(iterable(pop(stack))[-1])", 1),
    "u": ("stack.append(-1)", 0),
    "w": ("stack.append([pop(stack)])", 1),
    "x": ("context_level -= 1", 0),
    "y": ("stack += uninterleave(pop(stack))", 1),
    "z": ("fn, vector = pop(stack, 2); stack.append(VY_zipmap(fn, vector))", 2),
    "¬": ("stack.append(int(not pop(stack)))", 1),
    "∧": ("rhs, lhs = pop(stack, 2); stack.append(lhs and rhs)", 2),
    "⟑": ("rhs, lhs = pop(stack, 2); stack.append(rhs and lhs)", 2),
    "∨": ("rhs, lhs = pop(stack, 2); stack.append(lhs or rhs)", 2),
    "⟇": ("rhs, lhs = pop(stack, 2); stack.append(rhs or lhs)", 2),
    "÷": ("for item in iterable(pop(stack)): stack.append(item)", 1),
    "•": ("rhs, lhs = pop(stack, 2); stack.append(log(lhs, rhs))", 2),
    "⍎": ("fn = pop(stack); stack += fn(stack)", 1),
    "Ṛ": ("rhs, lhs = pop(stack, 2); stack.append(rand_between(lhs, rhs))", 2),
    "Ï": ("rhs, lhs = pop(stack, 2); stack.append(Generator(itertools.combinations_with_replacement(iterable(lhs), rhs)))", 2),
    "Ô": ("stack.append(Generator(lambda x: (2 * (x + 1)) + 1))", 0),
    "∞": ("stack.append(Generator(lambda x: x))", 0),
    "Ç": ("stack.append(subtract(1, pop(stack)))", 1),
    "æ": ("stack.append(is_prime(pop(stack)))", 1),
    "ʀ": ("stack.append(orderless_range(0, int(add(pop(stack), 1))))", 1),
    "ʁ": ("stack.append(orderless_range(0, int(pop(stack))))", 1),
    "ɾ": ("stack.append(orderless_range(1, int(add(pop(stack), 1))))", 1),
    "ɽ": ("stack.append(orderless_range(1, int(pop(stack))))", 1),
    "Þ": ("tos = iterable(pop(stack)); stack.append(int(tos == tos[::-1]))", 1),
    "ƈ": ("rhs, lhs = pop(stack, 2); stack.append(ncr(lhs, rhs))", 2),
    "⎡": ("rhs, lhs = pop(stack, 2); stack.append(VY_max(lhs, rhs))", 2),
    "⎣": ("rhs, lhs = pop(stack, 2); stack.append(VY_min(lhs, rhs))", 2),
    "Ð": ("alphabet, number = pop(stack, 2); stack.append(utilities.to_ten(number, alphabet))", 2),
    "Š": ("alphabet, number = pop(stack, 2); stack.append(utilities.from_ten(number, alphabet))", 2),
    "ř": ("rhs, lhs = pop(stack, 2); stack.append(repeat(lhs, rhs))", 2),
    "∺": ("stack.append(modulo(pop(stack), 2))", 1),
    "⨥": ("stack.append(add(pop(stack), 1))", 1),
    "⨪": ("stack.append(subtract(pop(stack), 1))", 1),
    "Ĥ": ("stack.append(100)", 0),
    "Ĵ": ("stack.append(''.join([VY_str(x) for x in iterable(pop(stack))]))", 1),
    "⁌": ("stack.append('\\n'.join([VY_str(x) for x in iterable(pop(stack))]))", 1),
    "Τ": ("stack.append(10)", 0),
    "²": ("x = pop(stack); stack.append(multiply(deref(x), deref(x)))", 1),
    "∑": ("stack.append(summate(pop(stack)))", 0),
    "‿": ("rhs, lhs = pop(stack, 2); stack.append([lhs, rhs])", 2),
    "č": ("stack.append(int(pop(stack) != 1))", 1),
    "½": ("stack.append(divide(pop(stack), 2))", 1),
    "❝": ("stack.append('')", 0),
    "ð": ("stack.append(' ')", 0),
    "√": ("stack.append(exponate(pop(stack), 0.5))", 1),
    "⳹": ("rhs, lhs = pop(stack, 2); stack.append(integer_divide(lhs, rhs))", 2),
    "Ẋ": ("rhs, lhs = pop(stack, 2); stack.append(int((lhs or rhs) and not (lhs and rhs)))", 2),
    "Ȧ": ("stack.append(VY_abs(pop(stack)))", 1),
    "Ȯ": ("stack.append(VY_oct(pop(stack)))", 1),
    "Ḋ": ("rhs, lhs = pop(stack, 2); stack.append([integer_divide(deref(lhs), deref(rhs)), modulo(lhs, rhs)])", 2), # Dereference because generators could accidentally get exhausted.
    "Ė": ("stack.append(Generator(enumerate(iterable(pop(stack)))))", 1),
    "Ẹ": ("stack = [Generator(enumerate(stack))]", 0),
    "ṙ": ("stack.append(VY_round(pop(stack)))", 1),
    "⁂":("rhs, lhs = pop(stack, 2); stack.append(inclusive_range(lhs, rhs))", 2),
    "ĸ": ("value, vector = pop(stack, 2); stack.append(distribute(vector, value))", 2),
    "¶": ("stack.append('\\n')", 0),
    "⁋": ("stack.append(vertical_join(pop(stack)))", 1),
    "⁑": ("padding, vector = pop(stack, 2); stack.append(vertical_join(vector, padding))", 2),
    "Ń": ("n, fn = pop(stack, 2); stack.append(first_n(fn, n))", 2),
    "ń": ("stack.append(first_n(pop(stack)))", 1),
    "‼": ("stack.append(factorial(pop(stack)))", 1),
    "⨊": ("stack.append(cumulative_sum(iterable(pop(stack))))", 1),
    "≈": ("stack.append(int(len(set(iterable(pop(stack)))) == 1))", 1),
    "ʗ": ("stack.append(counts(pop(stack)))", 1),
    "◁": ("stack.append(reverse(pop(stack)))", 1),
    "⊐": ("stack.append(iterable(pop(stack), str)[:-1])", 1),
    "⎝": ("stack.append(min(pop(stack), key=lambda x: x[-1]))", 1),
    "⎠": ("stack.append(max(pop(stack), key=lambda x: x[-1]))", 1),
    "∫": ("stack = [summate(stack)]", 0),
    "⍋": ("stack.append(graded(iterable(pop(stack))))", 1),
    "⍒": ("stack.append(reverse(graded(iterable(pop(stack)))))", 1),
    "∈": ("fn, vector = pop(stack, 2); stack.append(indexes_where(fn, iterable(vector)))", 2),
    "ₛ": ("fn , vector = pop(stack, 2); stack.append(VY_sorted(vector, fn))", 2),
    "£": ("register = pop(stack)", 1),
    "Œ": ("indexes, vector = pop(stack, 2); stack.append(indexed_into(iterable(vector), iterable(indexes)))", 2),
    "œ": ("rhs, lhs = pop(stack, 2); stack.append(compare(modulo(lhs, rhs), 0, Comparitors.EQUALS))", 2),
    "≕": ("rhs, lhs = pop(stack, 2); stack.append(int(lhs == rhs))", 2),
    "≠": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.NOT_EQUALS))", 2),
    "¥": ("stack.append(register)", 0), #---------------------------
    "ⁱ": ("rhs, lhs = pop(stack, 2); stack.append(iterable(lhs)[rhs:])", 2),
    "‹": ("rhs, lhs = pop(stack, 2); stack.append(lshift(lhs, rhs))", 2),
    "›": ("rhs, lhs = pop(stack, 2); stack.append(rshift(lhs, rhs))", 2),
    "⍲": ("rhs, lhs = pop(stack, 2); stack.append(bit_and(lhs, rhs))", 2),
    "⍱": ("rhs, lhs = pop(stack, 2); stack.append(bit_or(lhs, rhs))", 2),
    "‸": ("rhs, lhs = pop(stack, 2); stack.append(bit_xor(lhs, rhs))", 2),
    "¡": ("stack.append(bit_not(pop(stack)))", 1),
    "⊑": ("item, vector = pop(stack, 2); stack.append(prepend(iterable(vector), item))", 2),
    "≀": ("item, index, vector = pop(stack, 3); stack.append(inserted(vector, item, index))", 3),
    "℅": ("stack.append(random.choice(iterable(pop(stack))))", 1),
    "≤": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.LESS_THAN_EQUALS))", 2),
    "≥": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.GREATER_THAN_EQUALS))", 2),
    "↜": ("if len(stack) >= 2: stack.append(stack[-2])\nelse: stack.append(get_input())", 0),
    "≗": ("value, index, vector = pop(stack, 3); stack.append(assigned(iterable(vector), index, value))", 3),
    "⋯": ("top = pop(stack);\nif VY_type(top) == Number:stack.append(Generator(partition(top)))\nelse: stack.append(' '.join([VY_str(x) for x in top]))", 1), #---------------------------
    "⧢": ("stack.append(Generator(itertools.permutations(iterable(pop(stack)))))", 1),
    "ũ": ("stack.append(integer_list(pop(stack)))", 1),
    "⁰": ("index, vector = pop(stack, 2); stack.append(iterable(vector)[0:index])", 2),
    "¹": ("index, vector = pop(stack, 2); stack.append(iterable(vector)[1:index])", 2),
    "ₑ": ("code = VY_compile(pop(stack)); exec(code);", 1),
    "ϊ": ("obj = iterable(pop(stack)); stack.append(Generator(range(1, len(obj) + 1)))", 1),
    "≎": ("stack.append(group_consecutive(iterable(pop(stack))))", 1),
    "⇿": ("new, original, string = pop(stack, 3); stack.append(transilterate(iterable(original, str), iterable(new, str), iterable(string, str)))", 3),
    "⊛": ("stack = [stack[0], stack[1:]]", 1),
    "×": ("rhs, lhs = pop(stack, 2); stack.append(Generator(itertools.product(iterable(lhs), iterable(rhs))))", 2),
    "¯": ("stack.append(deltas(pop(stack)))", 1),
    "±": ("stack.append(sign_of(pop(stack)))", 1),
    "⊂": ("length, vector = pop(stack, 2); vector = iterable(vector)\nif type(vector) is str: vector = list(vector)\nstack.append(Generator(itertools.combinations(vector, length)))", 2),
    "⍞": ("if inputs: stack.append([inputs])\nelse:\n    s, x = [], input()\n    while x:\n        s.append(Vy_eval(x)); x = input()", 0),
    "፣": ("VY_print(stack[-1]); printed = True", 0),
    "₴": ("VY_print(pop(stack), end=''); printed = True", 1),
    "⍉": ("stack.append(transpose(iterable(pop(stack))))", 1),
    "ΐ": ("obj = iterable(pop(stack)); stack.append(Generator(range(0, len(obj))))", 1),
    "₁": ("stack.append(input_values[input_level][0][-1])", 0),
    "⊘": ("rhs, lhs = pop(stack, 2); stack.append(split(lhs, rhs, True))", 2),
    "ᶢ": ("rhs = pop(stack)\nif VY_type(rhs) in [list, Generator]: stack.append(gcd(rhs))\nelse: stack.append(gcd(pop(stack), rhs))", 1),
    "↭": ("c, b, a = pop(stack, 3); stack.append(c); stack.append(a); stack.append(b)", 3),
    "ſ": ("stack.append(69)", 0),
    "ƀ": ("""top = pop(stack)
if VY_type(top) is Number:
    limit = int(top); vector = pop(stack)
else:
    limit = -1; vector = top
fn = pop(stack)
stack.append(Generator(fn, limit=limit, initial=iterable(vector)))
""", 2),
    "Ɓ": ("stack.append(int(bool(stack.pop())))", 1),
    "⁚": ("vector = iterable(pop(stack)); stack.append(vector[:-1]); stack.append(vector[-1])", 1),
    "⌈": ("stack.append(ceiling(pop(stack)))", 1),
    "⌊": ("stack.append(floor(pop(stack)))", 1),
    "⊓": ("rhs, lhs = pop(stack, 2); stack.append(wrap(lhs, rhs))", 2),
    "⊣": ("rhs, lhs = pop(stack, 2); stack.append(trim(lhs, rhs))", 2),
    "Ḟ": ("needle, haystack = pop(stack, 2); stack.append(find(iterable(haystack), needle))", 2),
    "ḟ": ("start, needle, hastack = pop(stack, 3); stack.append(find(iterable(haystack), needle, start))", 3),
    "∪": ("rhs, lhs = map(iterable, pop(stack, 2)); stack.append(list(set(lhs) | set(rhs)))", 2),
    "∩": ("rhs, lhs = map(iterable, pop(stack, 2)); stack.append(list(set(lhs) & set(rhs)))", 2),
    "⊍": ("rhs, lhs = map(iterable, pop(stack, 2)); stack.append(list(set(lhs) ^ set(rhs)))", 2),
    "⁜": ("stack.append(divide(1, pop(stack)))", 1),
    "Ḇ": ("stack += bifuricate(pop(stack))", 1),
    "₂": ("stack.append(input_values[input_level][0][-2])", 0),
    "⁾": ("stack.append(exponate(10, pop(stack)))", 1),
    "₦": ("stack.append(str(pop(stack)).split('\n'))", 1),
    "¼": ("stack.append(divide(pop(stack), 4))", 1),
    "ƒ": ("stack.append(fractionify(pop(stack)))", 1),
    "ɖ": ("stack.append(decimalify(pop(stack)))", 1),
    "Ꝓ": ("stack.append(powerset(iterable(pop(stack))))", 1),
    "′": ("stack.append(sympy.ntheory.primefactors(pop(stack)))", 1),
    "₥": ("top = iterable(pop(stack)); stack.append(divide(summate(top), len(top)))", 1),
    "″": ("stack.append(sympy.ntheory.prime(pop(stack) + 1))", 1),
    "α": ("stack.append(26)", 0),
    "β": ("stack.append(64)", 0),
    "γ": ("stack.append(128)", 0),
    "Π": ("stack.append(product(iterable(pop(stack))))", 1)
}

math_command_dict = {
    "q": ("coeff_a, coeff_b = pop(stack, 2); stack.append(polynomial([coeff_a, coeff_b, 0]))", 2),
    "Q": ("coeff_b, coeff_c = pop(stack, 2); stack.append(polynomial([1, coeff_b, coeff_c]))", 2),
    "P": ("coeff = iterable(pop(stack)); stack.append(polynomial(coeff));", 1)
}

string_command_dict = {
    "o": ("needle, haystack = pop(stack, 2); stack.append(infinite_replace(haystack, needle, ''))", 2),
    "V": ("replacement, needle, haystack = pop(stack, 3); stack.append(infinite_replace(haystack, needle, replacement)", 3),
    "c": ("string = pop(stack); stack.append('«' + utilities.from_ten(utilities.to_ten(string, utilities.base27alphabet), encoding.codepage_string_compress) + '«')", 1),
    "C": ("number = pop(stack); stack.append('»' + utilities.from_ten(number, encoding.codepage_number_compress) + '»')", 1),
    "l": ("stack.append(str(pop(stack)).lower())", 1),
    "U": ("stack.append(str(pop(stack)).upper())", 1),
    "t": ("stack.append(str(pop(stack)).title())", 1),
    "$": ("stack.append(str(pop(stack)).swapcase())", 1)
}

list_command_dict = {}

misc_command_dict = {
    '"': ("stack = iterable_shift(stack, ShiftDirections.RIGHT)", 0),
    "'": ("stack = iterable_shift(stack, ShiftDirections.LEFT)", 0)
}
