import re

my_numbers = '''
+355 056659865
+213 54548125
+376 548597
+244 465489
+672 18913231
+54 5156846
+374 516598489
+297 546489
+61 546847212
+43 21321354
+994 5468213
+973 5468475
+880 54984321
+375 54232
+32 489984754
+501 15468532
+229 54654861
+975 656465
+591 512356
+387 5165132
+267 21132
+55 87965
+673 54658
+32 489984754
'''

pattern = re.compile(r'\+\d{1,3}')
matches = set(pattern.findall(my_numbers))

if matches:
    nums = list()
    for match in matches:
        num = match.split("+")
        nums.append(int(num[1]))

    nums.sort()

    for num in nums:
        print("+" + str(num) + " " + str(type(num)))
else:
    print("Error")