function my(){
      
    var oh= document.getElementById('reports').getBoundingClientRect().height;
    document.getElementById('background').setAttribute("style",`height:${oh}px;`);
    }