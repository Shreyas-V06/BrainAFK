from langchain.prompts import PromptTemplate
def GenerateAlgorithmPrompt():
    AlgorithmPromptTemplate=PromptTemplate(
        input_variables=['code'],
        template='''

You are an AI that generates step-by-step algorithms for given code snippets, For the given code:

{code}
        
Follow these strict rules and generate algorithms:  

1. Always start with Step 1: Start and end with Step last: End.  
2. If the algorithm involves loops, use this format:  
   Step n: Repeat for i = 0 to i < n:  
   n.1 [Action]  
   n.2 [Action]  
3. If the problem involves multiple functions (e.g., stack operations, sorting algorithms), write separate algorithms for each function, excluding the main function.  
4. Each step should be clear and concise, with a maximum of 10-12 words.  
5. Avoid unnecessary steps like initialization or declaration. Focus only on the logical steps.  

Example Algorithm: Checking if a Number is a Palindrome  

Function: isPalindrome(n)  
1. Start  
2. Set rev = 0 and temp = n  
3. Repeat while temp ≠ 0:  
   3.1 Get last digit of temp  
   3.2 Multiply rev by 10 and add last digit  
   3.3 Divide temp by 10  
4. If rev = n, print "Palindrome", else print "Not Palindrome"  
5. End  

Output Format: Output should only contain the algorithm only, 
with appropriate newline characters added at end of each line. 
Do not add any comments of your own''')

    return AlgorithmPromptTemplate
def GenerateAimPrompt():
    AimPromptTemplate = PromptTemplate(input_variables=['algorithm'], template= '''
You are an AI that generates the Aim of the Experiment for a given algorithm. 
Generate the Aim of the experiment for 
{algorithm} 
                                       
By Following these strict rules when writing the aim:  

1. Use one of the two formats:  
   Format 1: Aim: To implement [code_purpose] using C program  
   Format 2: Aim: To write a C program to [code_purpose]  
2. Clearly describe the purpose of the given algorithm in simple and precise terms.  
3. If the algorithm involves a specific data structure, mention it explicitly.  
4. Do not add unnecessary details or explanations.  

Example 1: If the algorithm is for merge sort, the output should be:  
Aim: To implement Merge Sort algorithm using C program  

Example 2: If the algorithm is to reverse a string using stacks, the output should be:  
Aim: To write a C program to reverse a given string using the stack data structure  

Output format : 
Strictly just give the output of the content of Aim only without any additional sentences or word
Example output : Aim: To implement Merge Sort algorithm using C program 

 .''')
    return AimPromptTemplate
def GenerateConclusionPrompt():
    ConclusionPromptTemplate = PromptTemplate(input_variables=['aim'],template='''
You are an AI that generates the Conclusion of the Experiment based on the given Aim. 
Generate the Conclusion for the given aim:
                                              
{aim}
                                              
Follow these strict rules when writing the conclusion:  

1. Use the format: Conclusion: Successfully implemented [code_purpose] and passed all test cases 
2. The [code_purpose] must exactly match the key operation or concept from the given Aim.  
3. Do not add unnecessary details or explanations.  
4. Ensure the conclusion confirms successful implementation and correctness.  

Example: If the aim is:  
Aim: To implement Merge Sort algorithm using C program  

The output should be:  
Conclusion: Successfully implemented Merge Sort and passed all test cases  

Output should only contain the conclusion without any additional inputs from your side
Output example: Conclusion: Successfully implemented Merge Sort and passed all test cases''')
    return ConclusionPromptTemplate