#Name : Hamid Ahmad
#Working : First part checking whether matrix is REF or not & second part converting the matrix into REF form
# Note:
    #use convertMatrixIntoREF(matrix) to convert your matrix into REF matrix and give a matrix as a parameter

    #use is_REF(matrix) to check your matrix is REF matrix or not REF matrix and give matrix as a parameter
    # you need numpy pacakage to run this
    #where ever I use REF/ref in code it means (Row enchlon form) 

#Check whether matrix is is REF or not

import numpy as np

#Part 0
#Checking if matrix is zero. In case of zero matrix it is ref so return True
def isZeroMatrix(matrix):
    #get number of rows & colmns of matrix
    matrixOrder=matrix.shape
    row = matrixOrder[0]
    column = matrixOrder[1]
    
    #itterate through each row and column
    for i in range(row):
        for x in range(column):
            
            #and check every element of matrix. If there is no non-zero element then it's a zero mtrix & ref matrix.
            #if there is single non-zero element then it's a non-zero matrix
            elementOfMatrix = matrix[i, x]
            if elementOfMatrix !=0:
                return False
                
    return True

#----------------------------------------

#Part 1
#getting the pivot

#this function is giving the pivot positions in each row of matrix
def pivotPosition(matrix):
    #get number of rows & colmns of matrix
    matrixOrder = matrix.shape
    row = matrixOrder[0]
    column = matrixOrder[1]

    # creating an empty list to store the pivot position of row and utilize later
    pivotPositions=[]
    
    # itterating through each row and column
    for i in range(row):
        for x in range(column):
            element = matrix[i, x]
            
            # if there is any pivot in row then store it's position in empty list which we already created
            if(element != 0):
                pivotPositions.append(x)
                break
        try:
            if(pivotPositions[i-1]):
                #print(pivotPositions[i])
                pass
        except:
            pivotPositions.append(100+i)
                
    return pivotPositions

#-----------------------------------------------
#Part 2

#this function is checking whether the zero rows of matrix are at bottom or not
def isZeroRowPositionValid(matrix):
    
    matrixOrder = matrix.shape
    row = matrixOrder[0]
    column = matrixOrder[1]
    
    nonZeroRowPosition=[]
    zeroRowPosition=[]
    
    #getting the positions of non-zero rows and zero-rows in matrix
    for i in range(row):
        storeElementZeros=[]
        for j in range(column):
            element = matrix[i,j]
            
            if element !=0:
                nonZeroRowPosition.append(i)
                break
            else:
                
                storeElementZeros.append(element)
                
                if len(storeElementZeros)==column:
                    zeroRowPosition.append(i)
                    
    # if zero rows are not at bottom then return false
    for i in nonZeroRowPosition:
        nonZeroRowNumber=i
        
        for j in zeroRowPosition:
            zeroRowNumber = j
            
            if(zeroRowNumber<=nonZeroRowNumber):
                return False
            
    return True


#---------------------------------------------------------

#Part 3

#getting the pivot postion of each row of matrix
def pivotPosition(matrix):
    matrixOrder = matrix.shape
    row = matrixOrder[0]
    column = matrixOrder[1]

    #creating a empty list to save pivot positions later in it
    pivotPositions=[]
    
    #itterating through each row and
    for i in range(row):
        for x in range(column):
            element = matrix[i, x]
            
            # ... and saving the positions of pivot positions of each row in pivotPositions list which we declared earlier
            if(element != 0):
                pivotPositions.append(x)
                break
        try:
            if(pivotPositions[i-1]):
                print(pivotPositions[i])
        except:
            pivotPositions.append(100+i)
                
    return pivotPositions         
                
#------------------------------------------------------
#Part 4


#checking the pivot positions is valid or not in each row of matrix

def validPivotPositions(pivotPositions):
    min_value=pivotPositions[0]
    
    noOfPivotPosition = len(pivotPositions)
    
    for i in range(1,noOfPivotPosition):
        pivotPoint = pivotPositions[i]
        
        if(min_value<pivotPoint):
            min_value=pivotPoint
        else:
            return False
        
    return True


