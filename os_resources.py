"""Module containing OsResource Class."""
import psutil

class OsResources:
    """Class for fetching cpu and memory statistics."""
    
    @classmethod
    def get_cpu(cls):
        """Get CPU percentage."""
        cpu_perc = psutil.cpu_percent(interval=1)
        return cpu_perc

    @classmethod
    def get_free_mem_perc(cls):
        """Get memory percentage."""
       memory_used_perc = psutil.virtual_memory().percent
       return memory_used_perc

    @classmethod
    def get_free_mem_mb(cls):
        """Get free memory in MBs"""
        memory_used_mb = psutil.virtual_memory().free / 1024 /1024
        return memory_used_mb