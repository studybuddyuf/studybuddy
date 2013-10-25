function hide(id){
	
	if(id.value === "course") {
		document.getElementById("fahr").disabled=false;
		document.getElementById("cel").disabled=true;
		
		//	enable fahr
		document.buddySearch.fahr.style.color = "black";
		document.buddySearch.fahr.style.background = "#ECF8FF";

		//	disable cel
		document.buddySearch.cel.style.color = "#AAA";
		document.buddySearch.cel.style.background = "#DDD";
		
	}
	
	if(id.value === "name") {
		document.getElementById("cel").disabled=false;
		document.getElementById("fahr").disabled=true;
	
		//	enable cel
		document.buddySearch.cel.style.color = "black";
		document.buddySearch.cel.style.background = "#ECF8FF";

		//	disable fahr
		document.buddySearch.fahr.style.color = "#AAA";
		document.buddySearch.fahr.style.background = "#DDD";
	
	}
}