#---------------------------------------------
#Final Part

#controling the whole first program and giving response to user
def is_REF(matrix):
    try:
        zeroMatrix=isZeroMatrix(matrix)
        if zeroMatrix:
            return True
    
        if isZeroRowPositionValid(matrix):
            pass
        else:
            return False
    
        pivotsPositions=pivotPosition(matrix)
        if validPivotPositions(pivotsPositions)==True:
            return True
        else:
            return False
    except:
        print("There occured an error")

checkMatrix = np.array([[1,0,1],[0,2,1],[0,0,0]])
isREF=is_REF(checkMatrix)
if(isREF==True):
    print("It's REF matrix")
else:
    print(isREF)

#First task of checking whether matrix is in REF is ending here
#-------------------------------------------------------------------------------------



#Task2 is starting from here
#Convert Matrix into Row Enchlon Form
# Step:1. Arrange the zero rows at bottom of matrix (using function 1 & 2)
# Step:2. Arrange that row at top that has less number of zero before pivot then so on(using function 3 & 4)
# Step:3. Creating zeros under Pivot (using function 5)
# Step:4. Converting pivots to 1 (using function 6)
# Final function controlling whole program 

import numpy as np

#Part 0

#checking whether  matrix is zero matrix or not
def isZeroMatrix(matrix):
    matrixOrder=matrix.shape
    row = matrixOrder[0]
    column = matrixOrder[1]
    
    for i in range(row):
        for x in range(column):
            elementOfMatrix = matrix[i, x]
            if elementOfMatrix !=0:
                return False
                
    return True



#-------------------------------------------------

# this function will work only if matrix have only one column because this is a special case which was causing proble,
#Part 0.5 
def lessThan2Column(matrix):
    order = matrix.shape
    row = order[0]
    column = order[1]
    if column < 2 :
        #assigning the first column of first row it's default value 
        matrix[0][0]=matrix[0][0]

        # ... and others are 0
        for i in range(1,row):
                matrix[i][0]=0

    return matrix

#-------------------------------------------------


#Part 1
#getting the positions of zero rows

def zeroRowPosition(matrix):
    #get the order of matrix
    matrixOrder = matrix.shape
    row = matrixOrder[0]
    column = matrixOrder[1]
    
    #this list will store the position of non-zero rows and next list will store position of zero rows
    nonZeroRowPosition=[]
    zeroRowPosition=[]

    #this loop will check every row
    for i in range(row):
        #actually this list will help to identify zero row.
        #first we are checking if element is zero then it will store in this list
        #if number of zero elemnts in this list is equal to the number of elements in the matrix it 
        #means this row is zero row
        storeElementZeros=[]
        for j in range(column):
            element = matrix[i,j]
            
            # it's stroing the positions of non-zero rows
            if element !=0:
                nonZeroRowPosition.append(i)
                break
            else:
                
                #if element is zero so store 0 in list 
                storeElementZeros.append(element)
                #... if length of storeElementZeros become equal to no of columns then it means row is zero row
                if len(storeElementZeros)==column:
                    # ... and then store the position of that row in zeroRowPosition list
                    zeroRowPosition.append(i)
                    
    # returning the positions of zero and non-zero rows
    rowPositions=[zeroRowPosition,nonZeroRowPosition]         
    return rowPositions



#--------------------------------------------------------
#Part2


