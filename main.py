# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



###################################################
# import modules
import pandas as pd
import os
import glob


###################################################
# directory setting
current_directory = os.getcwd()
print(current_directory)

path = 'C:/Users/USER/Desktop/aptEnergy'
os.chdir(path)
path_dataProcessing = os.path.join(path, r'dataProcessing')

if not os.path.exists(path_dataProcessing):
   os.makedirs(path_dataProcessing)

##################################################
open files by folders

path = 'C:/Users/USER/Desktop/aptEnergy'
sub_path = os.path.join(path + "/국토부실거래가", r'transaction_APT')
sub_folders = [name for name in os.listdir(sub_path) if os.path.isdir(os.path.join(sub_path, name))]
# print(sub_folders)

# Define an empty dictionary to store the DataFrames
dfs = []
stacked_dfs = []

# read file names in the folder
for folder in sub_folders:
    sub_path_folder = sub_path + '/' + folder
    transaction_files = glob.glob(os.path.join(sub_path_folder, "*.csv"))

    for f in transaction_files:
        # get df name from description line
        with open(f, 'r', encoding='cp949') as file:
            for line in file:
                if '계약일자' in line:
                    contract_date = line.split(':')[-1].strip()[:4]
                    # print(contract_date)
                    break
                    dfName = "df" + "contract_date"
            # Set the DataFrame name dynamically using the contract date
            df_name = "df" + contract_date
            # Read in the DataFrame from the CSV file
            df = pd.read_csv(f, header=0, skiprows=15, encoding='cp949')
            df.name = df_name
            # print(df['계약년월'].unique())
            dfs.append(df)

    # df_names = [df.name for df in dfs]
    # sorted_names = sorted(df_names)
    # print(sorted_names)
    stacked_df = pd.concat(dfs, axis=0)
    stacked_df.name = folder

    stacked_dfs.append(stacked_df)
    # print(stacked_df)
    # stacked_dfs.append(stacked_df)
# print(list(stacked_dfs))

stacked_dfs_names = [stacked_df.name for stacked_df in stacked_dfs]
sorted_stacked_names = sorted(stacked_dfs_names)
aptTransactionData = pd.concat(stacked_dfs, axis=0)
for name in sorted_stacked_names:
        print(name)

# print(stacked_df)
# print(stacked_df.info())

file_path = os.path.join(path + '/dataProcessing', 'aptTransactionData.csv')
aptTransactionData.to_csv(file_path, index=False, sep = ",")


##################################################
난방비 등 정보, 출처: k-apt

path = 'C:/Users/USER/Desktop/aptEnergy'
path_aptEnergyUseData = path+'/energyUseData'
energyUseData_files = glob.glob(os.path.join(path_aptEnergyUseData, "*.xlsx"))

# print(list(energyUseData_files))

df15 = pd.read_excel(energyUseData_files[0], skiprows=[0])
df16 = pd.read_excel(energyUseData_files[1], skiprows=[0])
df17 = pd.read_excel(energyUseData_files[2], skiprows=[0])
df18 = pd.read_excel(energyUseData_files[3], skiprows=[0])
df19 = pd.read_excel(energyUseData_files[4], skiprows=[0])
df20 = pd.read_excel(energyUseData_files[5], skiprows=[0])
df21 = pd.read_excel(energyUseData_files[6])
df22 = pd.read_excel(energyUseData_files[7])

dfs = [df15, df16, df17, df18, df19, df20, df21, df22]

aptEnergyUseData = pd.concat(dfs, axis=0, ignore_index=True)

file_path = os.path.join(path + '/dataProcessing', 'aptEnergyUseData.csv')
aptEnergyUseData.to_csv(file_path, index=False, sep = ",")


##################################################
관리비공개의무단지 기본정보, 출처: k-apt

path = 'C:/Users/USER/Desktop/aptEnergy'
path_aptInfoFromKAPT = path+'/aptData/'
aptInfoKAPT = pd.read_excel(path_aptInfoFromKAPT+"20230201_단지_기본정보.xlsx", skiprows=[0])
aptInfoKAPTSubset = aptInfoKAPT[[
 '단지코드',
 '세대수',
 '법정동주소',
 '도로명주소',
 '분양세대수',
 '임대세대수',
 '관리방식',
 '난방방식',
 '사용승인일',
 '최고층수',
 '최고층수(건축물대장상)',
 '지하층수',
 '건물구조',
 '전기-수전용량',
 '전기-세대전기계약방식',
 '전기안전관리자선임여부',
 '화재수신반방식',
 '급수방식']]

file_path = os.path.join(path + '/dataProcessing', 'aptInfoKAPT.csv')
aptInfoKAPTSubset.to_csv(file_path, index=False, sep = ",")



###################################################
총괄표제부 / 아니면, 건축인허가 기본개요, 출처: 세움터

