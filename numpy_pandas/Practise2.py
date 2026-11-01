import pandas as pd

signups = pd.DataFrame({
    "email": ["a@shop.in", "b@shop.in", "a@shop.in", "c@shop.in",
              "b@shop.in", "d@shop.in", "c@shop.in", "e@shop.in"],
    "plan": ["Basic", "Pro", "Basic", "Basic", "Pro", "Pro", "Basic", "Basic"],
    "amount": [100, 300, 100, 100, 350, 300, 100, 100],
})

def dedupe_signups(df):
    rows_before = len(df)
    full_row_repeats = len(df) - len(df.drop_duplicates())
    email_repeats = len(df) - len(df.drop_duplicates(subset=["email"]))
    cleaned = df.drop_duplicates(subset=["email"], keep="first").copy()
    amount_before = df["amount"].sum()
    amount_after = cleaned["amount"].sum()

    print(f"Rows before: {rows_before}")
    print(f"Full-row repeats: {full_row_repeats}")
    print(f"Email repeats: {email_repeats}")
    print(f"Rows after: {len(cleaned)}")
    print(f"Amount before: {amount_before} | Amount after: {amount_after}")
    return cleaned

if __name__ == "__main__":
    result = dedupe_signups(signups)
    print(result)
