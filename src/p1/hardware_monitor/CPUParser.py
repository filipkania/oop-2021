import re
from collections import defaultdict
from Parser import Parser

intel_temp_regex = re.compile(r'Core\s\d*:\s*\+(\d*.\d*).*')
amd_temp_regex = re.compile(r'Tdie:\s*.(\d*\.\d*).*')

mhz_regex = re.compile(r'cpu MHz\s*:\s(\d*.\d*)')


class CPUParser(Parser):
    data: str

    freq_idle: float
    freq_boosted: float

    def __init__(self, filename: str, freq_idle: float, freq_boosted: float):
        self.data = open(filename).read()

        self.freq_idle = freq_idle
        self.freq_boosted = freq_boosted

    def cpu_temp(self) -> float:
        temps = intel_temp_regex.findall(self.data) or amd_temp_regex.findall(self.data)
        assert temps

        return sum(map(float, temps)) / len(temps)

    def cpu_mhz(self) -> dict[str, float]:
        results = mhz_regex.findall(self.data)
        d = defaultdict(int)

        for f in map(float, results):
            if f <= self.freq_idle:
                d["idle"] += 1
            elif f >= self.freq_boosted:
                d["boosted"] += 1
            else:
                d["normal"] += 1

        return {k: d[k] / len(results) * 100 for k in ["idle", "boosted", "normal"]}
