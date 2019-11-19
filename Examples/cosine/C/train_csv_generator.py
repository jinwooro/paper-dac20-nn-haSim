import pandas as pd


features = pd.read_csv('./cos_data.csv')
print('The features have been successfully imported.')

turning_point =pd.DataFrame(columns=('Time','x_out','cstate','next_state'))
output =pd.DataFrame(columns=('Time','x_out','cstate','next_state'))


index = 0
x_out_prev = features.iloc[index]['x_out']
r = features.iloc[index]['r']
time = features.iloc[index]['Time']
cstate = 0
cstate_flag = 1

turning_point=turning_point.append(pd.DataFrame({'Time':[time],'x_out':[x_out_prev],'cstate':[cstate],'next_state':[r]}),ignore_index=True)

index = 1
x_out_curr = features.iloc[index]['x_out']

trend = x_out_curr - x_out_prev

index = 2

while index < features.shape[0]:
    x_out_prev = x_out_curr
    x_out_curr = features.iloc[index]['x_out']
    tmp_trend = x_out_curr - x_out_prev

    if tmp_trend * trend < 0:
        cstate = cstate + cstate_flag
        cstate_flag = cstate_flag * -1
        r = features.iloc[index - 1]['r']
        time = features.iloc[index - 1]['Time']
        turning_point=turning_point.append(pd.DataFrame({'Time':[time],'x_out':[x_out_prev],'cstate':[cstate],'next_state':[r]}),ignore_index=True)

    trend = tmp_trend
    index = index + 1

index = 0
index_turning_point = 0

while index < features.shape[0]:
    r = features.iloc[index]['r']
    time = features.iloc[index]['Time']
    x_out = features.iloc[index]['x_out']
    if time == turning_point.iloc[index_turning_point]['Time']:
        index_turning_point = index_turning_point + 1
        if index_turning_point >= turning_point.shape[0]:
            break
    output=output.append(pd.DataFrame({'Time':[time],'x_out':[x_out],'cstate':[turning_point.iloc[index_turning_point-1]['cstate']]\
            ,'next_state':[turning_point.iloc[index_turning_point]['Time'] - time]}),ignore_index=True)
    index = index + 1

output.to_csv('train_data_large.csv', index=0)
