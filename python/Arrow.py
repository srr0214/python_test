{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9451bc26",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Administrator\\AppData\\Local\\Temp\\ipykernel_2520\\3540773805.py:8: DtypeWarning: Columns (7,12,15,23) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  vdata_pd=pd.read_csv(\"D:/data/2021VAERSDATA.csv\",encoding=\"iso-8859-1\")\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 749439 entries, 0 to 749438\n",
      "Data columns (total 35 columns):\n",
      " #   Column        Non-Null Count   Dtype  \n",
      "---  ------        --------------   -----  \n",
      " 0   VAERS_ID      749439 non-null  int64  \n",
      " 1   RECVDATE      749439 non-null  object \n",
      " 2   STATE         637160 non-null  object \n",
      " 3   AGE_YRS       668499 non-null  float64\n",
      " 4   CAGE_YR       600833 non-null  float64\n",
      " 5   CAGE_MO       4267 non-null    float64\n",
      " 6   SEX           749439 non-null  object \n",
      " 7   RPT_DATE      871 non-null     object \n",
      " 8   SYMPTOM_TEXT  749148 non-null  object \n",
      " 9   DIED          10558 non-null   object \n",
      " 10  DATEDIED      9391 non-null    object \n",
      " 11  L_THREAT      11115 non-null   object \n",
      " 12  ER_VISIT      127 non-null     object \n",
      " 13  HOSPITAL      47479 non-null   object \n",
      " 14  HOSPDAYS      31215 non-null   float64\n",
      " 15  X_STAY        378 non-null     object \n",
      " 16  DISABLE       11967 non-null   object \n",
      " 17  RECOVD        676198 non-null  object \n",
      " 18  VAX_DATE      693706 non-null  object \n",
      " 19  ONSET_DATE    683599 non-null  object \n",
      " 20  NUMDAYS       655040 non-null  float64\n",
      " 21  LAB_DATA      279899 non-null  object \n",
      " 22  V_ADMINBY     749439 non-null  object \n",
      " 23  V_FUNDBY      940 non-null     object \n",
      " 24  OTHER_MEDS    412769 non-null  object \n",
      " 25  CUR_ILL       326967 non-null  object \n",
      " 26  HISTORY       437705 non-null  object \n",
      " 27  PRIOR_VAX     36321 non-null   object \n",
      " 28  SPLTTYPE      220045 non-null  object \n",
      " 29  FORM_VERS     749439 non-null  int64  \n",
      " 30  TODAYS_DATE   743953 non-null  object \n",
      " 31  BIRTH_DEFECT  460 non-null     object \n",
      " 32  OFC_VISIT     144356 non-null  object \n",
      " 33  ER_ED_VISIT   90161 non-null   object \n",
      " 34  ALLERGIES     364617 non-null  object \n",
      "dtypes: float64(5), int64(2), object(28)\n",
      "memory usage: 1.4 GB\n",
      "Total690MB\n"
     ]
    }
   ],
   "source": [
    "#01 \n",
    "##调用python的包：\n",
    "import gzip              #提供压缩包\n",
    "import pandas as pd\n",
    "from pyarrow import csv   #调用pyarrow中的csv\n",
    "import pyarrow.compute as pc\n",
    "##读文件(pandas)：\n",
    "vdata_pd=pd.read_csv(\"D:/data/2021VAERSDATA.csv\",encoding=\"iso-8859-1\")\n",
    "columns=list(vdata_pd.columns)\n",
    "vdata_pd.info(memory_usage=\"deep\") #1.4 GB\n",
    "##读文件(Arrow):\n",
    "vdata_arrow=csv.read_csv(\"D:/data/2021VAERSDATA.csv\")\n",
    "tot_bytes=sum([vdata_arrow[name].nbytes\n",
    "             for name in vdata_arrow.column_names])   #计算每列大小然后求和\n",
    "print(f\"Total{tot_bytes//(1024**2)}MB\")  #Total690MB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "350cfc67",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "VAERS_ID int64 5 int64 5\n",
      "RECVDATE string 10 object 47\n",
      "STATE string 4 object 39\n",
      "AGE_YRS double 5 float64 5\n",
      "CAGE_YR int64 5 float64 5\n",
      "CAGE_MO double 5 float64 5\n",
      "SEX string 3 object 41\n",
      "RPT_DATE string 2 object 22\n",
      "SYMPTOM_TEXT binary 457 object 495\n",
      "DIED string 2 object 23\n",
      "DATEDIED string 2 object 23\n",
      "L_THREAT string 2 object 23\n",
      "ER_VISIT string 2 object 22\n",
      "HOSPITAL string 2 object 24\n",
      "HOSPDAYS int64 5 float64 5\n",
      "X_STAY string 2 object 22\n",
      "DISABLE string 2 object 23\n",
      "RECOVD string 3 object 39\n",
      "VAX_DATE string 9 object 46\n",
      "ONSET_DATE string 9 object 45\n",
      "NUMDAYS int64 5 float64 5\n",
      "LAB_DATA binary 27 object 54\n",
      "V_ADMINBY string 5 object 42\n",
      "V_FUNDBY string 2 object 22\n",
      "OTHER_MEDS binary 22 object 51\n",
      "CUR_ILL binary 8 object 36\n",
      "HISTORY binary 21 object 52\n",
      "PRIOR_VAX binary 4 object 25\n",
      "SPLTTYPE string 7 object 32\n",
      "FORM_VERS int64 5 int64 5\n",
      "TODAYS_DATE string 9 object 47\n",
      "BIRTH_DEFECT string 2 object 22\n",
      "OFC_VISIT string 2 object 26\n",
      "ER_ED_VISIT string 2 object 25\n",
      "ALLERGIES binary 9 object 38\n"
     ]
    }
   ],
   "source": [
    "#02\n",
    "##比较pandas和arrow之间列的内存和类型的区别：\n",
    "for name in vdata_arrow.column_names:  \n",
    "    arr_bytes=vdata_arrow[name].nbytes   #元素消耗的总字节数\n",
    "    arr_type=vdata_arrow[name].type      #每列的数据类型\n",
    "    pd_bytes=vdata_pd[name].memory_usage(index=False,deep=True)   #内存大小\n",
    "    pd_type=vdata_pd[name].dtype                                  #每列的数据类型\n",
    "    print(name,\n",
    "        arr_type,arr_bytes//(1024**2),\n",
    "        pd_type,pd_bytes//(1024**2))     #发现pd_object所占内存大"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "81ac47ed",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<magic-timeit>:1: DtypeWarning: Columns (7,12,15,23) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "<magic-timeit>:1: DtypeWarning: Columns (7,12,15,23) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "<magic-timeit>:1: DtypeWarning: Columns (7,12,15,23) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "<magic-timeit>:1: DtypeWarning: Columns (7,12,15,23) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "<magic-timeit>:1: DtypeWarning: Columns (7,12,15,23) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "<magic-timeit>:1: DtypeWarning: Columns (7,12,15,23) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "<magic-timeit>:1: DtypeWarning: Columns (7,12,15,23) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "<magic-timeit>:1: DtypeWarning: Columns (7,12,15,23) have mixed types. Specify dtype option on import or set low_memory=False.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7.71 s ± 233 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)\n",
      "1.46 s ± 82.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)\n"
     ]
    }
   ],
   "source": [
    "#03\n",
    "##pandas arrow时间的对比\n",
    "%timeit pd.read_csv(\"D:/data/2021VAERSDATA.csv\", encoding=\"iso-8859-1\") #7.71 s\n",
    "%timeit csv.read_csv(\"D:/data/2021VAERSDATA.csv\") #1.46 s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "fe32fe25",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Administrator\\AppData\\Local\\Temp\\ipykernel_2520\\630728529.py:4: DtypeWarning: Columns (7,12,15,23) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  vdata_pd=pd.read_csv(\"D:/data/2021VAERSDATA.csv\",encoding=\"iso-8859-1\",usecols=lambda x:x!=\"SYMPTOM_TEXT\") #定义不读哪一列\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 749439 entries, 0 to 749438\n",
      "Data columns (total 34 columns):\n",
      " #   Column        Non-Null Count   Dtype  \n",
      "---  ------        --------------   -----  \n",
      " 0   VAERS_ID      749439 non-null  int64  \n",
      " 1   RECVDATE      749439 non-null  object \n",
      " 2   STATE         637160 non-null  object \n",
      " 3   AGE_YRS       668499 non-null  float64\n",
      " 4   CAGE_YR       600833 non-null  float64\n",
      " 5   CAGE_MO       4267 non-null    float64\n",
      " 6   SEX           749439 non-null  object \n",
      " 7   RPT_DATE      871 non-null     object \n",
      " 8   DIED          10558 non-null   object \n",
      " 9   DATEDIED      9391 non-null    object \n",
      " 10  L_THREAT      11115 non-null   object \n",
      " 11  ER_VISIT      127 non-null     object \n",
      " 12  HOSPITAL      47479 non-null   object \n",
      " 13  HOSPDAYS      31215 non-null   float64\n",
      " 14  X_STAY        378 non-null     object \n",
      " 15  DISABLE       11967 non-null   object \n",
      " 16  RECOVD        676198 non-null  object \n",
      " 17  VAX_DATE      693706 non-null  object \n",
      " 18  ONSET_DATE    683599 non-null  object \n",
      " 19  NUMDAYS       655040 non-null  float64\n",
      " 20  LAB_DATA      279899 non-null  object \n",
      " 21  V_ADMINBY     749439 non-null  object \n",
      " 22  V_FUNDBY      940 non-null     object \n",
      " 23  OTHER_MEDS    412769 non-null  object \n",
      " 24  CUR_ILL       326967 non-null  object \n",
      " 25  HISTORY       437705 non-null  object \n",
      " 26  PRIOR_VAX     36321 non-null   object \n",
      " 27  SPLTTYPE      220045 non-null  object \n",
      " 28  FORM_VERS     749439 non-null  int64  \n",
      " 29  TODAYS_DATE   743953 non-null  object \n",
      " 30  BIRTH_DEFECT  460 non-null     object \n",
      " 31  OFC_VISIT     144356 non-null  object \n",
      " 32  ER_ED_VISIT   90161 non-null   object \n",
      " 33  ALLERGIES     364617 non-null  object \n",
      "dtypes: float64(5), int64(2), object(27)\n",
      "memory usage: 965.0 MB\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "list.remove(x): x not in list",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[23], line 7\u001b[0m\n\u001b[0;32m      5\u001b[0m vdata_pd\u001b[38;5;241m.\u001b[39minfo(memory_usage\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdeep\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;66;03m# 965.0 MB\u001b[39;00m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;66;03m###arrow:\u001b[39;00m\n\u001b[1;32m----> 7\u001b[0m columns\u001b[38;5;241m.\u001b[39mremove(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSYMPTOM_TEXT\u001b[39m\u001b[38;5;124m\"\u001b[39m)  \u001b[38;5;66;03m#移出哪一列\u001b[39;00m\n\u001b[0;32m      8\u001b[0m vdata_arrow \u001b[38;5;241m=\u001b[39m csv\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mD:/data/2021VAERSDATA.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m,convert_options\u001b[38;5;241m=\u001b[39mcsv\u001b[38;5;241m.\u001b[39mConvertOptions(include_columns\u001b[38;5;241m=\u001b[39mcolumns))\n\u001b[0;32m      9\u001b[0m vdata_arrow\u001b[38;5;241m.\u001b[39mnbytes\n",
      "\u001b[1;31mValueError\u001b[0m: list.remove(x): x not in list"
     ]
    }
   ],
   "source": [
    "#04\n",
    "##不加载某一列：\n",
    "###pandas:\n",
    "vdata_pd=pd.read_csv(\"D:/data/2021VAERSDATA.csv\",encoding=\"iso-8859-1\",usecols=lambda x:x!=\"SYMPTOM_TEXT\") #定义不读哪一列\n",
    "vdata_pd.info(memory_usage=\"deep\") # 965.0 MB\n",
    "###arrow:\n",
    "columns.remove(\"SYMPTOM_TEXT\")  #移出哪一列\n",
    "vdata_arrow = csv.read_csv(\"D:/data/2021VAERSDATA.csv\",convert_options=csv.ConvertOptions(include_columns=columns))\n",
    "vdata_arrow.nbytes  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b5462b34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 749439 entries, 0 to 749438\n",
      "Data columns (total 34 columns):\n",
      " #   Column        Non-Null Count   Dtype  \n",
      "---  ------        --------------   -----  \n",
      " 0   VAERS_ID      749439 non-null  int64  \n",
      " 1   RECVDATE      749439 non-null  object \n",
      " 2   STATE         749439 non-null  object \n",
      " 3   AGE_YRS       668499 non-null  float64\n",
      " 4   CAGE_YR       600833 non-null  float64\n",
      " 5   CAGE_MO       4267 non-null    float64\n",
      " 6   SEX           749439 non-null  object \n",
      " 7   RPT_DATE      749439 non-null  object \n",
      " 8   DIED          749439 non-null  object \n",
      " 9   DATEDIED      749439 non-null  object \n",
      " 10  L_THREAT      749439 non-null  object \n",
      " 11  ER_VISIT      749439 non-null  object \n",
      " 12  HOSPITAL      749439 non-null  object \n",
      " 13  HOSPDAYS      31215 non-null   float64\n",
      " 14  X_STAY        749439 non-null  object \n",
      " 15  DISABLE       749439 non-null  object \n",
      " 16  RECOVD        749439 non-null  object \n",
      " 17  VAX_DATE      749439 non-null  object \n",
      " 18  ONSET_DATE    749439 non-null  object \n",
      " 19  NUMDAYS       655040 non-null  float64\n",
      " 20  LAB_DATA      749439 non-null  object \n",
      " 21  V_ADMINBY     749439 non-null  object \n",
      " 22  V_FUNDBY      749439 non-null  object \n",
      " 23  OTHER_MEDS    749439 non-null  object \n",
      " 24  CUR_ILL       749439 non-null  object \n",
      " 25  HISTORY       749439 non-null  object \n",
      " 26  PRIOR_VAX     749439 non-null  object \n",
      " 27  SPLTTYPE      749439 non-null  object \n",
      " 28  FORM_VERS     749439 non-null  int64  \n",
      " 29  TODAYS_DATE   749439 non-null  object \n",
      " 30  BIRTH_DEFECT  749439 non-null  object \n",
      " 31  OFC_VISIT     749439 non-null  object \n",
      " 32  ER_ED_VISIT   749439 non-null  object \n",
      " 33  ALLERGIES     749439 non-null  object \n",
      "dtypes: float64(5), int64(2), object(27)\n",
      "memory usage: 1.2 GB\n"
     ]
    }
   ],
   "source": [
    "#05\n",
    "##将arrow的数据加载到pandas，需要转换数据结构：\n",
    "vdata=vdata_arrow.to_pandas() #由arrow转为pandas\n",
    "vdata.info(memory_usage=\"deep\") #1.2 GB\n",
    "#在转pandas时，arrow可以自毁，从而节约内存：\n",
    "vdata=vdata_arrow.to_pandas(self_destruct=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
