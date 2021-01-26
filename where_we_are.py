"""
Список ключевых слов:
    import keyword
    print(keyword.kwlist)
"""

# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
#
#
#
# for kw in keyword.kwlist:
#     print('   '+kw)

keywords = """
+   None
+   False
+   True

+   not                     
+   or
+   and

!   is

+   pass

+   if
+   elif
+   else

+   while
+   for
+   break
+   continue
+   in

!   try
!   except
!   finally
!   as

!   def
!   return
!   global
!   nonlocal
!   lambda

-   assert
-   async
-   await
?   class
!   del
?   from
?   import
?   raise
?   with
?   yield
"""


keywords_by_category = {}
keywords_list = keywords.split('\n')
for kw in keywords_list:
    if kw:
        letter = kw[0]
        if letter in keywords_by_category:
            keywords_by_category[letter].append(kw)
        else:
            keywords_by_category[letter] = [kw]

for letter, ks in keywords_by_category.items():
    print(f"{letter}: {len(ks)}, {100*len(ks)/len(keywords_list):.2f}%")
    for k in ks:
        print('  ', k)
