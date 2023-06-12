import streamlit as st
# Import Chat completion template and set-up variables
# !pip install openai
import openai
import urllib.parse
import re

openai.api_key = "EMPTY" # Key is ignored and does not matter
openai.api_base = "http://34.132.127.197:8000/v1"

# Report issues
def raise_issue(e, model, prompt):
    issue_title = urllib.parse.quote("[bug] Hosted Gorilla: <Issue>")
    issue_body = urllib.parse.quote(f"Exception: {e}\nFailed model: {model}, for prompt: {prompt}")
    issue_url = f"https://github.com/ShishirPatil/gorilla/issues/new?assignees=&labels=hosted-gorilla&projects=&template=hosted-gorilla-.md&title={issue_title}&body={issue_body}"
    print(f"An exception has occurred: {e} \nPlease raise an issue here: {issue_url}")

# Query Gorilla server 
def get_gorilla_response(prompt="I would like to translate from English to French.", model="gorilla-7b-hf-v0"):
  try:
    with st.spinner('Wait for it...'):
        completion = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
        )
        # print(completion)
    st.success('Done!')
    return completion.choices[0].message.content
  except Exception as e:
    raise_issue(e, model, prompt)

def parse_response(text):
  # text = "<<<domain>>>: Multimodal Image-to-Text <<<api_call>>>: VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-small-stage1')"

  # Extract domain and API call using regular expression
  pattern = r"<<<(\w+)>>>:\s(.*?)(?=\n<<<\w+>>>:|\Z)"
  # pattern = r"<<<(\w+)>>>:\s(.*?)(?=\n<<<\w+>>>:|\Z)"
  matches = re.findall(pattern, text, re.DOTALL)
#   print(matches)

  data = {}
  for match in matches:
      data[match[0]] = match[1].strip()
  
  return data

def installation():
    # st.header("Installation")
    pass

def suggested_prompts():
    st.subheader("Example Prompts :")
    st.code("I would like to recognise text from captcha image\nI want to build a robot that can detecting objects in an image.\nI would like to translate from English to Chinese.")
    return 

def gorilla_llm():      
    installation()
    st.title("# Gorilla: Large Language Model Connected with Massive APIs [[Project Website](https://shishirpatil.github.io/gorilla/)]")
    text_input = st.text_area(
        "Text to analyze",
    )
    suggested_prompts()


    if text_input:
        # print("text_input",text_input)
        st.subheader("Response :")
        response = get_gorilla_response(text_input, model="gorilla-7b-hf-v0" )
        data = parse_response(response)
        st.markdown(f"Domain: {data.get('domain')}" )
        st.markdown(f"API Call: `{data.get('api_call')}`")
        st.markdown(f"API Provider: {data.get('api_provider')}")
        st.markdown(f"Explanation:\n {data.get('explanation')}")
    