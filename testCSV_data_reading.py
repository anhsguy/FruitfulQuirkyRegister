import pandas as pd


# read csv> dataframe> get 'frame number' column /recorded_time> frame rate
class FrameData:
    def __init__(self, csv, record_time):
        self.csv = csv
        self.record_time = record_time
        self.df = self.csv_df()

    def csv_df(self):
        df = pd.read_csv(self.csv)
        df['TF'] = df.index
        print(df.head())
        return df

    def frame_number(self):
        frame_num = self.df['Frame number']
        f_l = list(frame_num)
        f_l=[int(x) for x in f_l]
        print([f_l[-1], f_l[0]])
        f_delta_l = []
        for i in range(len(f_l)-1):
            f_delta=f_l[i+1]-f_l[i]
            f_delta_l.append(f_delta)
        print(f_delta_l)
        return f_delta_l



