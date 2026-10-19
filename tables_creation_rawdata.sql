CREATE TABLE SCH
(
    ServiceConfirmationHeader VARCHAR(50) NOT NULL,
    EquipmentCode VARCHAR(50),
    ServiceTechnicianCode VARCHAR(20),
    MaterialCode VARCHAR(20),
    MaterialDescription VARCHAR(200),
    HeaderStatusCode VARCHAR(20),
    CreationTimestamp DATETIME2,
    EnergyTypeCode VARCHAR(10),
    CategoryCode VARCHAR(10),
    ProductTypeCode VARCHAR(20),
    ProductType1 VARCHAR(10),
    ProductType2 VARCHAR(10),
    ProductFamilyDescription VARCHAR(50),
    SkillProfileCode VARCHAR(10),
    EquipmentAge INT,
    LastMaintenanceDate DATE,

    CONSTRAINT PK_SCH
        PRIMARY KEY (ServiceConfirmationHeader)

--    CONSTRAINT FK_SCH_EQ
--        FOREIGN KEY (EquipmentCode)
--        REFERENCES EQ(EquipmentCode),

--    CONSTRAINT FK_SCH_SKILLS
--        FOREIGN KEY (ServiceTechnicianCode)
--        REFERENCES Skills(ServiceTechnicianCode),

--    CONSTRAINT FK_SCH_PROD
--        FOREIGN KEY (MaterialCode)
--        REFERENCES PROD(MaterialCode)
);

CREATE TABLE SCI
(
    ServiceConfirmationHeader VARCHAR(50) NOT NULL,
    ServiceConfirmationItem   VARCHAR(50) NOT NULL,
    ItemTypeCode              VARCHAR(10),
    StatusCode                VARCHAR(10),
    CreationTimestamp         DATETIME2,
    StartWork                 DATETIME2,
    EndWork                   DATETIME2,
    ActualDuration            INT,
    CONSTRAINT PK_SCI
        PRIMARY KEY
        (
            ServiceConfirmationHeader,
            ServiceConfirmationItem
        ),
--    CONSTRAINT FK_SCI_SCH
--        FOREIGN KEY (ServiceConfirmationHeader)
--        REFERENCES SCH(ServiceConfirmationHeader)
);


CREATE TABLE EQUIPMENT
(
    EquipmentCode      VARCHAR(50) NOT NULL,
    ProductCode        VARCHAR(50),
    ConstructionYear   INT,
    InstallerCode      VARCHAR(20),
    ManufacturerCode   VARCHAR(10),
    PowerCode          VARCHAR(20),
    FeukoLastYear      INT,
    WarrantyEndDate    DATE,
    StartUpDate        DATE,
    WarrantyStartDate  DATE,

    CONSTRAINT PK_EQUIPMENT
        PRIMARY KEY (EquipmentCode)

    --,CONSTRAINT FK_EQUIPMENT_PRODUCT
    --    FOREIGN KEY (ProductCode)
    --    REFERENCES PRODUCT(ProductCode)
);

			Cd Skill Profile	Cd Warengroup	Ds Material

CREATE TABLE PRODUCT
(
    MaterialCode         VARCHAR(50) NOT NULL,
    EnergyTypeCode       VARCHAR(10),
    ProductFamilyCode    VARCHAR(20),
    ProductTypeCode      VARCHAR(20),
    SkillProfileCode     VARCHAR(10),
    WarengroupCode       VARCHAR(10),
    MaterialDescription  VARCHAR(100),
    PowerMaxKW           INT,
    PowerMinKW           INT,
    PowerMaxLT           INT,
    RefrigerantFluid     VARCHAR(20),

    CONSTRAINT PK_PRODUCT
        PRIMARY KEY (MaterialCode)
);

CREATE TABLE SKILLS
(
    ResourceID   VARCHAR(20) NOT NULL,
    TeamCode     VARCHAR(20),
    SkillCode    VARCHAR(50),

    CONSTRAINT PK_SKILLS
        PRIMARY KEY
        (
            ResourceID,
            SkillCode
        ),
);