# this function first getting the positions of zero and non-zero rows from previous function 
#(zeroRowPostion) and then swapping zero rows to the bottom of matrix
def changeZeroRowPosition(matrix):
    #get the order of matrix
    order=matrix.shape
    row=order[0]
    
    #get the position of zero and non-zero rows
    rowPositions=zeroRowPosition(matrix)
    nonZeroRowPositionArray = rowPositions[1] #positin of non-zero rows
    zeroRowPositionArray=rowPositions[0] #positin of zero rows
    
    #and now knowing how many zero and non-zero rows are there
    lenOfNonZeroRowPositionArray = len(nonZeroRowPositionArray)
    lenOfZeroRowPositionArray=len(zeroRowPositionArray)
    
    #if there is any row with zeros then do this
    if (lenOfZeroRowPositionArray!=0):
            
          
        #declare an empty list to store rows in this
        variables=[]
        
        #first start storing nonzero rows in it 
        for i in range(lenOfNonZeroRowPositionArray):
            variables.append(list(matrix[nonZeroRowPositionArray[i]]))
            
        #then store zero rows it
        for i in range(lenOfZeroRowPositionArray):
            #print(matrix[zeroRowPositionArray[i]])  
            variables.append(list(matrix[zeroRowPositionArray[i]]))
        
        #change the positions of rows in matrix and now zero rows will be at the end
        #print(variables)
        
        for i in range(0,row):
            matrix[i]=variables[i]
            
        #print(matrix)
            
    return matrix


#-------------------------------------------------------------------
#Part3


# this function tells how many number of zero are there on left side of pivot
def giveNoOfZerosWRTtoZerosOnleftOfPivot(matrix):
    order=matrix.shape
    
    row = order[0]
    column=order[1]
    
    #this list is for stroing zeros of left side of pivot if when we find pivot then by getting the 
    #length of list we can know the number of zero in that respective list
    no_of_zeros=[]
    for i in range(row):
        #print(f"Column is {i}")
        counter=0
        #print(f"initial value of count is {counter}")
        for j in range(column):
            element=matrix[i,j]
            
            #checking wheter row is zero-row or not because in case of zero row no need to count zeros
            #this first condition is telling that row is zero row
            #ye wali condition last element mai row par chalti hai agar row kay all elements 0 hon aur
            #last element bh zero ho tu ye phir zero row hogi
            if((j+1)==column and element==0):
                #print("Yes")
                no_of_zeros.append(-1)
            elif element==0:
                #this counter is counting number of zeros till it find any non-zero in row
                counter=counter+1
            elif((j+1)==column and element!=0):
                #jab non-zero row mai first pivot point mil jaye ga tu ye number of zeros in that row 
                #...store kar day da list no_of_zeros mai
                #here we find non-zero(pivot) so we are adding number of zeros in list
                no_of_zeros.append(counter)
            else:
                no_of_zeros.append(counter)
                #print(counter, no_of_zeros)
                break
            
    return no_of_zeros



#---------------------------------------------------------
#Part4


def arrangeRowWRTNoOfZerosOnleftOfPivot(matrix,zerosRowsOrder):
    order = matrix.shape
    
    row=order[0]
    column= order[1]
    
    #this is getting the number of zeros on left side of pivot in row
    #zerosRowsOrder =  giveNoOfZerosWRTtoZerosOnleftOfPivot(myMatrix)
    
    rowsOfMatrix = []
    
    #this loop is storing all the rows in matrix into a list of rowsOfMatrix to create copy of matrix
    for i in range(row):
        rowsOfMatrix.append(list(matrix[i]))
    
    counter=0
    reArrangeMatrix=[] #this list will have the rows with rearranged rows wrt zeros on left of pivot
    
    start = max(zerosRowsOrder)
    #print(zerosRowsOrder)
    #print(start)
    for i in range(start+1):
        value_to_find = i
        indices = [index for index, value in enumerate(zerosRowsOrder) if value == value_to_find]
        
        
        for j in indices:
            reArrangeMatrix.append(rowsOfMatrix[j])
            counter=counter+1
            
    nonZeroRows=zeroRowPosition(matrix)[1]

    
    for i in nonZeroRows:
        matrix[i]=reArrangeMatrix[i]
       
    return matrix



#-----------------------------------------------------------
#Part5




def makeZerosUnderPivot(matrix):
    matrix = matrix.astype(float)
    num_rows, num_cols = matrix.shape
    
    if num_cols < 2:
        print("Sorry I'm unable to handle this case.")
        return matrix

    for pivot_row in range(num_rows):
        for current_row in range(pivot_row + 1, num_rows):
            pivot_element = matrix[pivot_row][pivot_row]
            if pivot_element == 0:
                continue
            current_element = matrix[current_row][pivot_row]
            
            
            factor = current_element / pivot_element
            
            
            # Update the current row to create zeros below the pivot
            for col in range(pivot_row, num_cols):
                matrix[current_row][col] -= factor * matrix[pivot_row][col]
                #print(factor * matrix[pivot_row][col])

    return matrix



