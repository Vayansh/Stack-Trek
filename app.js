function my(){
      
    var oh= document.getElementById('reports').getBoundingClientRect().height;
    document.getElementById('background').setAttribute("style",`height:${oh}px;`);
    document.getElementById('report-back').setAttribute("style",`height: ${oh}px;`)    
}
const d = new Date(); 
const month = ["January","February","March","April","May","June","July","August","September","October","November","December"];
document.getElementById('date').innerHTML= "Date: "+d.getDate() + "-" +month[d.getMonth()] + "-" + d.getFullYear();
