$(document).ready(function() {

//alert("enteerd");
	$(".sensors-view").css("display","block");
	$(".previousData-view").css("display","none");
	$("ul li a").click(function(){ 
			$(".sensors-view").css("display","none");
	$(".previousData-view").css("display","none");
			var p=$(this).attr("class");
			$("."+p+"-view").css("display","block");
			//alert(p);

});



$("div input:button").click(function(){


	var my = $(this).attr("class");
	//alert(my);
	var o= "."+my+"_graph";
	//alert(o);
	$("svg g").css("display","none");
	$("svg polyline").css("display","none");
	$("svg .grid").css("display","block");
	$(o).css("display","block");
	$("svg input").css("backround","silver");
	$(this).css("backround","#a5eab2");
});






});

