exit_outer_loop=False
for i in range(3):
    for j in range(3):
        print(i, j)
        if i>0:
            exit_outer_loop=True
            break

    if exit_outer_loop:
        break