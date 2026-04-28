words = ["ծրագրավորում", "ինֆորմատիկա", "դպրոց", "համակարգիչ", "ցիկլ"]
longest_word = ""

for w in words:
    if len(w) > len(longest_word):
        longest_word = w

print(f"Ցուցակը. {words}")
print(f"Ամենաերկար բառը՝ '{longest_word}'")
print(f"Տառերի քանակը՝ {len(longest_word)}")