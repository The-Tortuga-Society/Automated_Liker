
function autoLikeArchives() {
    // Wait a bit for the page to fully load
	var actionDelay = 2000 + 4000*Math.random();
    setTimeout(() => {
        // Find the like button - Substack typically uses a heart icon


					var elList = document.querySelectorAll('a[aria-label*="Like"]');
					elList.forEach(function(el) {
						if (el.getAttribute('aria-pressed') === 'true' ) {
							// this is already liked
							   console.log('This is already liked');
							   
						} else {
							// go ahead and like this one with delay
							   actionDelay+=430 + 3000*Math.random();
							   console.log('Not already liked');
							   setTimeout(() => {
							   console.log(el);
							   el.click();
						       console.log('Substack post liked!');
							   }, actionDelay); // additional delay to ensure likes don't collide
							   }
						   
					});					



    }, actionDelay); // millisecond delay to ensure page elements are loaded
}


autoLikeArchives();
