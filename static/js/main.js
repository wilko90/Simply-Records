$(document).ready(function() {
    $("#news-slider").owlCarousel({
        items:6,
        itemsDesktop:[1199,2],
        itemsDesktopSmall:[980,2],
        itemsMobile:[700,1],
        pagination:false,
        navigation:true,
        navigationText:["",""],
        autoPlay:true
    });
  
   /**
   *  Initializes Bootstrap toasts
   */
    $('.toast').toast('show');
});
