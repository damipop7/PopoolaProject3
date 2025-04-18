class ResultsWriter:
    @staticmethod
    def save_timing_results(load_factors, results, filename="timing_results.txt"):
        with open(filename, 'w') as f:
            f.write("Load Factor Analysis Results\n")
            f.write("==========================\n\n")
            
            f.write("Successful Searches:\n")
            f.write("-----------------\n")
            for lf, time in zip(load_factors, results['successful']):
                f.write(f"Load Factor: {lf:.3f}, Time: {time:.6f}\n")
            
            f.write("\nUnsuccessful Searches:\n")
            f.write("-------------------\n")
            for lf, time in zip(load_factors, results['unsuccessful']):
                f.write(f"Load Factor: {lf:.3f}, Time: {time:.6f}\n")