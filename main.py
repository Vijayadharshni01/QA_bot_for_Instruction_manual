import streamlit as st 
from langchain import OpenAI
from langchain import PromptTemplate


st.set_page_config(page_title="instructions made easy",page_icon="🐋")


st.markdown("# Instruction Manual Reader")

st.markdown("### Instruction manuals made easy by making this model to read and answer your doubts")

st.image(image="manimg.png",width=700)

prompt = """
You work is to read the user manual given to you are content and given the correct steps or solution to the user's problem/
User will ask you question and you need to carefully read the instruction manual content line by line which is given to you/
and answer the user with correct steps to solve or solution for their question or answer thier doubts clearly.
content that you should read is ({input_content})
the question of the user is ({input_text}) and you need to answer with the above instructions
NOTE: The answer should only be fromt the instruction manual and no answer should be from your own but you can modify the grammer if needed.

If no content is given to read they tell that no content is given if any question is asked and no random asnwers.
"""


input_content = st.text_area("# Copy paste the instruction manual here (max - 4097 characters only)", value="")

input_text = st.text_area("# Write your question or doubts here")

formatted_prompt = prompt.format(input_content=input_content, input_text=input_text)

#st.write(input_content)

#prompt_a = prompt.format(content,user_text)
    #st.write(prompt_a)
#st.write(formatted_prompt)
llm = OpenAI(temperature=0.9, openai_api_key="API KEY")
result = llm(formatted_prompt)

if input_content:
    st.write(result)
else:
    st.error("Error - provide the instruction in the box above")

#prompt = PromptTemplate(input_variables=[content,user_text],template=content)
