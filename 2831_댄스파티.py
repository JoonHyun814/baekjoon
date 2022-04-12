N = int(input())
mans = input().split(' ')
womans = input().split(' ')
matched_num = 0

# 1. 정렬
def p_n_sorting(persons):
    like_tall = []
    like_short = []
    for person in persons:
        if person[0] == '-':
            like_short.append(int(person[1:]))
        else:
            like_tall.append(int(person))
    return sorted(like_short), sorted(like_tall)

mans_like_short,mans_like_tall = p_n_sorting(mans)
womans_like_short,womans_like_tall = p_n_sorting(womans)

# 작은 것을 선호하는 남자 --> 큰 것을 선호하는 여자
womans_like_tall = womans_like_tall[::-1]
for man_like_short in mans_like_short:
    if len(womans_like_tall) == 0:
        break
    if man_like_short <= womans_like_tall[-1]:
        continue
    else:
        matched_num += 1
        womans_like_tall.pop()


# 큰 것을 선호하는 남자 --> 작은 것을 선호하는 여자
for man_like_tall in mans_like_tall[::-1]:
    if len(womans_like_short) == 0:
        break
    if man_like_tall >= womans_like_short[-1]:
        continue
    else:
        matched_num += 1
        womans_like_short.pop()

print(matched_num)