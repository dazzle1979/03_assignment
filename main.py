"""Assignment week 3. Output CPU and memory usage in JSON file and terminal (optional)."""
from os_resources import OsResources
from utilities import Utilities

def main():
    """Output CPU/memory usage to JSON or terminal."""
    args = Utilities.parse_arguments()
    data = {}

    if not args.no_cpu: 
        data["cpu"] = OsResources.get_cpu()
        if args.stdout:
            print(f"CPU: {data['cpu']}")

    if not args.no_memory:
        data["free_memory_perc"] = OsResources.get_free_mem_perc()
        mem_mb = data["free_memory_mb"] = OsResources.get_free_mem_mb()
        if args.stdout:
            print(f"Free memory: {data['free_memory_mb']}MB  ({data['free_memory_perc']}%)")

    Utilities.write_json(data)

if __name__ == "__main__":
    main()