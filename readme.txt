Resolution-Refutation Theorem Prover

>> Introduction
   This repository contains Python implementations of a propositional logic theorem prover based on the resolution-refutation algorithm. The prover is presented as a search problem, with two different search strategies: uniform search and greedy search. The goal is to determine whether a given knowledge base (KB) entails a provided query.

>> File Structure
   greedy.py: Python script implementing the resolution-refutation algorithm with a greedy search strategy.
   uniform.py: Python script implementing the resolution-refutation algorithm with a uniform search strategy.
   README.md: Documentation file providing information about the assignment, code structure, usage, and analysis of results.

>> Choose the script based on the desired search strategy:
   For Uniform Search: python uniform.py
   For Greedy Search: python greedy.py
   Follow the prompts to input the KB, query, and mode.

>> Input Format:
   The first line contains two integers 'n' and 'm', representing the number of formulas in the KB and the mode.
   The next 'n' lines contain one formula per line.
   The last line contains the query that needs to be proved.

>> Output Format:

   If m = 0, the script prints only the result (integer value 0/1).
   If m = 1, the script first prints the resolution steps (one step per line), then prints the result.

>> Code Structure
   Parsing and CNF Conversion (convert_to_cnf, parse_formula):
   Formulas are parsed into a format suitable for resolution-refutation.
   Parsed formulas are converted into Conjunctive Normal Form (CNF) using the sympy library.
   KB Reformation (flatten_and_separate, split_at_or):
   Formulas in the KB are converted into CNF.
   Formulas are split at '&' to create a list of clauses.

>> Resolution Refutation (resolution, resolution_greedy):
   The resolution algorithm is implemented using both uniform and greedy search strategies.
   The is_resolvent function checks if two clauses can be resolved, and the heuristic function is used for greedy search.

>> Query Processing (process_query):
   The negation of the query is added to the KB to check for entailment.

>>Experiment Details
   Input Parameters:
   The number of nodes explored during resolution.
   Execution time for each resolution attempt.

>> Comparison of Search Strategies:
   Uniform Search (uniform.py) vs. Greedy Search (greedy.py).
   Time complexity and node exploration are analyzed for each test case.

>> Observations:
   Entailment results for each test case.
   Comparison of time and node exploration between uniform and greedy search.

>> Results and Analysis
   The results are presented in a tabular format, showing the entailment result, time taken, and nodes explored for each test case.
   Greedy search tends to explore fewer nodes in some cases, demonstrating the effectiveness of the heuristic in guiding the search towards faster convergence.
   Time complexity varies between the two search strategies, with uniform search performing better in certain scenarios.
   
>> Conclusion
   This resolution-refutation theorem prover provides a flexible and efficient implementation for checking entailment in propositional logic. The choice between uniform and greedy search can be made based on the specific characteristics of the knowledge base and query, as demonstrated by the experiment results.
