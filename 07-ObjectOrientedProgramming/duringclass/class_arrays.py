class Arrays():

    @staticmethod 
    def print_in_col(array): 
        for c in array: 
            print(c)

    @staticmethod
    def print_in_line(array):
        print(str(array).strip('[]')) 

    @staticmethod
    def create_array(numberOfElements,element):
        arr = []
        while 0 < numberOfElements:
            arr.append(element)
            numberOfElements -= 1
        print(arr)  
    @staticmethod 
    def random_int(numberOfElements,l,h):
        arr = []
        for x in range(numberOfElements):
            arr.append(randint(l,h))
        print(arr)
    @staticmethod
    def elementsSpec(array,l,h):
        counter = 0
        for x in array:
            if x >= l and x <= h:
                counter += 1 
        print(counter)

my_array = [4, 1, 8, 7, 2]         
Arrays.print_in_col(my_array)
Arrays.print_in_line(my_array)
Arrays.create_array(5,5) # A
Arrays.random_int(10,1,4) # B
Arrays.elementsSpec([1,2,3,4,5,6,7,8,9], 3,8)