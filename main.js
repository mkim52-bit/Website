function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}

function BarGraph(response){
response = JSON.parse(response)
var layout = {
  title:"Cities By Suicide Rates",
  xaxis:{title:"Suicide Rates"},
  yaxis:{title:"Cities"}
  
}

Plotly.newPlot(document.getElementById("bar"),response,layout)
}


function PieGraph(response){
response = JSON.parse(response)
var layout = {
  title:"Suicide Rates By Year",
  
}
Plotly.newPlot(document.getElementById("pie"), response,layout);
}

function post(){
  ajaxPostRequest("/makePie2", JSON.stringify({"Key":"value"}), PieGraph);
  
}

function postR(){
  ajaxPostRequest("/makePie3", JSON.stringify({"Key":"value"}), PieGraph);
}

function postB2(){
  ajaxPostRequest("/makeBar2", JSON.stringify({"Bar":2}), BarGraph);
}

function postBR(){
  ajaxPostRequest("/makeBarR", JSON.stringify({"Bar":2}), BarGraph);
}


  




function getData(){
ajaxGetRequest("/makeBar",BarGraph);
ajaxGetRequest("/makePie",PieGraph);


}
