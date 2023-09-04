station = []
person = 0
max_person = []
for i in range(4) :
    out_person, in_person = map(int, input().split())
    person += in_person - out_person
    max_person.append(person)

print(max(max_person))
