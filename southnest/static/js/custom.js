// Template Name: Food Heaven HTML
// Version: 1.0.0
// Author: Webstrot 

// Preloader js
$(window).on('load', function () {
    $("#status").fadeOut();
    $("#preloader").delay(450).fadeOut("slow");
});

$('.dropdown').on('show.bs.dropdown', function(e){
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown(300);
  });
$('.dropdown').on('hide.bs.dropdown', function(e){
  $(this).find('.dropdown-menu').first().stop(true, true).slideUp(200);
});

$(document).ready(function($) {
  // When the window resizes
    var mastHeight = $('.header').outerHeight();
    $('.searchBox').css('top', mastHeight); 
    $('.mainHeader .navbar div#collapsibleNavbar').css('top', mastHeight); 
    $('.professionalSec').css('padding-top', mastHeight); 
    $('.fishFarming').css('margin-top', mastHeight); 
    $('.cartSideBox').css('top', mastHeight); 

    var topHeaderHeight = $('.topHeader').outerHeight();
    $('.headerThree #collapsibleNavbar').css('top', topHeaderHeight); 
});

// active search
$(".searchBtn").click(function(){
  $(".searchBox").toggleClass("active");
});

// active cart side Box
$(".cardBtn").click(function(){
  $(".cartSideBox").toggleClass("active");
});
$(".closeCart").click(function(){
  $(".cartSideBox").toggleClass("active");
});
var buttonPlus  = $(".qty-btn-plus");
var buttonMinus = $(".qty-btn-minus");

var incrementPlus = buttonPlus.click(function() {
  var $n = $(this)
  .parent(".qty-container")
  .find(".input-qty");
  $n.val(Number($n.val())+1 );
});

var incrementMinus = buttonMinus.click(function() {
  var $n = $(this)
  .parent(".qty-container")
  .find(".input-qty");
  var amount = Number($n.val());
  if (amount > 0) {
    $n.val(amount-1);
  }
});

$(document).ready(function(){
  $(".navbar-nav .dropdown").hover(            
      function() {
          $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).slideDown("400");
          $(this).toggleClass('open');        
      },
      function() {
          $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).slideUp("400");
          $(this).toggleClass('open');       
      }
  );
});


$(function() { // Dropdown toggle
  $(document).click(function(e) 
  { 
  var target = e.target; 
  if (!$(target).is('.searchBtn, .searchBoxInner ') && !$(target).parents().is('.searchBtn, .searchBoxInner ')) 
  //{ $('.dropdown').hide(); }
    {  $(".searchBox.active").removeClass("active"); }
  });
});

$(function() { // Dropdown toggle
  $(document).click(function(e) 
  { 
  var target = e.target; 
  if (!$(target).is('.cartSideBox, .cardBtn') && !$(target).parents().is('.cartSideBox, .cardBtn')) 
  //{ $('.dropdown').hide(); }
  {  $(".cartSideBox.active").removeClass("active"); }
  });
});

// $(window).scroll(function(){
//   if ($(this).scrollTop() > 50) {
//       $('.headerTwo').addClass('headerActive');
//   } else {
//       $('.headerTwo').removeClass('headerActive');
//   }
// });

$(document).ready(function($) {
  // When the window resizes
    var mastHeight = $('.headerThree').outerHeight();
    $('.logoFullHeight, .cartIcon').css('height', mastHeight); 
});



// Animation on Scroll using jQuery

$(document).on("scroll", function () {
  var pageTop = $(document).scrollTop()
  var pageBottom = pageTop + $(window).height()
  var tags = $(".fadein")

  for (var i = 0; i < tags.length; i++) {
    var tag = tags[i]

    if ($(tag).offset().top < pageBottom) {
      $(tag).addClass("visible")
    } else {
      $(tag).removeClass("visible")
    }
  }
})



// cursor

// UPDATE: I was able to get this working again... Enjoy!

var cursor = document.querySelector('.cursor');
var cursorinner = document.querySelector('.cursor2');
var a = document.querySelectorAll('a');

document.addEventListener('mousemove', function(e){
  var x = e.clientX;
  var y = e.clientY;
  cursor.style.transform = `translate3d(calc(${e.clientX}px - 50%), calc(${e.clientY}px - 50%), 0)`
});

document.addEventListener('mousemove', function(e){
  var x = e.clientX;
  var y = e.clientY;
  cursorinner.style.left = x + 'px';
  cursorinner.style.top = y + 'px';
});

document.addEventListener('mousedown', function(){
  cursor.classList.add('click');
  cursorinner.classList.add('cursorinnerhover')
});

document.addEventListener('mouseup', function(){
  cursor.classList.remove('click')
  cursorinner.classList.remove('cursorinnerhover')
});

a.forEach(item => {
  item.addEventListener('mouseover', () => {
    cursorinner.classList.add('hover');
  });
  item.addEventListener('mouseleave', () => {
    cursorinner.classList.remove('hover');
  });
})


$('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
  type: 'iframe',
  mainClass: 'mfp-fade',
  removalDelay: 160,
  preloader: true,
  fixedContentPos: false
});
$('.image-popup-vertical-fit').magnificPopup({
  type: 'image',
  closeOnContentClick: true,
  mainClass: 'mfp-img-mobile',
  image: {
      verticalFit: true
  }
});

// gallery js

$('.portfolio_img_text').magnificPopup({
  delegate: '.img-link',
  type: 'image',
  tLoading: 'Loading image #%curr%...',
  mainClass: 'mfp-img-mobile',
  gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0, 1]
  },
  image: {
      tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
      titleSrc: function (item) {
          return item.el.attr('title') + '<small></small>';
      }
  }
});
$('.portfolio_img_icon').magnificPopup({
  delegate: '.img-link',
  type: 'image',
  tLoading: 'Loading image #%curr%...',
  mainClass: 'mfp-img-mobile',
  gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0, 1]
  },
  image: {
      tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
      titleSrc: function (item) {
          return item.el.attr('title') + '<small></small>';
      }
  }
});


