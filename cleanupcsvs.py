import pandas as pd

def clean_csv(CSV_PATH, OUTPUT_PATH):
    chunk_size = 50000
    num_files = 10
    for i in range(num_files):
        start = i * chunk_size
        column_names = pd.read_csv(CSV_PATH, nrows=1).columns
        df = pd.read_csv(CSV_PATH, skiprows=start, nrows=chunk_size)
        print(f"Processing chunk {i+1}/{num_files} of {CSV_PATH}")
        chunk = df
        chunk.to_csv(f"{OUTPUT_PATH}{i+1}.csv", mode='a', header=column_names, index=False)

if __name__ == "__main__":
    DFT_Path = "Magic Draft CSVs\\draft_data_public.DFT.PremierDraft.csv"
    DSK_Path = "Magic Draft CSVs\\draft_data_public.DSK.PremierDraft.csv"
    FDN_Path = "Magic Draft CSVs\\draft_data_public.FDN.PremierDraft.csv"
    PIO_Path = "Magic Draft CSVs\\draft_data_public.PIO.PremierDraft.csv"

    clean_csv(DFT_Path, "Magic Draft CSVs\\DFTS\\DFT")
    clean_csv(DSK_Path,"Magic Draft CSVs\\DSKS\\DSK")
    clean_csv(FDN_Path,"Magic Draft CSVs\\FDNS\\FDN")
    clean_csv(PIO_Path,"Magic Draft CSVs\\PIOS\\PIO")