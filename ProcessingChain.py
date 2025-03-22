from langchain.chains import SequentialChain
from langchain.chains import LLMChain
from ModelInitializer import InitializeGeminiLLM
from PromptTemplates  import GenerateAimPrompt,GenerateAlgorithmPrompt,GenerateConclusionPrompt

def GenerationChain(SourceCode):
    GeminiLLM=InitializeGeminiLLM()
    GenerateAimChain=LLMChain(llm=GeminiLLM,prompt=GenerateAimPrompt(),output_key='aim')
    GenerateAlgorithmChain=LLMChain(llm=GeminiLLM,prompt=GenerateAlgorithmPrompt(),output_key='algorithm')
    GenerateConclsuionChain=LLMChain(llm=GeminiLLM,prompt=GenerateConclusionPrompt(),output_key='conclusion')

    chain=SequentialChain(chains=[GenerateAlgorithmChain,GenerateAimChain,GenerateConclsuionChain],input_variables=['code'],output_variables=['algorithm','aim','conclusion'])
    Response=chain.invoke({'code':SourceCode})
    return Response