path = 'C:/Users/USER/Desktop/aptEnergy'
path_aptInfoFromSeumteo = path+'/aptData/'
names = pd.read_csv(path_aptInfoFromSeumteo+"mart_djy_02ColumnNames.txt", sep = ",", engine='python', encoding = 'UTF-8')
colNames = list(names.columns)

#open apt info data
seumteodf = pd.read_csv(path_aptInfoFromSeumteo+"mart_djy_02.txt", sep = "|", engine='python', encoding = "cp949", header=None)
seumteodf.columns = colNames

#seumteodf['주_용도_코드_명'].unique()
aptInfoSeumteo = seumteodf[seumteodf['주_용도_코드_명']=='공동주택']

file_path = os.path.join(path + '/dataProcessing', 'aptInfoSeumteo.csv')
aptInfoSeumteo.to_csv(file_path, index=False, sep = ",")

###################################################
## 현재까지 완료 ##
###################################################







# ###################################################
# # import modules
# import pandas as pd
# import os
# import glob
#
#
# ###################################################
# # directory setting
# current_directory = os.getcwd()
# print(current_directory)
#
# path = 'C:/Users/USER/Desktop/aptEnergy/국토부실거래가'
# os.chdir(path)
# path_dataProcessing = os.path.join(path, r'dataProcessing')
#
# if not os.path.exists(path_dataProcessing):
#    os.makedirs(path_dataProcessing)
#
# ###################################################
# # open files by folders
#
# sub_path = os.path.join(path, r'transaction_APT')
# sub_folders = [name for name in os.listdir(sub_path) if os.path.isdir(os.path.join(sub_path, name))]
# # print(sub_folders)
#
# # Define an empty dictionary to store the DataFrames
# dfs = []
#
# # read file names in the folder
# for folder in sub_folders:
#     sub_path_folder = sub_path + '/' + folder
#     transaction_files = glob.glob(os.path.join(sub_path_folder, "*.csv"))
#
# # open all files in the folder
# for f in transaction_files:
#     # get df name from description line
#     with open(f, 'r', encoding='cp949') as file:
#         for line in file:
#             if '계약일자' in line:
#                 contract_date = line.split(':')[-1].strip()[:4]
#                 print(contract_date)
#                 break
#                 dfName = "df" + "contract_date"
#         # Set the DataFrame name dynamically using the contract date
#         df_name = "df" + contract_date
#         # Read in the DataFrame from the CSV file
#         df = pd.read_csv(f, header=0, skiprows=15, encoding='cp949')
#         df.name = df_name
#         dfs.append(df)
#
# df_names = [df.name for df in dfs]
# sorted_names = sorted(df_names)
#
# for name in sorted_names:
#     print(name)
#
# # stack all dataframe as one
# stacked_df = pd.concat(dfs, axis=0)
# print(stacked_df)




# # open all files in the folder
# for f in transaction_files:
#     # get df name from description line
#     with open(f, 'r', encoding='cp949') as file:
#         for line in file:
#             if '계약일자' in line:
#                 contract_date = line.split(':')[-1].strip()[:4]
#                 print(contract_date)
#                 break
#                 dfName = "df" + "contract_date"
#         # Set the DataFrame name dynamically using the contract date
#         df_name = "df" + contract_date
#         # Read in the DataFrame from the CSV file
#         df = pd.read_csv(f, header=0, skiprows=15, encoding='cp949')
#         df.name = df_name
#         dfs.append(df)
#
# df_names = [df.name for df in dfs]
# sorted_names = sorted(df_names)
#
# for name in sorted_names:
#     print(name)
#
# # stack all dataframe as one
# stacked_df = pd.concat(dfs, axis=0)
# print(stacked_df)
# #
# import os
# import glob
# import pandas as pd
#
# # Directory where the folders are located
# base_path = 'C:/Users/USER/Desktop/aptEnergy/국토부실거래가'
#
# # Get the folder names
# folder_names = [name for name in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, name))]
#
# # Loop over the folder names
# for folder_name in folder_names:
#     # Path to the current folder
#     folder_path = os.path.join(base_path, folder_name)
#
#     # List of CSV files in the folder
#     csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
#
#     # List to store the DataFrames for this folder
#     dfs = []
#
#     # Loop over the CSV files
#     for csv_file in csv_files:
#         # Read the CSV file into a DataFrame
#         df = pd.read_csv(csv_file, header=0, skiprows=15, encoding='cp949')
#
#         # Add the DataFrame to the list
#         dfs.append(df)
#
#     # Concatenate the DataFrames into a single DataFrame
#     stacked_df = pd.concat(dfs, axis=0)
#
#     # Set the name of the stacked DataFrame to the folder name
#     stacked_df.name = folder_name
#
#     # Print the stacked DataFrame
#     print(stacked_df)