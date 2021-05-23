import pandas as pd
import thulac as thulac

cleaned_data = pd.read_csv("C:/Users/HectorPena/cleaned_data.csv", encoding="utf-8")
print(cleaned_data.shape[0])
cleaned_data.dropna(how='any', axis='index', inplace=True)

print(cleaned_data.shape[0])
tokenized = []
thu1 = thulac.thulac(seg_only=True)
for text in cleaned_data["cleaned_content"]:
    tokenized.append(thu1.cut(text, text=True))

tokenized_df = pd.DataFrame(tokenized)
tokenized_df.columns = ["tokenized_data"]
tokenized_data = pd.concat([cleaned_data, tokenized_df], axis=1, sort=False)
tokenized_data = tokenized_data.drop(columns=["cleaned_content"])
