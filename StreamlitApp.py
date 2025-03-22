from ProcessingChain import GenerationChain
import streamlit as st # type: ignore


def main():
    st.title("BrainAFK🤖")
    st.subheader("Write DS Records mindlessly!")
    code = st.text_area("Paste your C code here:")
    
    if st.button("Generate Output"):
        if code.strip():
            with st.spinner("Cooking..."): 
                result = GenerationChain(code)
                result.update({
                    "Requirements": "Moodle, Basic C knowledge",
                    "code": code,
                    "testcases": "Please refer Moodle for this"
                })
            
            st.subheader("Aim:")
            st.write(result["aim"])
            
            st.subheader("Algorithm:")
            st.text(result["algorithm"])
            
            st.subheader("Code:")
            st.code(result["code"], language="c")
            
            st.subheader("Test Cases:")
            st.write(result["testcases"])
            
            st.subheader("Conclusion:")
            st.write(result["conclusion"])
        else:
            st.error("Please enter your code before generating output.")

if __name__ == "__main__":
    main()