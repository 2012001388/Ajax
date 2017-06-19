$(function(){
	$('button').click(function(){
		var city=$("#cityname").val();
		$.ajax({
			url:'get_city_weather',
			data:$('form').serialize(),
			type:'POST',
			success:function(response){
				document.getElementById('weather').disabled=false;
				document.getElementById('weather').value=response;
			},
			error:function(console){
				console.log(error)
			}
		});
	});
});