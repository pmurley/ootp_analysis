from enum import Enum


class Personality(Enum):
    Personable = 0
    Easygoing = 1
    Normal = 2
    Temperamental = 3
    Controlling = 4


class ManagementStyle(Enum):
    NoStyleGiven = 0
    Conventional = 1
    Sabermetric = 2
    Smallball = 3
    Unorthodox = 4


class Position(Enum):
    Manager = 1
    BenchCoach = 2
    GeneralManager = 3
    PitchingCoach = 4
    HittingCoach = 5
    ScoutingDirector = 6
    Trainer = 8
    Owner = 9
    BaseCoach = 10


class Occupation(Enum):
    GeneralManager = 1
    Manager = 2
    BenchCoach = 3
    PitchingCoach = 4
    HittingCoach = 5
    ScoutingDirector = 6
    TrainerJob = 12
    Owner = 13
    FirstBaseCoach = 14
    ThirdBaseCoach = 15
