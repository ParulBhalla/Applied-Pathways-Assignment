#print table header with labels "Question Label",
#"Answer Values" and "Type" enclosed within "hyphens"

print('-'*128)

print('|{0:72} | {1:24} | {2:24}|'.format('Question Label', 'Answer Values', 'Type'))

print('-'*128)


#Open the input file
#Use file object "fo"

with open('appliedpathways_input_file.txt') as fo:

#Define variables to be used in the program
#These variables are initialized with empty strings
    
    op_name=''
    op_answer_names=''
    op_additional_data=''
    column_2_val=''
    op_type=''
    

#Each node in the input file is separated by "#----" sign
#Traverse each node and read each line of the node
#Each node is split by "#--------" and each line is split
#by a newline character

    for x in fo.read().split("#--------------------"):
        for y in x.split("\n"):

#Check if the line in the node is a name or
#answer_names or additional_data:result or
#type. Based on this, store the value in respective variables
#Bit slice portion of the input list to extract the information
#needed. This information will be printed in the table column.

        
            if y.find("#name")!=-1:
                op_name=y       
                
                            
            if y.find("#answer_names")!=-1:
                op_answer_names=y
                column_2_val=op_answer_names[15:]             
                

            if y.find("#additionaldata:result")!=-1:
                op_additional_data=y
                column_2_val=op_additional_data[24:]

            if y.find("#type")!=-1:
                op_type=y                         
                

       
        print('|{0:72} | {1:24} | {2:24}|'.format(op_name[7:],column_2_val,op_type[7:]))     

 
#Reset the variables
               
        op_answer_names=''
        op_additional_data=''
        column_2_val=''
        op_type=''
   

        fo.close()

print('-'*128)