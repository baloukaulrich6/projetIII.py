row1 = ["🟥","🟥","🟥"]
row2 = ["🟥","🟥","🟥"]
row3 = ["🟥","🟥","🟥"]
map= [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input ("ou avez vous mis le tresor ? ")

horizontal= int(position[0])
verticla = int(position[1])

select_row = map[verticla - 1 ]
select_row[horizontal -1] = "X"

print(f"{row1}\n{row2}\n{row3}")