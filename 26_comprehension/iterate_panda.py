import pandas as pd

student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'scores': [56, 78, 98]
}

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

print('**************************')

stud_df = pd.DataFrame(student_dict)
# print(stud_df)
#
# for (key, value) in stud_df.items():
#     print(value)


# loop through rows of a DF
for(index, row) in stud_df.iterrows():
    # print(row)
    print(row['student'])
    if row['student'] == 'Angela':
        print(row['scores'])
