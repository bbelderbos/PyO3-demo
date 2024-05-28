# PyO3 demo

Steps taken:

```
cargo new --lib sum_squares

# updated Cargo.toml
# added Rust code to src/lib.rs

# compile
python -m venv venv
source venv/bin/activate

(venv) pip install maturin
(venv) maturin develop (--release)

# script to compare Rust vs Python code
(venv) python test.py
```
