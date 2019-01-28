(function(){
console.log('test');
var list_i = document.getElementsByTagName("code");
	for (var i = 0; i < list_i.length; i++ ){
		list_i[i].style.color = "blue";
		list_i[i].style.backgroundColor = "blue";
		list_i[i].addEventListener('click', function () {
      toggle_i_font(this);
		}, false);
	}
  var button_reset = document.getElementById("reset");
  button_reset.addEventListener('click', function() {
    make_all_i_font_unvisible();
  });
  
  function make_all_i_font_unvisible(){
  	location.relord();
  	/*
  	var list_i = document.getElementsByTagName("code");
  	for (var i = 0; i < list_i.length; i++ ){
  		list_i[i].style.color = "blue";
  	}
  	*/
  }
  function toggle_i_font(target){
    var style = window.getComputedStyle(target);
    var value = style.getPropertyValue("color");
    if (value === "rgb(255, 255, 255)"){
      target.style.color = "blue";
    }else{
      target.style.color = "white";
    }
  }
  })();
