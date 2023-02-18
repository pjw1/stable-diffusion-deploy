def my_streamlit_ui(state):
    import streamlit as st
    import requests
    import base64

    if "image" not in st.session_state:
        st.session_state.image = None
    col1, col2 = st.columns(2)

    with col1:
        if state.api_url:
            prompt = st.text_input("prompt here")
            generate_button = st.button("Generate image!")
            if generate_button:
                response = requests.post(f"{state.api_url}/api/predict", json={"prompt": prompt, "high_quality": "true"})
                image_string = response.json()["image"].replace("data:image/png;base64,", "")
                image = base64.b64decode(image_string)
                st.session_state.image = image
    
    with col2:
        if st.session_state.image:
            st.image(st.session_state.image)