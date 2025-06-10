
````markdown
# π Approximation Algorithms

This Python project (`main.py`) implements and compares five well-known infinite series algorithms used to approximate the value of π (pi). The code evaluates their convergence speed and computational efficiency for a given number of terms.

## Algorithms Implemented

The following mathematical methods are included:

- **Leibniz Series** (Gregory-Leibniz)
- **Nilakantha Series**
- **Machin's Formula** (based on arctangent identities)
- **Ramanujan Series** (high-precision series)
- **Bailey–Borwein–Plouffe (BBP) Formula**

All series compute an approximation of π for a defined number of terms (`n_termos`), which is set to `1000` by default. The results include the computed π value, absolute and percentage errors compared to the `math.pi` reference, and computation time.

## Dependencies

- Python 3.6+
- `decimal` module (standard library, for high-precision calculations)
- `math` module (standard library)
- `time` module (standard library)

## Usage

To run the script:

```bash
python main.py
````

The output will be a formatted table showing:

* Method name
* Number of terms
* Approximated value of π
* Absolute error
* Percentage error
* Execution time in seconds

### Example Output

```
Método       Termos   π Aproximado         Erro Absoluto     Erro Percentual (%)    Tempo (s)
--------------------------------------------------------------------------------------------------------------
Leibniz      1000     3.140592653839794    0.000999999749999 0.031830980661         0.000334
Nilakantha   1000     3.141592653340544    0.000000000249249 0.000000007934         0.000364
Machin       1000     3.141592653589794    0.000000000000001 0.000000000000         0.001037
Ramanujan    1000     3.141592653589793    0.000000000000000 0.000000000000         2.265166
BBP          1000     3.141592653589793    0.000000000000000 0.000000000000         0.005808
```

## Notes

* The `decimal` module is used with increased precision (`getcontext().prec = 50`) to ensure accurate calculations in Ramanujan and BBP formulas.
* Despite its high accuracy, the Ramanujan algorithm is computationally heavier compared to others, especially at high term counts.

## Author

This project was developed as part of a comparative study on the convergence and computational performance of classical and modern π approximation algorithms.

## License

This project is released under the MIT License.

```

