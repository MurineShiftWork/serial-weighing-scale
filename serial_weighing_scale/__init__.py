import warnings

warnings.warn(
    "serial-weighing-scale is deprecated and will receive no further updates. "
    "Use serial-scale-hx711 (Arduino+HX711) or serial-scale-bench (RS-232/USB bench scales) instead: "
    "https://github.com/MurineShiftWork/serial-scale-hx711",
    DeprecationWarning,
    stacklevel=2,
)
