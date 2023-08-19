{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "345cc861",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Administrator\\AppData\\Local\\Temp\\ipykernel_15044\\303165712.py:3: DtypeWarning: Columns (7,12,15,23) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  vdata=pd.read_csv(\"D:/data/2021VAERSDATA.csv\",encoding=\"iso-8859-1\")\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<bound method NDFrame.sample of         VAERS_ID    RECVDATE STATE  AGE_YRS  CAGE_YR  CAGE_MO SEX RPT_DATE  \\\n",
      "0         916600  01/01/2021    TX     33.0     33.0      NaN   F      NaN   \n",
      "1         916601  01/01/2021    CA     73.0     73.0      NaN   F      NaN   \n",
      "2         916602  01/01/2021    WA     23.0     23.0      NaN   F      NaN   \n",
      "3         916603  01/01/2021    WA     58.0     58.0      NaN   F      NaN   \n",
      "4         916604  01/01/2021    TX     47.0     47.0      NaN   F      NaN   \n",
      "...          ...         ...   ...      ...      ...      ...  ..      ...   \n",
      "749434   1997122  12/31/2021    NV     50.0     50.0      NaN   M      NaN   \n",
      "749435   1998663  12/31/2021    TN     83.0     83.0      NaN   F      NaN   \n",
      "749436   1998668  12/31/2021    SC      NaN      NaN      NaN   F      NaN   \n",
      "749437   2554159  12/31/2021    CA     49.0      NaN      NaN   M      NaN   \n",
      "749438   2594447  12/31/2021    PR     66.0     66.0      NaN   F      NaN   \n",
      "\n",
      "                                             SYMPTOM_TEXT DIED  ...  \\\n",
      "0       Right side of epiglottis swelled up and hinder...  NaN  ...   \n",
      "1       Approximately 30 min post vaccination administ...  NaN  ...   \n",
      "2       About 15 minutes after receiving the vaccine, ...  NaN  ...   \n",
      "3       extreme fatigue, dizziness,. could not lift my...  NaN  ...   \n",
      "4       Injection site swelling, redness, warm to the ...  NaN  ...   \n",
      "...                                                   ...  ...  ...   \n",
      "749434  Hives all over the body and swelling of the li...  NaN  ...   \n",
      "749435  She had a stroke on April 1st, 2021 while at t...    Y  ...   \n",
      "749436                                     Arm tenderness  NaN  ...   \n",
      "749437  He has been fully vaccinated with the Pfizer C...  NaN  ...   \n",
      "749438  DOSE ADMINISTERED AFTER BEING STORAGE FOR 30 D...  NaN  ...   \n",
      "\n",
      "                                                  CUR_ILL  \\\n",
      "0                                                    None   \n",
      "1       Patient residing at nursing facility. See pati...   \n",
      "2                                                    None   \n",
      "3                                        kidney infection   \n",
      "4                                                      Na   \n",
      "...                                                   ...   \n",
      "749434                                               None   \n",
      "749435  She had taken some shots for her back pain. Sh...   \n",
      "749436                                                NaN   \n",
      "749437                                                NaN   \n",
      "749438                                                NaN   \n",
      "\n",
      "                                                  HISTORY  \\\n",
      "0                                                    None   \n",
      "1       Patient residing at nursing facility. See pati...   \n",
      "2                                                    None   \n",
      "3       diverticulitis, mitral valve prolapse, osteoar...   \n",
      "4                                                     NaN   \n",
      "...                                                   ...   \n",
      "749434                                               None   \n",
      "749435  She had a stroke one week after taking the vac...   \n",
      "749436                                                NaN   \n",
      "749437  Medical History/Concurrent Conditions: Diabete...   \n",
      "749438                                                NaN   \n",
      "\n",
      "                                                PRIOR_VAX  \\\n",
      "0                                                     NaN   \n",
      "1                                                     NaN   \n",
      "2                                                     NaN   \n",
      "3       got measles from measel shot, mums from mumps ...   \n",
      "4                                                     NaN   \n",
      "...                                                   ...   \n",
      "749434                                                NaN   \n",
      "749435                                                NaN   \n",
      "749436                                                NaN   \n",
      "749437                                                NaN   \n",
      "749438                                                NaN   \n",
      "\n",
      "                        SPLTTYPE  FORM_VERS TODAYS_DATE BIRTH_DEFECT  \\\n",
      "0                            NaN          2  01/01/2021          NaN   \n",
      "1                            NaN          2  01/01/2021          NaN   \n",
      "2                            NaN          2  01/01/2021          NaN   \n",
      "3                            NaN          2  01/01/2021          NaN   \n",
      "4                            NaN          2  01/01/2021          NaN   \n",
      "...                          ...        ...         ...          ...   \n",
      "749434                       NaN          2  12/31/2021          NaN   \n",
      "749435                       NaN          2         NaN            Y   \n",
      "749436                       NaN          2  12/31/2021          NaN   \n",
      "749437  USPFIZER INC202101798458          2  12/28/2021          NaN   \n",
      "749438                       NaN          2  12/30/2021          NaN   \n",
      "\n",
      "       OFC_VISIT ER_ED_VISIT  \\\n",
      "0              Y         NaN   \n",
      "1              Y         NaN   \n",
      "2            NaN           Y   \n",
      "3            NaN         NaN   \n",
      "4            NaN         NaN   \n",
      "...          ...         ...   \n",
      "749434       NaN         NaN   \n",
      "749435         Y           Y   \n",
      "749436       NaN         NaN   \n",
      "749437       NaN         NaN   \n",
      "749438       NaN         NaN   \n",
      "\n",
      "                                                ALLERGIES  \n",
      "0                                       Pcn and bee venom  \n",
      "1                                                 \"Dairy\"  \n",
      "2                                               Shellfish  \n",
      "3       Diclofenac, novacaine, lidocaine, pickles, tom...  \n",
      "4                                                      Na  \n",
      "...                                                   ...  \n",
      "749434                                               None  \n",
      "749435  Allergic to iodine, penicillian and codene, su...  \n",
      "749436                                                NaN  \n",
      "749437                                                NaN  \n",
      "749438                                                NaN  \n",
      "\n",
      "[749439 rows x 35 columns]>\n",
      "<bound method NDFrame.sample of         VAERS_ID VAX_TYPE         VAX_MANU  VAX_LOT VAX_DOSE_SERIES VAX_ROUTE  \\\n",
      "0         910642  COVID19  PFIZER\\BIONTECH   EJ1685               1       NaN   \n",
      "1         916600  COVID19          MODERNA  037K20A               1        IM   \n",
      "2         916601  COVID19          MODERNA  025L20A               1        IM   \n",
      "3         916602  COVID19  PFIZER\\BIONTECH   EL1284               1        IM   \n",
      "4         916603  COVID19          MODERNA  unknown             UNK       NaN   \n",
      "...          ...      ...              ...      ...             ...       ...   \n",
      "793610   2666018  COVID19          MODERNA  004M20A               2        IM   \n",
      "793611   2666019  COVID19          MODERNA  027L20A               2        IM   \n",
      "793612   2666045  COVID19          MODERNA  039K20A               1        IM   \n",
      "793613   2666047  COVID19          MODERNA  039K20A               2        IM   \n",
      "793614   2666063  COVID19          MODERNA      NaN               1        IM   \n",
      "\n",
      "       VAX_SITE                             VAX_NAME  \n",
      "0            LA  COVID19 (COVID19 (PFIZER-BIONTECH))  \n",
      "1            LA          COVID19 (COVID19 (MODERNA))  \n",
      "2            RA          COVID19 (COVID19 (MODERNA))  \n",
      "3            LA  COVID19 (COVID19 (PFIZER-BIONTECH))  \n",
      "4           NaN          COVID19 (COVID19 (MODERNA))  \n",
      "...         ...                                  ...  \n",
      "793610       LA          COVID19 (COVID19 (MODERNA))  \n",
      "793611       LA          COVID19 (COVID19 (MODERNA))  \n",
      "793612       LA          COVID19 (COVID19 (MODERNA))  \n",
      "793613       LA          COVID19 (COVID19 (MODERNA))  \n",
      "793614       LA          COVID19 (COVID19 (MODERNA))  \n",
      "\n",
      "[793615 rows x 8 columns]>\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "vdata=pd.read_csv(\"D:/data/2021VAERSDATA.csv\",encoding=\"iso-8859-1\")\n",
    "vdata.sample(frac=0.9).to_csv(\"vdata_sample.csv\",index=False)\n",
    "print(vdata.sample)\n",
    "vax=pd.read_csv(\"D:/data/2021VAERSVAX.csv\",encoding=\"iso-8859-1\")\n",
    "vax.sample(frac=0.9).to_csv(\"vax_sample.csv\",index=False)\n",
    "print(vax.sample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "146deab2",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Administrator\\AppData\\Local\\Temp\\ipykernel_15044\\570575060.py:1: DtypeWarning: Columns (12,15) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  vdata=pd.read_csv(\"vdata_sample.csv\")\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        VAERS_ID    RECVDATE STATE  AGE_YRS  CAGE_YR  CAGE_MO SEX RPT_DATE  \\\n",
      "0        1598435  08/21/2021    NJ     40.0      NaN      NaN   F      NaN   \n",
      "1        1560753  08/15/2021    OR     65.0     65.0      NaN   M      NaN   \n",
      "2        1424194  06/24/2021   NaN     87.0     87.0      NaN   F      NaN   \n",
      "3        1929399  12/07/2021    MD     12.0     12.0      NaN   M      NaN   \n",
      "4         932529  01/10/2021    WA     41.0     41.0      NaN   F      NaN   \n",
      "...          ...         ...   ...      ...      ...      ...  ..      ...   \n",
      "674490   1200929  04/13/2021    CT     52.0     52.0      NaN   F      NaN   \n",
      "674491   1436108  06/30/2021   NaN     64.0      NaN      NaN   M      NaN   \n",
      "674492   1231316  04/19/2021    TX     22.0     22.0      NaN   F      NaN   \n",
      "674493   1346881  05/25/2021    RI     56.0     56.0      NaN   F      NaN   \n",
      "674494   1816477  10/26/2021    WA     43.0     43.0      NaN   F      NaN   \n",
      "\n",
      "                                             SYMPTOM_TEXT DIED  ... OFC_VISIT  \\\n",
      "0       pain in left arm; running down arm; pain is 10...  NaN  ...       NaN   \n",
      "1       Hives on left arm and lower chest area; Hives ...  NaN  ...       NaN   \n",
      "2       Patient presented to the ED and was subsequent...  NaN  ...       NaN   \n",
      "3       Client, was given pediatric Pfizer dose by RN ...  NaN  ...       NaN   \n",
      "4       About 5 min after getting the first dose, I fe...  NaN  ...       NaN   \n",
      "...                                                   ...  ...  ...       ...   \n",
      "674490  Chest pain/heartburn, pressure in left ear wit...  NaN  ...         Y   \n",
      "674491  \"wiped out\" for 3 days following the second do...  NaN  ...       NaN   \n",
      "674492  Mild rash starts in the upper thigh region ten...  NaN  ...       NaN   \n",
      "674493  So I had the injection on 4/2 by the middle of...  NaN  ...         Y   \n",
      "674494  12pm Sleepy  3-4pm Nauseous Feeling, slight he...  NaN  ...       NaN   \n",
      "\n",
      "       ER_ED_VISIT                                          ALLERGIES  \\\n",
      "0              NaN                                                NaN   \n",
      "1              NaN                                                NaN   \n",
      "2                Y                                                NaN   \n",
      "3              NaN                                                NaN   \n",
      "4              NaN                                               none   \n",
      "...            ...                                                ...   \n",
      "674490           Y                                                NKA   \n",
      "674491         NaN                                                NaN   \n",
      "674492         NaN                            None that I am aware of   \n",
      "674493         NaN  I'm allergic to everything. 100% all the way, ...   \n",
      "674494         NaN  Pencillian, avoid penicillin family, oral alle...   \n",
      "\n",
      "       VAX_TYPE         VAX_MANU  VAX_LOT VAX_DOSE_SERIES VAX_ROUTE VAX_SITE  \\\n",
      "0       COVID19          MODERNA      NaN               1        OT       LA   \n",
      "1       COVID19          MODERNA  007M20A             UNK        OT       LA   \n",
      "2       COVID19          MODERNA  unknown               1        IM       UN   \n",
      "3       COVID19  PFIZER\\BIONTECH   FK5127               1        IM       RA   \n",
      "4       COVID19  PFIZER\\BIONTECH      NaN               1       SYR       LA   \n",
      "...         ...              ...      ...             ...       ...      ...   \n",
      "674490  COVID19          JANSSEN  043AJ1A               1        IM       LA   \n",
      "674491  COVID19  PFIZER\\BIONTECH      NaN               2       NaN      NaN   \n",
      "674492  COVID19          MODERNA  037A21B               1       SYR       LA   \n",
      "674493  COVID19          JANSSEN  041A21A               1        IM       LA   \n",
      "674494  COVID19          MODERNA  039D21A               1       SYR       LA   \n",
      "\n",
      "                                   VAX_NAME  \n",
      "0               COVID19 (COVID19 (MODERNA))  \n",
      "1               COVID19 (COVID19 (MODERNA))  \n",
      "2               COVID19 (COVID19 (MODERNA))  \n",
      "3       COVID19 (COVID19 (PFIZER-BIONTECH))  \n",
      "4       COVID19 (COVID19 (PFIZER-BIONTECH))  \n",
      "...                                     ...  \n",
      "674490          COVID19 (COVID19 (JANSSEN))  \n",
      "674491  COVID19 (COVID19 (PFIZER-BIONTECH))  \n",
      "674492          COVID19 (COVID19 (MODERNA))  \n",
      "674493          COVID19 (COVID19 (JANSSEN))  \n",
      "674494          COVID19 (COVID19 (MODERNA))  \n",
      "\n",
      "[642689 rows x 42 columns]\n"
     ]
    }
   ],
   "source": [
    "vdata=pd.read_csv(\"vdata_sample.csv\")\n",
    "vax=pd.read_csv(\"vax_sample.csv\")\n",
    "vdata_with_vax=vdata.join(vax.set_index(\"VAERS_ID\"),on=\"VAERS_ID\",how=\"inner\")\n",
    "print(vdata_with_vax)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9ae76e60",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "674495"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(vdata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6f6351e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "714254"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(vax)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "69552200",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "642689"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(vdata_with_vax)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "206198ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        VAERS_ID    RECVDATE STATE  AGE_YRS  CAGE_YR  CAGE_MO SEX RPT_DATE  \\\n",
      "5        1872077  11/16/2021    MA      NaN      NaN      NaN   F      NaN   \n",
      "61       1311041  05/12/2021    CA     56.0     56.0      NaN   F      NaN   \n",
      "68       1872109  11/16/2021    FL     76.0     75.0      NaN   F      NaN   \n",
      "98       1071799  03/04/2021    PA     50.0     50.0      NaN   F      NaN   \n",
      "99       1075884  03/05/2021    CA     41.0     41.0      NaN   F      NaN   \n",
      "...          ...         ...   ...      ...      ...      ...  ..      ...   \n",
      "674463   1302530  05/10/2021    VT     33.0     33.0      NaN   F      NaN   \n",
      "674466   1482171  07/18/2021    OH     41.0      NaN      NaN   F      NaN   \n",
      "674476   1763909  10/06/2021    NC      NaN      NaN      NaN   M      NaN   \n",
      "674486    988620  01/29/2021    FL     78.0     78.0      NaN   M      NaN   \n",
      "674489   1460119  07/09/2021    FL     40.0     40.0      NaN   M      NaN   \n",
      "\n",
      "                                             SYMPTOM_TEXT DIED  ...  \\\n",
      "5       Very sick; Nauseated; Fever for 3 days; This s...  NaN  ...   \n",
      "61      In spite of being immunized against COVID-19, ...  NaN  ...   \n",
      "68      did not get 2nd dose; bad headache stopped aft...  NaN  ...   \n",
      "98      Patch of redness over the dorsum of the right ...  NaN  ...   \n",
      "99        redness, swelling, headache, soreness, weakness  NaN  ...   \n",
      "...                                                   ...  ...  ...   \n",
      "674463  Just over 48 hours after the vaccine, I got a ...  NaN  ...   \n",
      "674466  body aches; dizziness; pain at injection site;...  NaN  ...   \n",
      "674476  pressurized spray from the adjuvant vial hit h...  NaN  ...   \n",
      "674486  Pt complains of itching, redness, and bump at ...  NaN  ...   \n",
      "674489  Woke up with light sensitivity and head pressu...  NaN  ...   \n",
      "\n",
      "                    CUR_ILL  \\\n",
      "5                       NaN   \n",
      "61      Atrial Fibrillation   \n",
      "68                      NaN   \n",
      "98                      NaN   \n",
      "99                      NaN   \n",
      "...                     ...   \n",
      "674463                  NaN   \n",
      "674466                  NaN   \n",
      "674476                  NaN   \n",
      "674486                  NaN   \n",
      "674489                 None   \n",
      "\n",
      "                                                  HISTORY PRIOR_VAX  \\\n",
      "5                                                     NaN       NaN   \n",
      "61                                         Morbid Obesity       NaN   \n",
      "68      Medical History/Concurrent Conditions: COVID-1...       NaN   \n",
      "98                                           hypertension       NaN   \n",
      "99                                                    NaN       NaN   \n",
      "...                                                   ...       ...   \n",
      "674463                                      Asthma ExcemA       NaN   \n",
      "674466  Comments: List of non-encoded Patient Relevant...       NaN   \n",
      "674476                                                NaN       NaN   \n",
      "674486  Heart Attack, Heart Disease, Arthritis, Depres...       NaN   \n",
      "674489                                               None       NaN   \n",
      "\n",
      "                         SPLTTYPE  FORM_VERS TODAYS_DATE BIRTH_DEFECT  \\\n",
      "5       USMODERNATX, INC.MOD20213          2  11/15/2021          NaN   \n",
      "61                            NaN          2  05/12/2021          NaN   \n",
      "68      USMODERNATX, INC.MOD20213          2  11/15/2021          NaN   \n",
      "98                            NaN          2  03/04/2021          NaN   \n",
      "99                            NaN          2  03/05/2021          NaN   \n",
      "...                           ...        ...         ...          ...   \n",
      "674463                        NaN          2  05/10/2021          NaN   \n",
      "674466     USPFIZER INC2021340223          2  07/08/2021          NaN   \n",
      "674476  USGLAXOSMITHKLINEUS202120          2  10/05/2021          NaN   \n",
      "674486                        NaN          2  01/29/2021          NaN   \n",
      "674489                        NaN          2  07/09/2021          NaN   \n",
      "\n",
      "       OFC_VISIT ER_ED_VISIT               ALLERGIES  \n",
      "5            NaN         NaN                     NaN  \n",
      "61           NaN         NaN              Penicillin  \n",
      "68           NaN         NaN                     NaN  \n",
      "98             Y         NaN                    none  \n",
      "99           NaN         NaN                     NaN  \n",
      "...          ...         ...                     ...  \n",
      "674463       NaN         NaN  Penacillin Omaxacillin  \n",
      "674466       NaN         NaN                     NaN  \n",
      "674476       NaN         NaN                     NaN  \n",
      "674486       NaN           Y                    NKDA  \n",
      "674489         Y         NaN                    None  \n",
      "\n",
      "[64313 rows x 35 columns]\n"
     ]
    }
   ],
   "source": [
    "lost_vdata=vdata.loc[~vdata.index.isin(vdata_with_vax.index)]\n",
    "print(lost_vdata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e42df864",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RangeIndex(start=0, stop=674495, step=1)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
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
