function my(){
      
    var oh= document.getElementById('reports').getBoundingClientRect().height;
    document.getElementById('background').setAttribute("style",`height:${oh}px;`);
    document.getElementById('report-back').setAttribute("style",`height: ${oh}px;`)    
}
const d = new Date(); 
document.getElementById('date').innerHTML= "Date: "+d.getDay() + "-" +d.getMonth() + "-" + d.getFullYear();
