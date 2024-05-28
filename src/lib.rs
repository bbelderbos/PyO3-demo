use pyo3::prelude::*;

#[pyfunction]
fn sum_of_squares(n: u64) -> u64 {
    (1..=n).map(|x| x * x).sum()
}

#[pymodule]
fn sum_squares(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_of_squares, m)?)?;
    Ok(())
}
