(function() {

	$('img').hover(
		function() {
			$(this).next().animate({width: 'toggle'}, 350)
				.parent().addClass('selected');
		}, function() {
			$(this).next().slideUp(600).parent().removeClass('selected');
	});	   

})();
