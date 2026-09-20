function updatePreview(){
  const marks=[...document.querySelectorAll(".mark")].map(x=>parseFloat(x.value)||0);
  const total=marks.reduce((a,b)=>a+b,0);
  const percentage=marks.length ? total/marks.length : 0;
  let result=marks.some(m=>m<35) ? "Fail" : "Pass";
  let grade="F";
  if(result==="Pass"){
    if(percentage>=90) grade="A+";
    else if(percentage>=80) grade="A";
    else if(percentage>=70) grade="B+";
    else if(percentage>=60) grade="B";
    else if(percentage>=50) grade="C";
    else grade="D";
  }
  document.getElementById("total").textContent=`Total: ${total.toFixed(1)}/500`;
  document.getElementById("percentage").textContent=`Percentage: ${percentage.toFixed(2)}%`;
  document.getElementById("grade").textContent=`Grade: ${grade}`;
  document.getElementById("result").textContent=`Result: ${result}`;
}
document.querySelectorAll(".mark").forEach(x=>x.addEventListener("input",updatePreview));
updatePreview();
