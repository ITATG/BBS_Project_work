from sqlalchemy import URL, create_engine
import pandas as pd

server = "crm-data.database.windows.net"
database = "rawdata-test"
username = "INSERT USERNAME HERE"
password = "INSERT PASSWORD HERE"

connection_url = URL.create(
    "mssql+pymssql",
    username=username,
    password=password,
    host=server,
    database=database
)

engine = create_engine(connection_url)

with engine.connect() as conn:
    print("Connection OK")

config = {

    "SCH": {
        "table": "SCH",
        "mapping": {
            "Cd Service Confirmation Num": "ServiceConfirmationHeader",
            "Cd Equipment" : "EquipmentCode",
            "Cd Exc Service Employee": "ServiceTechnicianCode",
            "Cd Material": "MaterialCode",
            "Ds Material" : "MaterialDescription",
            "Cd Status Header": "HeaderStatusCode",
            "Dt Creation Date Timestamp": "CreationTimestamp",
            "Cd Energy Type": "EnergyTypeCode",
            "Cd Category": "CategoryCode",
            "Cd Product Family": "ProductTypeCode",
            "Cd Product Type 1": "ProductType1",
            "Cd Product Type 2": "ProductType2",
            "Ds Product Family": "ProductFamilyDescription",
            "Cd Skill Profile": "SkillProfileCode",
            "EQ_Age": "EquipmentAge",
            "Last maintenance date": "LastMaintenanceDate",
        }
    },

    "SCI": {
        "table": "SCI",
        "mapping": {
            "Cd Service Confirmation Num": "ServiceConfirmationHeader",
            "Cd Service Confirmation Item": "ServiceConfirmationItem",
            "Cd Item Type": "ItemTypeCode",
            "Cd Status Item": "StatusCode",
            "Dt Creation Date Timestamp": "CreationTimestamp",
            "Dt Start Work Date and Time": "StartWork",
            "Dt End Work Date and Time": "EndWork",
            "Qt Act Duration": "ActualDuration"
        }
    },

    "EQ": {
        "table": "EQUIPMENT",
        "mapping": {
            "Cd Equipment": "EquipmentCode",
            "Cd Product": "ProductCode",
            "Cd Constr Year": "ConstructionYear",
            "Cd Eq Installer": "InstallerCode",
            "Cd Eq Manufacturer": "ManufacturerCode",
            "Cd Eq Power": "PowerCode",
            "Cd Feuko Last Year": "FeukoLastYear",
            "Dt End Warranty": "WarrantyEndDate",
            "Dt Start Up": "StartUpDate",
            "Dt Start Warranty": "WarrantyStartDate",
        }
    },

    "PROD": {
        "table": "PRODUCT",
        "mapping": {
            "Cd Material": "MaterialCode",
            "Cd Energy Type": "EnergyTypeCode",
            "Cd Product Family": "ProductFamilyCode",
            "Cd Product Type 2": "ProductTypeCode",
            "Cd Skill Profile": "SkillProfileCode",
            "Cd Warengroup": "WarengroupCode",
            "Ds Material": "MaterialDescription",
            "Nr Power Max Kw": "PowerMaxKW",
            "Nr Power Max Lt": "PowerMinKW",
            "Nr Power Min Kw": "PowerMaxLT",
            "Nr Refrigerant Fluid": "RefrigerantFluid",
        }
    },

    "Skills": {
            "table": "SKILLS",
            "mapping": {
                "resourceId": "ResourceId",
                "parentResourceId": "TeamCode",
                "workSkill": "SkillCode"
            }
        }
}
for sheet_name, cfg in config.items():

    print(f"Elaborating {sheet_name}")

    df = pd.read_excel(
        r"C:\Users\bordo\OneDrive - Bologna Business School\Documenti\Project Work\lorenzo_bordoni - SC Linked to EQ + Product and ST Skills.xlsx",
        sheet_name=sheet_name,
        usecols=list(cfg["mapping"].keys())
    )

    # Trasformazioni specifiche dello sheet
    if sheet_name == "SCH":
        df["Cd Exc Service Employee"] = (
            df["Cd Exc Service Employee"]
            .astype(str)
            .str.removeprefix("ZP")
        )

    # Rinomina colonne Excel -> SQL
    df = df.rename(columns=cfg["mapping"])

    print(df.head())
    # drop empty rows 
    df = df.dropna(how="all")
    # Load into SQL
    df.to_sql(
        name=cfg["table"],
        con=engine,
        if_exists="append",
        index=False,
        chunksize=1000
    )

    print(f"{len(df)} record loaded into table {cfg['table']}")


