

# import pandas  as pd

# data ={'Product':['A','B','A','C','B'],
#        'Price':[10,15,12,20,18]}

# df =pd.DataFrame(data)

# print("Original data ",df) 

# #.............................One-hot encode th Porduct column...................................

# df_encoded =pd.get_dummies(df,columns=['Product'],drop_first=False)

# print("\n Data frame after One-hot encoding with pandas")

# print(df_encoded)


#..............................Initialize OneHotEncoder.................................................

# from sklearn.preprocessing import OneHotEncoder

# encode=OneHotEncoder(handle_unknown='ignore',sparse_output=False)

# #..................fit and transform the product column.........................
# product_encoder=encoder.fit_transform(df[['Product']])

# # Converting the encoded array back to a Datafrom for better readability

# product_df=pd.DataFrame(product_encoder,columns=encoder.get_feature_names_out(['Product']))

# #Concatenate with the Origial data fram 
# df_encoded_sklearn=pd.concat([df.drop('Product',axis=1),product_df],axis=1)

# print("\n DataFrame after one-hot-encoding withe scikit-learn :")

# print(df_encoded_sklearn)



#........................................................OneHotEncoder.......................................................................

# from sklearn.preprocessing import OneHotEncoder
# import pandas as pd

# # Initialize OneHotEncoder
# encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

# # Fit and transform the 'Product' column
# product_encoder = encoder.fit_transform(df[['Product']])

# # Convert the encoded array back to a DataFrame for better readability
# product_df = pd.DataFrame(product_encoder, columns=encoder.get_feature_names_out(['Product']))

# # Concatenate with the original DataFrame (drop the original 'Product' column)
# df_encoded_sklearn = pd.concat([df.drop('Product', axis=1).reset_index(drop=True), product_df], axis=1)

# # Display the final encoded DataFrame
# print("\nDataFrame after one-hot encoding with scikit-learn:")
# print(df_encoded_sklearn)


#.................................................................................................

# from sklearn.preprocessing import OneHotEncoder
# import pandas as pd
# import nltk

# sentence='''The cow is red 
#             the horses are brown
#             the dog is not cow'''
            
# word=nltk.word_tokenize(sentence)          
# df=pd.DataFrame(word)
# print(df) 


# df_encoded =pd.get_dummies(df)

# print("\n Data frame after One-hot encoding with pandas")

# print(df_encoded)
 
 
 
# #....................................................................................................

# # Step 1: Preprocess - lowercase & split into words
# words = sentence.lower().split()

# # Step 2: Reshape into 2D array (each word as a separate row)
# words_array = [[word] for word in words]

# # Step 3: Apply OneHotEncoder
# encoder = OneHotEncoder(sparse_output=False)
# encoded_words = encoder.fit_transform(words_array)

# # Step 4: Create DataFrame for better visualization
# encoded_df = pd.DataFrame(encoded_words, columns=encoder.get_feature_names_out(['word']))

# # Display
# print("One-hot encoded words:")
# print(encoded_df) 
 
 
#.........................................................................................

# onehot_encoder_app.py

import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

st.set_page_config(page_title="Word One-Hot Encoder", layout="centered")

st.title("🔤 Word-Level One-Hot Encoder using Scikit-Learn")

st.write("Enter a sentence below. The app will convert each word into one-hot encoded format.")

# User input
sentence = st.text_area("Enter your sentence here:", height=150)

if st.button("Encode"):
    if not sentence.strip():
        st.warning("Please enter a sentence before encoding.")
    else:
        # Step 1: Preprocess - lowercase & split into words
        words = sentence.lower().split()
        words_array = [[word] for word in words]  # 2D array for encoder

        # Step 2: One-hot encode
        encoder = OneHotEncoder(sparse_output=False)
        encoded = encoder.fit_transform(words_array)

        # Step 3: Convert to DataFrame
        encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['word']))
        encoded_df.insert(0, "Word", words)  # Insert original word for reference

        # Step 4: Display
        st.success("✅ One-hot encoding complete!")
        st.dataframe(encoded_df, use_container_width=True)
 
 