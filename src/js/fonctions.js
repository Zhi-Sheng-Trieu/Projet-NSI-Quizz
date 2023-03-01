function verifier(){
	var carLogin=document.getElementById("username").value.length;
	var carMdp=document.getElementById("mdp").value.length;
	
	if(carLogin==0){
		document.getElementById("username").style.borderColor = "red";
	}else{
		document.getElementById("username").style.borderColor = "";
	}
	
	if(carMdp<8){
		document.getElementById("mdp").style.borderColor = "red";
		alert("Il faut saisir un mot de passe faisant au moins 8 caractères.")
	}else{
		document.getElementById("mdp").style.borderColor = "";
	}
	if(carLogin>0 && carMdp>=8){
		document.getElementById("formulaire").onsubmit="return true";
	}
}

function border(){
		document.getElementById("login").style.borderColor = "";
}

function border2(){
		document.getElementById("mdp").style.borderColor = "";
}