#----------------------------------------------------------------
#Part6

def makePivot(matrix):
    matrix=matrix.astype(float)
    order=matrix.shape
    row = order[0]
    column = order[1]
    
    
    for i in range(row):
        for j in range(column):
            element = matrix[i,j]
            if element !=0:
                matrix[i]=matrix[i]/element
                break
            else:
                continue
                
                
        for k in range(column):
            if matrix[i][k]==0:
                    matrix[i][k]+=0
        

    return matrix


#---------------------------------------------------
#Final

#this function is controlling the whole 2nd program
def convertMatrixIntoREF(matrix):
    
    try:
        order=matrix.shape
        if(matrix.size==0):
            return 'Matrix is empty.'
        
        is_Matrix_REF = is_REF(matrix)
        if(is_Matrix_REF==True):
            print("Matrix is already in REF.")
            return matrix
    
        isZero = isZeroMatrix(matrix)
        if(isZero==True):
            print("Matrix is already in REF.")
            return matrix
        if(order[1]<2):
            print("Enter")
            matrix=lessThan2Column(matrix)
            return matrix
        
        matrixChangePositionsOfZeroRows = changeZeroRowPosition(matrix)
        
        
        getNumberOfZerosOnLeftOfPivot = giveNoOfZerosWRTtoZerosOnleftOfPivot(matrixChangePositionsOfZeroRows)
        matrixWithArrangeRowsWRTZeros = arrangeRowWRTNoOfZerosOnleftOfPivot(matrixChangePositionsOfZeroRows, getNumberOfZerosOnLeftOfPivot)
        createZerosUnderPivot = makeZerosUnderPivot(matrixWithArrangeRowsWRTZeros)
        createPivotsInMatrix = makePivot(createZerosUnderPivot)
        againMatrixChangePositionsOfZeroRows = changeZeroRowPosition(createPivotsInMatrix)
        return againMatrixChangePositionsOfZeroRows.round(2)
    except:
        print("Sorry, there occured an error.")



#Matrix for checking wheter code is working well or not
arr = np.array([[0,0,0], [0,0,0], [0,0,0]])
matrixA = np.array([[3,2,3,5], [0,0,0,0] ,[5,5,3,0], [8,3,2,0],[0,3,6,4]])
matrixB = np.array([[1,2,3,5], [1,1,0,0], [0,0,0,0], [0,0,0,0]])
matrixC = np.array([[1,2,3,5], [2,3,3,0], [8,3,0,0]])
matrixD = np.array([[0,0,0,0], [0,0,2,1], [1,2,2,1]])
matrixE = np.array([[1,2], [1,4], [0,7]])
matrixF= np.array([[-2,3,5],[0,4,1],[0,2,1]])
matrixG = np.array([[3], [2], [4]])


convertMatrixIntoREF(matrixC)


#Task 2 is end here to convert a matrix into REF




#use convertMatrixIntoREF(matrix) to convert your matrix into REF matrix and give a matrix as a parameter

#use is_REF(matrix) to check your matrix is REF matrix or not REF matrix and give matrix as a parameter

#Task 2 end
#---------------------------------------------------------------------------------


#Task 3 starting from here
#here we can get number of rows and columns from user generate a random matrix and then convert that matrix into REF(row enchlon form) matrix

#getting number of rows and columns from user
row=int(input("Please enter the number of rows!\n"))
column= int(input("Please enter the number of columns!\n\n"))


randmonMatrix = np.random.randint(1,100,size=(row,column)).round(2)

print("The random matrix is:")
print(randmonMatrix)

refOfRandomMatrix=convertMatrixIntoREF(randmonMatrix)


print("Convert random matrix into REF matrix:\n")
print(refOfRandomMatrix)



