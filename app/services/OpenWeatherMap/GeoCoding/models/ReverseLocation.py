from pydantic import BaseModel


class LocalNames(BaseModel):
    af: str
    ar: str
    ascii: str
    az: str
    bg: str
    ca: str
    da: str
    de: str
    el: str
    en: str
    eu: str
    fa: str
    feature_name: str
    fi: str
    fr: str
    gl: str
    he: str
    hi: str
    hr: str
    hu: str
    id: str
    it: str
    ja: str
    la: str
    lt: str
    mk: str
    nl: str
    no: str
    pl: str
    pt: str
    ro: str
    ru: str
    sk: str
    sl: str
    sr: str
    th: str
    tr: str
    vi: str
    zu: str


class ReverseLocation(BaseModel):
    name: str
    local_names: LocalNames
    lat: float
    lon: float
    country: str
