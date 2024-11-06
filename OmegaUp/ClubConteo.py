# %%
import sys
def count_subchains(chain):
    counts = []
    current_count = 1
    
    for i in range(1, len(chain)):
        if chain[i] == chain[i - 1]:
            current_count += 1
        else:
            counts.append(current_count)
            current_count = 1

    # Append the count for the last subchain
    counts.append(current_count)
    return counts

for line in sys.stdin:
# for i in range(3):
    
    chain = line.strip()
    # chain = input()
    subchain_counts = count_subchains(chain)


    people_min = subchain_counts[0]
    if len(chain) > 0 :

        for i in range(1, len(subchain_counts)):

            people_min = people_min + max(0, subchain_counts[i] - people_min )

        print(people_min)   
    else:
        print(0)

        
# # %%

# def count_subchains(chain):
#     counts = []
#     current_count = 1
#     for i in range(1, len(chain)):
#         if chain[i] == chain[i - 1]:
#             current_count += 1
#         else:
#             counts.append(current_count)
#             current_count = 1

#     # Append the count for the last subchain
#     counts.append(current_count)
#     return counts

# def process_lines(input_string):
#     # Split the input string by lines
#     # input
#     # chain = input()
#     cadenas = input_string.splitlines()
    
#      # Process each line individually
#     for idx, chain in enumerate(cadenas, 1):

#         # You can perform any manipulation here
#         # print(f'Processing line {idx}: {line}')

#         subchain_counts = count_subchains(chain)

#         # # Example of manipulation: print line length
#         # print(f'  Length of line {idx}: {len(line)}')
#         # print('---')

#         people_min = subchain_counts[0]
#         if len(chain) > 0 :

#             for i in range(1, len(subchain_counts)):

#                 people_min = people_min + max(0, subchain_counts[i] - people_min )

#             print(people_min)   
#         else:
#             print(0)


# input_string = """++-+-++++
# --++---
# +-+-"""
# # input_string = input()

# # Call the function with the multi-line input
# process_lines(input_string)