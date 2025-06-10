# 🧮 π Approximation Algorithms

📌 *A comparative study of convergence and performance for classical and modern π (pi) approximation methods.*

---

## 📂 Overview

This Python project ([`main.py`](main.py)) implements and compares **five well-known infinite series algorithms** to approximate the value of π (pi). The code evaluates their **convergence speed** and **computational efficiency** for a given number of terms.

---

## ⚙️ Algorithms Implemented

The following mathematical methods are included:

| Method        | Description                                   |
|---------------|-----------------------------------------------|
| 🌀 **Leibniz**      | Simple alternating series (Gregory-Leibniz) |
| 🔺 **Nilakantha**   | Extension using product of three integers   |
| 📐 **Machin**       | Arctangent identity-based formula          |
| 🧠 **Ramanujan**    | High-precision series with fast convergence|
| 🧮 **BBP**          | Digit-extraction formula for π             |

> All algorithms compute π for a defined number of terms (`n_termos = 1000` by default).

---

## 📦 Dependencies

This project uses only Python's **standard libraries**:

- `decimal` (for high-precision math)
- `math` (basic mathematical functions)
- `time` (execution timing)

✅ **No external packages required!**

---

## 🚀 Usage

Run the script with:

```bash
python main.py
```

You will get a formatted comparison table:

### 💡 Sample Output

```
Método       Termos   π Aproximado         Erro Absoluto     Erro Percentual (%)    Tempo (s)
--------------------------------------------------------------------------------------------------------------
Leibniz      1000     3.140592653839794    0.000999999749999 0.031830980661         0.000334
Nilakantha   1000     3.141592653340544    0.000000000249249 0.000000007934         0.000364
Machin       1000     3.141592653589794    0.000000000000001 0.000000000000         0.001037
Ramanujan    1000     3.141592653589793    0.000000000000000 0.000000000000         2.265166
BBP          1000     3.141592653589793    0.000000000000000 0.000000000000         0.005808
```

---

## 📝 Notes

- The `decimal` module is configured with `getcontext().prec = 50` to ensure **high-precision** results, especially for **Ramanujan** and **BBP** formulas.
- 🐢 **Ramanujan**, despite being extremely accurate, has the **highest computational cost**.
- 🚀 **BBP and Machin** are fast and precise, even with low term counts.

---

## 👨‍💻 Author

This project was developed as part of a didactic and computational analysis on π approximations.  
📘 *For educational and research purposes.*

---

## 📄 License

This project is released under the **MIT License**.  
Feel free to use, modify, and share!

---
