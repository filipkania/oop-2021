from CPUParser import CPUParser
from NVMEParser import NVMEParser

if __name__ == "__main__":
    cpu_stats = CPUParser("logs/cpu_intel.txt", freq_idle=800.025, freq_boosted=800.051)

    print(cpu_stats.cpu_temp())
    print(cpu_stats.cpu_mhz())

    cpu_stats = CPUParser("logs/cpu_amd.txt", freq_idle=800.025, freq_boosted=800.051)

    print(cpu_stats.cpu_temp())
    print(cpu_stats.cpu_mhz())

    nvme_stats = NVMEParser("logs/nvme.txt")
    print(nvme_stats.parse())
