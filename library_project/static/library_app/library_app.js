let slideIndex = 1;
showSlides(slideIndex);

function showSlides(num) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    if (num > slides.length) {
        slideIndex = 1
    }    
    if (num < 1) {
        slideIndex = slides.length
    }
    // default to setting slides and dots as display: hidden/none
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    // set current slide and dot to showing/emphasized
    slides[slideIndex-1].style.display = "block";  
    dots[slideIndex-1].className += " active";
}

function plusSlides(num) {
    showSlides(slideIndex += num);
}

function currentSlide(num) {
    showSlides(slideIndex = num);
}


