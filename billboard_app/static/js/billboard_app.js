$(document).ready(function() {
        if ($('.messageOne').length) {
        	console.log('visible')
            $(".collapse-form").hide()
        }

    $("#add").click(function() {
		$(".error-container").hide();
        $(".collapse-form").show();
	});



    });