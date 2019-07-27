def sum(*n):
    result = 0
    iteration  = 1
    resval = 1
    xval = 1
    for x in n:
        print(resval," starting Result value : ",result )

        print(xval," starting X value is :",x)
        print("\n")
        result = result + x
        print(iteration," Iteration Result Value is : ",result)
        print("\n")
        iteration = iteration + 1
        resval = resval + 1
        xval = xval + 1
    print(" Final Result value is ",result)



sum(70,20)
