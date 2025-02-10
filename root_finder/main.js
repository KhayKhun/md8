
function cleanInputString(s) {
    return s
      .replace(/\*\*/g, "^")
      .trim();
  }

  function parseFunction(funcStr) {
    try {
      return math.compile(funcStr);
    } catch (error) {
      alert("Invalid function syntax. Please check your input.");
      return null;
    }
  }
  
  function bisectionMethod(func, start, end, epsilon) {
    let iterations = 0;
    let errors = [];
    let mid = start;
  
    while ((end - start) / 2 > epsilon) {
      mid = (start + end) / 2;
      let fMid = func.evaluate({ x: mid });
      let fStart = func.evaluate({ x: start });
  
      if (Math.abs(fMid) < epsilon) break;
  
      if (fStart * fMid < 0) {
        end = mid;
      } else {
        start = mid;
      }
  
      iterations++;
      errors.push(Math.abs(fMid));
    }
  
    return { root: mid, iterations, errors };
  }

  function newtonsMethod(func, funcDeriv, x0, epsilon) {
    let iterations = 0;
    let errors = [];
    let x = x0;
    let prevX;
  
    while (iterations < 100) {
      let fx = func.evaluate({ x: x });
      let fpx = funcDeriv.evaluate({ x: x });
  
      if (Math.abs(fpx) < epsilon) {
        alert("Derivative is too small. Newton's Method cannot proceed. Try another interval or function.");
        return { root: null, iterations, errors };
      }
  
      prevX = x;
      x = x - fx / fpx;
  
      errors.push(Math.abs(x - prevX));
  
      if (Math.abs(x - prevX) < epsilon) break;
      iterations++;
    }
  
    return { root: x, iterations, errors };
  }
  
  let chart = null;

  function plotGraph(bisecErrors, newtonErrors) {
    const ctx = document.getElementById("chart").getContext("2d");
  
    if (chart) {
      chart.destroy();
    }
  
    chart = new Chart(ctx, {
      type: "line",
      data: {
        labels: [...Array(Math.max(bisecErrors.length, newtonErrors.length)).keys()],
        datasets: [
          {
            label: "Bisection Method",
            data: bisecErrors,
            borderColor: "blue",
            fill: false
          },
          {
            label: "Newton's Method",
            data: newtonErrors,
            borderColor: "red",
            fill: false
          }
        ]
      },
      options: {
        scales: {
          y: {
            type: "logarithmic", // show in detail
            title: { display: true, text: "Error (log scale)" }
          },
          x: {
            title: { display: true, text: "Iteration" }
          }
        }
      }
    });
  }
  

  function findRoots() {
    let funcStr = document.getElementById("function").value;
    let start = parseFloat(document.getElementById("start").value);
    let end = parseFloat(document.getElementById("end").value);
    let epsilon = parseFloat(document.getElementById("precision").value);
  
    if (!funcStr) {
      alert("Please enter a function.");
      return;
    }
    if (isNaN(start) || isNaN(end) || isNaN(epsilon)) {
      alert("Please enter valid numerical values for start, end, and epsilon.");
      return;
    }
    if (start >= end) {
      alert("Start value must be less than End value.");
      return;
    }
    if (epsilon <= 0) {
      alert("Epsilon (precision) must be a positive number.");
      return;
    }
  
    funcStr = cleanInputString(funcStr);
  
    const func = parseFunction(funcStr);
    if (!func) return; 
  
    // 5. Check if there's a sign change in [start, end] for Bisection
    const fStart = func.evaluate({ x: start });
    const fEnd = func.evaluate({ x: end });
    if (fStart * fEnd > 0) {
      alert("No sign change detected in the given interval. Bisection might fail. Try a different interval.");
    }
  
    let derivativeStr;
    let funcDeriv;
    try {
      derivativeStr = math.derivative(funcStr, "x").toString();
      funcDeriv = parseFunction(derivativeStr);
    } catch (error) {
      alert("Failed to compute derivative. Please check your function.");
      return;
    }
  
    // Bisection Method
    const bisecResult = bisectionMethod(func, start, end, epsilon);
    const bisectRootStr = bisecResult.root ? bisecResult.root.toFixed(6) : "N/A";
  
    document.getElementById("bisectionResult").innerHTML =
      `Bisection Method: Root ≈ ${bisectRootStr}, Iterations: ${bisecResult.iterations}`;
  
    // Newton's Method (with initial guess at midpoint)
    const newtonResult = newtonsMethod(func, funcDeriv, (start + end) / 2, epsilon);
    const newtonRootStr = newtonResult.root
      ? newtonResult.root.toFixed(6)
      : "N/A";
  
    document.getElementById("newtonResult").innerHTML =
      `Newton's Method: Root ≈ ${newtonRootStr}, Iterations: ${newtonResult.iterations}`;
      plotGraph(bisecResult.errors, newtonResult.errors);
  }