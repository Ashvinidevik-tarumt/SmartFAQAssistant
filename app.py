import streamlit as st

# Title and Heading
st.title("Smart FAQ Assistant for Heart, Lung, and Blood Health")
st.header("This is a header")
st.write("""
    Ask questions related to heart, lung, and blood health topics, and get answers from our dataset.
    """)

# Input and Output
# Create text input for user to ask a question
user_question = st.text_input("Ask your question:")
#name = st.text_input("Enter your name:", value="Type here")
#if st.button("Submit"):
    #st.write(f"Hello, {name}! I love TAR UMT! ")

# Display an Image
#from PIL import Image
#image = Image.open("tarumt.png")  # Replace with your image path
#st.image(image, caption="TAR UMT, Beyond Education!")
# Button to trigger the question-answering process
if st.button("Get Answer"):

    if user_question.strip() == "":
        st.write("Please enter a question.")
    else:
        # Generate embedding for the user's question
        user_embedding = model.encode([user_question])

        # Compute cosine similarity between the user's question and all the questions in the dataset
        cosine_similarities = cosine_similarity(user_embedding, embeddings)

        # Get the index of the most similar question
        most_similar_idx = np.argmax(cosine_similarities)

        # Get the similarity score
        similarity_score = cosine_similarities[0][most_similar_idx]

        # Define a threshold for relevance (you can adjust this threshold based on your experimentation)
        threshold = 0.7  # You can tweak this value

        if similarity_score >= threshold:
            answer = df.iloc[most_similar_idx]['Answer']
            st.write(f"Answer: {answer}")
            st.write(f"Similarity Score: {similarity_score:.2f}")
        else:
            st.write("I apologize, but I don't have information on that topic yet. Could you please ask other questions?")

# Optional: Add a clear button to reset the input field
if st.button("Clear"):
    st.experimental_rerun()
