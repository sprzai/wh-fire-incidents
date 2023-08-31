-- Crear tabla de dimensión de período de tiempo
CREATE TABLE DimTime (
    TimeKey SERIAL PRIMARY KEY,
    IncidentDate DATE
);

-- Crear tabla de dimensión de distrito
CREATE TABLE DimDistrict (
    DistrictKey SERIAL PRIMARY KEY,
    DistrictName VARCHAR(255)
);

-- Crear tabla de dimensión de batallón
CREATE TABLE DimBattalion (
    BattalionKey SERIAL PRIMARY KEY,
    BattalionName VARCHAR(255)
);

-- Crear tabla de hechos
CREATE TABLE FactIncidents (
    IncidentKey SERIAL PRIMARY KEY,
    TimeKey INT REFERENCES DimTime(TimeKey),
    DistrictKey INT REFERENCES DimDistrict(DistrictKey),
    BattalionKey INT REFERENCES DimBattalion(BattalionKey),
    IncidentNumber VARCHAR(255),
    ExposureNumber VARCHAR(255),
    ID VARCHAR(255),
    Address VARCHAR(255),
    IncidentDate DATE,
    CallNumber VARCHAR(255),
    AlarmDtTm TIMESTAMP,
    ArrivalDtTm TIMESTAMP,
    CloseDtTm TIMESTAMP,
    City VARCHAR(255),
    Zipcode VARCHAR(10),
    StationArea VARCHAR(255),
    Box VARCHAR(255),
    SuppressionUnits INT,
    SuppressionPersonnel INT,
    EMSUnits INT,
    EMSPersonnel INT,
    OtherUnits INT,
    FirstUnitOnScene VARCHAR(255),
    EstimatedPropertyLoss NUMERIC,
    EstimatedContentsLoss NUMERIC,
    FireFatalities INT,
    FireInjuries INT,
    CivilianFatalities INT,
    CivilianInjuries INT,
    NumberOfAlarms INT,
    PrimarySituation VARCHAR(255),
    MutualAid VARCHAR(255),
    ActionTakenPrimary VARCHAR(255),
    ActionTakenSecondary VARCHAR(255),
    ActionTakenOther VARCHAR(255),
    DetectorAlertedOccupants VARCHAR(255),
    PropertyUse VARCHAR(255),
    AreaOfFireOrigin VARCHAR(255),
    IgnitionCause VARCHAR(255),
    IgnitionFactorPrimary VARCHAR(255),
    IgnitionFactorSecondary VARCHAR(255),
    HeatSource VARCHAR(255),
    ItemFirstIgnited VARCHAR(255),
    HumanFactorsAssociatedWithIgnition VARCHAR(255),
    StructureType VARCHAR(255),
    StructureStatus VARCHAR(255),
    FloorOfFireOrigin INT,
    FireSpread VARCHAR(255),
    NoFlameSpread VARCHAR(255),
    NumberOfFloorsWithMinimumDamage INT,
    NumberOfFloorsWithSignificantDamage INT,
    NumberOfFloorsWithHeavyDamage INT,
    NumberOfFloorsWithExtremeDamage INT,
    DetectorsPresent VARCHAR(255),
    DetectorType VARCHAR(255),
    DetectorOperation VARCHAR(255),
    DetectorEffectiveness VARCHAR(255),
    DetectorFailureReason VARCHAR(255),
    AutomaticExtinguishingSystemPresent VARCHAR(255),
    AutomaticExtinguishingSystemType VARCHAR(255),
    AutomaticExtinguishingSystemPerformance VARCHAR(255),
    AutomaticExtinguishingSystemFailureReason VARCHAR(255),
    NumberOfSprinklerHeadsOperating INT,
    SupervisorDistrict VARCHAR(255),
    NeighborhoodDistrict VARCHAR(255),
    Point VARCHAR(255)
);
